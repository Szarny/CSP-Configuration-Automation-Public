import requests
from typing import Optional

from IO import out
from DB.configdb import ConfigDB
from Model.external_js import ExternalJS
from Util.link_normalizer import normalize_link

configDB: ConfigDB = ConfigDB()


def load_external_js(js_link: str) -> Optional[ExternalJS]:
    """
    Receive link and load JavaScript.  
    If the link is relative, it will be properly converted in this function．
    """

    js_full_link: str = normalize_link(original_url=configDB.get_url(), 
                                       content_link=js_link)

    try:
        js_source_code: str = requests.get(js_full_link).text
    except:
        out.warn("Failed to load: {js_link}".format(js_link=js_link))
        return None

    out.add("Load: {js_full_link}".format(js_full_link=js_full_link))

    external_js: ExternalJS = ExternalJS(source_code=js_source_code,
                                                link=js_link,
                                                full_link=js_full_link)

    return external_js