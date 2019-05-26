from bs4 import BeautifulSoup


def parse_html(html_contents):
    """
    HTMLテキストをパースする

    Parameters
    ----------
    html_contents: str
        requestsにて取得し，textプロパティを抽出したHTML文字列

    Returns
    ----------
    parsed_html: BeautifulSoup
        BeautifulSoup(lxml)によってパース済みのHTML
    """

    parsed_html = BeautifulSoup(html_contents, "lxml")

    return parse_html