from urllib.parse import urlparse
import base64
import hashlib

from Output import Output

def configure_csp(csp_info_db, parsed_html, timer):
    """
    CSPを自動構成する

    Parameters
    ----------
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース
    parsed_html : BeautifulSoup
        BeautifulSoupによってパースしたHTML
    timer : timer
        時間計測用モジュール

    Returns
    ----------
    csp_info_meta_format: str
        CSP構成情報(metaタグ形式)
    csp_info_for_display : str
        表示用CSP構成情報
    csp_info_external_script_integrity : str
        外部参照を行うscriptタグにintegrity属性を付与した文字列
    """

    ##############################
    # script-srcの設定情報を構成 #
    #############################

    # script-srcに外部スクリプトのドメインを追加
    script_src_list = csp_info_db.get_script_src_list()
    script_src_csp_list = configure_script_src_domain(script_src_list)

    # script-srcに外部スクリプトのハッシュ値を追加
    external_script_list = csp_info_db.get_external_script_list()
    script_src_csp_list.extend(configure_script_src_hash(external_script_list, csp_info_db))

    # script-srcにインラインスクリプトのハッシュ値を追加
    inline_script_list = csp_info_db.get_inline_script_list()
    script_src_csp_list.extend(configure_inline_script_hash(inline_script_list))

    script_src_csp_list.insert(0, "'self'")
    script_src_csp_list.append("'strict-dynamic'")

    Output.add("Configured script-src")

    #############################
    # style-srcの設定情報を構成 #
    ############################

    # style-srcに外部スタイルのドメインを追加
    style_src_list = csp_info_db.get_style_src_list()
    style_src_csp_list = configure_style_src_domain(style_src_list)

    # style-srcにインラインスタイルのハッシュ値を追加
    inline_style_list = csp_info_db.get_inline_style_list()
    style_src_csp_list.extend(configure_inline_style_hash(inline_style_list))

    style_src_csp_list.insert(0, "'self'")

    Output.add("Configured style-src")

    ###############################
    # connect-srcの設定情報を構成 #
    ##############################
    connect_src_list = csp_info_db.get_connect_src_list()
    connect_src_csp_list = configure_connect_src_domain(connect_src_list, timer)

    Output.add("Configured connect-src")

    #############################
    # CSPのペイロード情報を構成 #
    ############################
    csp_info_meta_format, csp_info_for_display = configure_csp_payload(
        script_src_csp_list=script_src_csp_list,
        style_src_csp_list=style_src_csp_list,
        connect_src_csp_list=connect_src_csp_list
    )

    ###############################
    # integrity付きのscriptを設定 #
    ##############################
    external_script_src_and_hash_list = csp_info_db.get_external_script_src_and_hash_list()
    csp_info_external_script_integrity = configure_external_script_integrity(external_script_src_and_hash_list, parsed_html)

    return csp_info_meta_format, csp_info_for_display, csp_info_external_script_integrity


def configure_script_src_domain(script_src_list):
    """
    script-srcのドメイン部を構成する

    Parameters
    ----------
    script_src_list : list
        スクリプト読み込み元オリジンのリスト
    
    Returns
    ----------
    script_src_csp_list : list
        CSPに設定するscript-srcのペイロードのリスト
    """

    script_src_csp_list = []
    
    # オリジンをフォーマットした上で処理
    for script_src in script_src_list:
        shaped_script_src = '{uri.scheme}://{uri.netloc}'.format(
            uri=urlparse(script_src))
        script_src_csp_list.append(shaped_script_src)

    script_src_csp_list = list(set(script_src_csp_list))

    return script_src_csp_list


def configure_script_src_hash(external_script_list, csp_info_db):
    """
    外部スクリプトのハッシュ値を計算し
    script-srcに設定するための情報のリストを返却する

    加えて，ファイル名とハッシュ値のペアをCSPInfoDBに格納する

    Parameters
    ----------
    external_script_list : list
        リンクとJavaScriptコンテンツの辞書を要素とするリスト
    csp_info_db : CSPInfoDB
        CSP自動構成用データベース

    Returns
    ----------
    inline_script_csp_list : list
        CSPに設定するscript-srcのペイロードのリスト
    """

    inline_script_csp_list = []
    hash_value_list_for_check_duplication = []

    for external_script in external_script_list:
        filename = external_script["filename"]
        original_src = external_script["original_src"]
        contents = external_script["contents"]

        hash_value = base64.b64encode(
            hashlib.sha256(contents.encode()).digest()).decode()

        if hash_value in hash_value_list_for_check_duplication:
            continue

        inline_script_csp_list.append("'sha256-{}'".format(hash_value))
        hash_value_list_for_check_duplication.append(hash_value)

        csp_info_db.set_external_script_src_and_hash_list(
            src=original_src, hash_value=hash_value
        )
    
    return inline_script_csp_list


def configure_style_src_domain(style_src_list):
    """
    style-srcを構成する

    Parameters
    ----------
    style_src_list : list
        CSS読み込み元オリジンのリスト
    
    Returns
    ----------
    style_src_csp_list : list
        CSPに設定するstyle-srcのペイロードのリスト
    """

    style_src_csp_list = []
    
    # オリジンをフォーマットした上で処理
    for style_src in style_src_list:
        shaped_style_src = '{uri.scheme}://{uri.netloc}'.format(
            uri=urlparse(style_src))
        style_src_csp_list.append(shaped_style_src)

    style_src_csp_list = list(set(style_src_csp_list))

    return style_src_csp_list


