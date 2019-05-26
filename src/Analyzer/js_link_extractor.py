from bs4 import BeautifulSoup
from typing import List

from IO import out


def extract_js_link(parsed_html: BeautifulSoup) -> List[str]:
    """
    Extract JavaScript link from <script> tags in the parsed HTML.
    """

    script_tags = parsed_html.find_all("script")

    js_link_list: List[str] = []

    for script_tag in script_tags:
        js_link = script_tag.get("src")

        if js_link is not None:
            out.add("Extracted JavaScript link: {js_link}".format(js_link=js_link))
            js_link_list.append(js_link)

    return js_link_list
    