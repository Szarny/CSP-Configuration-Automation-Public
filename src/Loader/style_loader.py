import requests
from typing import Optional

from IO import out
from DB.configdb import ConfigDB
from Model.external_style import ExternalStyle
from Util.link_normalizer import normalize_link

configDB: ConfigDB = ConfigDB()


def load_external_style(style_link: str) -> Optional[ExternalStyle]:
    """
    Receive link and load stylesheet.  
    If the link is relative, it will be properly converted in this function．
    """

    style_full_link: str = normalize_link(original_url=configDB.get_url(),
                                          content_link=style_link)

    try:
        style_source_code: str = requests.get(style_full_link).text
    except:
        out.warn("Failed to load: {style_link}".format(style_link=style_link))
        return None

    
    out.add("Load: {style_full_link}".format(style_full_link=style_full_link))

    external_style: ExternalStyle = ExternalStyle(source_code=style_source_code,
                                                link=style_link,
                                                full_link=style_full_link)

    return external_style