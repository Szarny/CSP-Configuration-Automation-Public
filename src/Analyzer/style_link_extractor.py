from bs4 import BeautifulSoup
from typing import List

from IO import out


def extract_style_link(parsed_html: BeautifulSoup) -> List[str]:
    """
    Extract style link from <link> tags in the parsed HTML.
    """

    link_tags = parsed_html.find_all("link")

    style_link_list: List[str] = []

    for link_tag in link_tags:
        rel = link_tag.get("rel")[0]
        href = link_tag.get("href")

        if rel == "stylesheet":
            out.add("Extracted style link: {href}".format(href=href))
            style_link_list.append(href)

    return style_link_list
    