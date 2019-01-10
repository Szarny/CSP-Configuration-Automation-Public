import re

from Output import Output
from Util.EventlistenerList import eventlistener_list


def analyze(parsed_html, csp_info_db, url):
    """
    HTMLファイルを解析し，以下の項目をCSPデータベースに保存する．
    - javascript:スキームをhrefとするリンク
    - 外部を参照するJavaScriptリンク
    - 外部を参照するCSSリンク
    - インラインスクリプト
    - インラインスタイル

    Parameters
    ----------
    parsed_html : BeautifulSoup
        BeautifulSoupにてパースしたHTML
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    url : str
        対象となるURL

    Returns
    -----------
    result : bool
        実行結果
    """

    try:
        # javascript:スキームをhrefとするリンクを抽出
        extract_javascript_scheme_in_anchor(
            parsed_html, csp_info_db, url)

        # 外部を参照するJavaScriptのリンクおよびインラインスクリプトを抽出
        extract_javascript(parsed_html, csp_info_db, url)

        # 外部を参照するCSSのリンクおよびインラインスタイルを抽出
        extract_style(parsed_html, csp_info_db, url)

        return True
        
    except:
        return False


def extract_javascript_scheme_in_anchor(parsed_html, csp_info_db, filename):
    """
    HTMLファイルを解析し，javascript:スキームをhrefとするリンクを違反リストに追加する

    Parameters
    ----------
    parsed_html : BeautifulSoup
        BeautifulSoupにてパースしたHTML
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    filename : str
        解析対象ファイル名
    """

    anchor_tag_list = parsed_html.find_all("a")
    
    for anchor_tag in anchor_tag_list:
        href = anchor_tag.get("href")

        if href.startswith("javascript:"):

            Output.warn("Extracted javascript: Scheme\n{}".format(anchor_tag))

            # CSPポリシー違反リストに違反内容を追加
            csp_info_db.add_violation_list(
                category=csp_info_db.VIOLATION_CATEGORY_JAVASCRIPT_SCHEME,
                filename=filename,
                line=-1
            )


def extract_javascript(parsed_html, csp_info_db, url):
    """
    HTMLテキストからJavaScriptのタグを抽出し，適切な関数に引き渡す．

    Parameters
    ----------
    parsed_html : BeautifulSoup
        BeautifulSoupにてパースしたHTML
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    url : str
        対象となるURL
    """

    script_tag_list = parsed_html.find_all("script")

    # HTMLコンテンツ内に存在するscriptタグ要素を走査
    for script_tag in script_tag_list:
        js_link = script_tag.get("src")

        if js_link is None:
            regist_inline_script(script_tag.text, csp_info_db)
        else:
            regist_external_javascript_link(js_link, csp_info_db, url)

    # 全タグからイベントリスナーを検出
    all_tag_list = parsed_html.find_all(re.compile("[a-zA-Z0-9]+"))

    for tag in all_tag_list:
        for eventlistener in eventlistener_list:
            script_text = tag.get(eventlistener)

            if script_text is not None:
                regist_inline_script(script_text, csp_info_db)
    

def regist_inline_script(script_text, csp_info_db):
    """
    インラインスクリプトをCSPデータベースに登録する

    Parameters
    ----------
    script_text : str
        スクリプト本体
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    """

    # hash_value = base64.b64encode(
    #     hashlib.sha256(script_text.encode()).digest())

    display_script_text = script_text.replace("\n", "").strip()

    Output.add("Extracted Inline JavaScript {}".format(
        display_script_text if len(display_script_text) < 20 else display_script_text[:17] + "..."
    ))

    csp_info_db.add_inline_script_list(script_text)


def regist_external_javascript_link(js_link, csp_info_db, url):
    """
    外部を参照するJavaScriptリンクをCSPデータベースに登録する

    Parameters
    ----------
    js_link : str
        外部を参照するJavaScriptリンク
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    url : str
        対象となるURL
    """

    if js_link.startswith("http"):
        target_js_link = js_link
    else:
        url_ = "/".join(url.split("/")[:-1])
        js_link_ = "/".join(js_link.split("/")[1:])
        target_js_link = url_ + "/" + js_link_

    Output.add("Extracted JavaScript Link {}".format(target_js_link))

    # CSPJavaScript読み込み元オリジンリストに追加
    csp_info_db.add_script_src_list(
        script_src=target_js_link
    )


def extract_style(parsed_html, csp_info_db, url):
    """
    HTMLテキストからstyleのタグを抽出し，適切な関数に引き渡す．

    Parameters
    ----------
    parsed_html : BeautifulSoup
        BeautifulSoupにてパースしたHTML
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    url : str
        対象となるURL
    """

    # HTMLコンテンツ内に存在するlinkタグ要素を走査
    link_tag_list = parsed_html.find_all("link")
    for link_tag in link_tag_list:
        link_rel = link_tag.get("rel")[0]
        link_href = link_tag.get("href")

        if link_rel == "stylesheet":
            regist_external_style_link(link_href, csp_info_db, url)

    # HTMLコンテンツ内に存在するstyleタグ要素を走査
    style_tag_list = parsed_html.find_all("style")
    for style_tag in style_tag_list:
        regist_inline_style(style_tag.text, csp_info_db)

    # 全タグからstyle属性を検出
    all_tag_list = parsed_html.find_all(re.compile("[a-zA-Z0-9]+"))

    for tag in all_tag_list:
        style_text = tag.get("style")

        # MEMO:
        # style属性についてはブラウザごとに実装が異なるため
        # ハッシュ値や'unsafe-inline'の追加は行わず，警告表示に止める．
        if style_text is not None:
            Output.warn("Extracted style attribute in\n{}".format(url))

            # CSPポリシー違反リストに違反内容を追加
            csp_info_db.add_violation_list(
                category=csp_info_db.VIOLATION_CATEGORY_STYLE_ATTRIBUTE,
                filename=url,
                line=-1
            )


def regist_inline_style(style_text, csp_info_db):
    """
    インラインスタイルをCSPデータベースに登録する

    Parameters
    ----------
    style_text : str
        スタイル本体
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    """

    display_style_text = style_text.replace("\n", "").strip()

    Output.add("Extracted Inline Style {}".format(
        display_style_text if len(display_style_text) < 20 else display_style_text[:17] + "..."
    ))

    csp_info_db.add_inline_style_list(style_text)


def regist_external_style_link(style_link, csp_info_db, url):
    """
    外部を参照するJavaScriptリンクをCSPデータベースに登録する

    Parameters
    ----------
    style_link : str
        外部を参照するstyleリンク
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    url : str
        対象となるURL
    """

    if style_link.startswith("http"):
        target_style_link = style_link
    else:
        url_ = "/".join(url.split("/")[:-1])
        style_link_ = "/".join(style_link.split("/")[1:])
        target_style_link = url_ + "/" + style_link_

    Output.add("Extracted Style Link {}".format(target_style_link))

    # CSPJavaScript読み込み元オリジンリストに追加
    csp_info_db.add_style_src_list(target_style_link)
