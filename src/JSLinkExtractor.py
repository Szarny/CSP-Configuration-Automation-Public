from bs4 import BeautifulSoup

from Output import Output


def js_link_extractor(html_contents):
    """
    HTMLテキストからJavaScriptのリンク情報を抽出する．

    Parameters
    ----------
    html_contents : str
        requestsにて取得し，textプロパティを抽出したHTML文字列

    Returns
    ----------
    js_link_list : list
        JavaScriptのリンク情報を格納したリスト
    """

    parsed_html = BeautifulSoup(html_contents, "html.parser")
    script_tag_list = parsed_html.find_all("script")

    js_link_list = []

    # HTMLコンテンツ内に存在するscriptタグ要素を走査
    for script_tag in script_tag_list:
        js_link = script_tag.get("src")

        # インラインスクリプトは無視
        if js_link is not None:
            Output.add("Extracted {}".format(js_link))
            js_link_list.append(js_link)

    return js_link_list, parsed_html
    