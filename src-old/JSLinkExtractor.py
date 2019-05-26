from bs4 import BeautifulSoup

from Output import Output


def js_link_extractor(parsed_html):
    """
    HTMLテキストからJavaScriptのリンク情報を抽出する．

    Parameters
    ----------
    parsed_html: BeautifulSoup
        BeautifulSoupにてパースしたHTML

    Returns
    ----------
    js_link_list: list
        JavaScriptのリンク情報を格納したリスト
    """

    script_tag_list = parsed_html.find_all("script")

    js_link_list = []

    # HTMLコンテンツ内に存在するscriptタグ要素を走査
    for script_tag in script_tag_list:
        js_link = script_tag.get("src")

        # インラインスクリプトは無視
        if js_link is not None:
            Output.add("Extracted {}".format(js_link))
            js_link_list.append(js_link)

    return js_link_list
    