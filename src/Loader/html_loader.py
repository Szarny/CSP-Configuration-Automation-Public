import sys 

import requests

from IO import out


def load_html(url: str) -> str:
    """
    Load HTML by using requests library.
    """

    try:
        html = requests.get(url).text
        out.add("Loaded {url}".format(url=url))

        return html

    except:
        out.error("Failed to get {url}".format(url=url))
        sys.exit(-1)

    