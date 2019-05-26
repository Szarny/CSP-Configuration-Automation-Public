from hashlib import sha256
from base64 import b64encode

from typing import List

from IO import ask
from Model.inline_js import InlineJS
from Model.event_handler import EventHandler
from Model.external_js import ExternalJS
from Model.inline_style import InlineStyle
from Model.external_style import ExternalStyle


def generate_script_src(inline_js_list: List[InlineJS], external_js_list: List[ExternalJS]) -> str:
    external_js_origin_list: List[str] = list(set([external_js.get_origin() 
                                                   for external_js 
                                                   in external_js_list]))

    external_js_hash_list: List[str] = list(set([b64encode(sha256(external_js.get_source_code().encode()).digest()).decode()
                                                 for external_js 
                                                 in external_js_list]))

    inline_js_hash_list: List[str] = list(set([b64encode(sha256(inline_js.get_source_code().encode()).digest()).decode()
                                               for inline_js 
                                               in inline_js_list]))

    external_js_origins: str = " ".join(external_js_origin_list)
    external_js_hashes: str = " ".join(external_js_hash_list)
    inline_js_hashes: str = " ".join(inline_js_hash_list)

    return "{} {} {} {} {}".format("self",
                                   external_js_origins, 
                                   external_js_hashes, 
                                   inline_js_hashes,
                                   "strict-dynamic")
    
    
def generate_style_src(inline_style_list: List[InlineStyle], external_style_list: List[ExternalStyle]) -> str:
    external_style_origin_list: List[str] = list(set([external_style.get_origin() 
                                                      for external_style
                                                      in external_style_list]))

    external_style_hash_list: List[str] = list(set([b64encode(sha256(external_style.get_source_code().encode()).digest()).decode()
                                                                     for external_style 
                                                                     in external_style_list]))

    inline_style_hash_list: List[str] = list(set([b64encode(sha256(inline_style.get_source_code().encode()).digest()).decode()
                                                                   for inline_style
                                                                   in inline_style_list]))

    external_style_origins: str = " ".join(external_style_origin_list)
    external_style_hashes: str = " ".join(external_style_hash_list)
    inline_style_hashes: str = " ".join(inline_style_hash_list)

    return "{} {} {} {}".format("self", 
                                external_style_origins, 
                                external_style_hashes, 
                                inline_style_hashes)


def generate_connect_src(url_in_js_list: List[str]) -> str:
    connect_src_origins: List[str] = []

    for url_in_js in list(set(url_in_js_list)):
        is_connect_src = ask.ask("Add {} to connect-src? (y/n) >> ".format(url_in_js)) != "n"

        if is_connect_src:
            connect_src_origins.append(url_in_js)

    connect_src_origins.insert(0, "'self'")

    return " ".join(connect_src_origins)


def generate_csp(inline_js_list: List[InlineJS], 
                 external_js_list: List[ExternalJS],
                 inline_style_list: List[InlineStyle],
                 external_style_list: List[ExternalStyle],
                 url_in_js_list: List[str]) -> None:

    script_src: str = generate_script_src(inline_js_list, external_js_list)
    style_src: str = generate_style_src(inline_style_list, external_style_list)
    connect_src: str = generate_connect_src(url_in_js_list)
    


    