def configure_inline_script_hash(inline_script_list):
    """
    インラインスクリプトのハッシュ値を計算し
    script-srcに設定するための情報のリストを返却する

    Parameters
    ----------
    inline_script_list : list
        インラインスクリプトのコードを要素とするリストs

    Returns
    ----------
    inline_script_csp_list : list
        CSPに設定するscript-srcのペイロードのリスト
    """

    inline_script_csp_list = []
    hash_value_list_for_check_duplication = []

    for inline_script in inline_script_list:
        hash_value = base64.b64encode(
            hashlib.sha256(inline_script.encode()).digest()).decode()

        if hash_value in hash_value_list_for_check_duplication:
            continue

        inline_script_csp_list.append("'sha256-{}'".format(hash_value))
        hash_value_list_for_check_duplication.append(hash_value)

    return inline_script_csp_list


def configure_inline_style_hash(inline_style_list):
    """
    インラインスタイルのハッシュ値を計算し
    style-srcに設定するための情報のリストを返却する

    Parameters
    ----------
    inline_style_list : list
        インラインスタイルの内容を要素とするリスト

    Returns
    ----------
    inline_style_csp_list : list
        CSPに設定するstyle-srcのペイロードのリスト
    """

    inline_style_csp_list = []
    hash_value_list_for_check_duplication = []

    for inline_style in inline_style_list:
        hash_value = base64.b64encode(
            hashlib.sha256(inline_style.encode()).digest()).decode()

        if hash_value in hash_value_list_for_check_duplication:
            continue

        inline_style_csp_list.append("'sha256-{}'".format(hash_value))
        hash_value_list_for_check_duplication.append(hash_value)

    return inline_style_csp_list


def configure_connect_src_domain(connect_src_list, timer):
    """
    connect-srcを構成する

    Parameters
    ----------
    connect_src_list : list
        接続先である可能性があるオリジンのリスト
    timer : timer
        時間計測用モジュール
    
    Returns
    ----------
    connect_src_csp_list : list
        CSPに設定するconnect_srcのペイロードのリスト
    """

    connect_src_csp_list = []

    connect_src_list = list(set(connect_src_list))

    for connect_src in connect_src_list:
        timer.stop()

        is_connect_src = Output.ask(
            "Add {} to connect-src? (y/n) >> ".format(connect_src)) != "n"
            
        timer.start()

        if is_connect_src:
            connect_src_csp_list.append(connect_src)

    connect_src_csp_list.insert(0, "'self'")

    return connect_src_csp_list


def configure_csp_payload(script_src_csp_list, style_src_csp_list, connect_src_csp_list):
    """
    CSPペイロードを自動構成する

    Parameters
    ----------
    script_src_csp_list : list
        CSPに設定するscript-srcのペイロードのリスト
    style_src_csp_list : list
        CSPに設定するstyle-srcのペイロードのリスト
    connect_src_csp_list : list
        CSPに設定するconnect-srcのペイロードのリスト

    Returns
    ----------
    csp_info_meta_format: str
        CSP構成情報(metaタグ形式)
    csp_info_for_display : str
        表示用CSP校正情報
    """

    csp_info_meta_format = "<meta http-equiv=\"Content-Security-Policy\" content=\"default-src *; script-src {}; style-src {}; connect-src {}; base-uri 'none'\">"
    csp_info_for_display = "Content-Security-Policy:\n[default-src]\n*;\n\n[script-src]\n{}\n\n[style-src]\n{}\n\n[connect-src]\n{}\n\n[base-uri]\n'none'"

    return (
        csp_info_meta_format.format(
            " ".join(script_src_csp_list),
            " ".join(style_src_csp_list),
            " ".join(connect_src_csp_list)
        ),
        csp_info_for_display.format(
            "\n".join(script_src_csp_list),
            "\n".join(style_src_csp_list),
            "\n".join(connect_src_csp_list)
        )
    )


def configure_external_script_integrity(external_script_src_and_hash_list, parsed_html):
    """
    外部参照を行うscriptタグにintegrity属性を付与する

    Parameters
    ----------
    external_script_src_and_hash_list : list
        外部さん賞を行うscriptタグのsrc属性とハッシュ値
    parsed_html : BeautifulSoup
        BeutifulSoupによってパースしたHTML

    Returns
    ----------
    csp_info_external_script_integrity : str
        外部参照を行うscriptタグにintegrity属性を付与した文字列
    """

    # scriptタグから外部参照を行うものを抽出する
    def extract_external_script_tag(script_tag_list):
        external_script_tag_list = []

        for script_tag in script_tag_list:
            if script_tag.get("src") is not None:
                external_script_tag_list.append(script_tag)
        
        return external_script_tag_list

    external_script_integrity_list = []

    external_script_tag_list = extract_external_script_tag(parsed_html.find_all("script"))

    for external_script_src_and_hash in external_script_src_and_hash_list:
        src = external_script_src_and_hash["src"]
        hash_value = external_script_src_and_hash["hash_value"]
        integrity = "integrity=\"sha256-{}\"".format(hash_value)
        
        # 適切なscriptタグにintegrity属性を付与する
        for external_script_tag in external_script_tag_list:
            if external_script_tag.get("src") == src:
                
                # scriptタグにintegrity属性を挿入する処理
                external_script_tag_str = str(external_script_tag)
                splitted_external_script_tag_str = external_script_tag_str.split()
                splitted_external_script_tag_str.insert(1, integrity)
                external_script_integrity_list.append(
                    " ".join(splitted_external_script_tag_str))

    csp_info_external_script_integrity = "\n".join(external_script_integrity_list)

    return csp_info_external_script_integrity


