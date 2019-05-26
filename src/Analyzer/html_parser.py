from bs4 import BeautifulSoup


def parse_html(html: str) -> BeautifulSoup:
    """
    Parse HTML by Beautifulsoup and lxml parser.
    """

    return BeautifulSoup(html, "lxml")