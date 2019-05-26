import sys

from bs4 import BeautifulSoup
from typing import List, Optional, Dict

from DB.configdb import ConfigDB
from DB.contentdb import ContentDB
from DB.cspdb import CSPDB
from IO import ask, out
from Validation import url as url_validator
from Loader.html_loader import load_html
from Loader.js_loader import load_external_js
from Loader.style_loader import load_external_style
from Analyzer.html_parser import parse_html
from Analyzer.js_link_extractor import extract_js_link
from Analyzer.style_link_extractor import extract_style_link
from Analyzer.html_analyzer import analyze_html
from Analyzer.js_analyzer import analyze_js
from Model.external_js import ExternalJS
from Model.external_style import ExternalStyle
from CSP.csp_generator import generate_csp

# Generate singleton object dealing with global config and csp information
configDB: ConfigDB = ConfigDB()
contentDB: ContentDB = ContentDB()
cspDB: CSPDB = CSPDB()


def get_target_url_from_user() -> str:
    """
    Receive a URL from the user by stdin, then return it if it is within valid URL format.
    
    [ok] http://correct.com  
    [ng] invalid.net
    """

    url: str = ask.ask("Target URL")

    if url_validator.is_validate_url(url):
        return url
    else:
        sys.exit(-1)


def main() -> None:
    out.info("CSP Configuration Automation System activated")

    configDB.set_url(get_target_url_from_user())

    #################
    # Part1         #
    #################
    out.info("Load contents")

    # TODO: Move loading process to other file

    html: str = load_html(configDB.get_url())
    contentDB.set_parsed_html(parse_html(html))

    js_links: List[str] = extract_js_link(contentDB.get_parsed_html())
    contentDB.set_js_links(js_links)
    
    for js_link in contentDB.get_js_links():
        external_js: Optional[ExternalJS] = load_external_js(js_link)

        if external_js is not None:
            contentDB.add_external_js_list(external_js)

    
    style_links: List[str] = extract_style_link(contentDB.get_parsed_html())
    contentDB.set_style_links(style_links)

    for style_link in contentDB.get_style_links():
        external_style: Optional[ExternalStyle] = load_external_style(style_link)

        if external_style is not None:
            contentDB.add_external_style_list(external_style)

    
    #################
    # Part2         #
    #################
    out.info("Analyze HTML")

    analyze_html(parsed_html=contentDB.get_parsed_html())


    #################
    # Part3         #
    #################
    out.info("Analyze JavaScript")

    analyze_js(inline_js_list=contentDB.get_inline_js_list(), 
               event_handler_list=contentDB.get_event_handler_list(),
               external_js_list=contentDB.get_external_js_list())


    #################
    # Part4         #
    #################
    out.info("Generate CSP")

    generate_csp(inline_js_list=contentDB.get_inline_js_list(),
                 external_js_list=contentDB.get_external_js_list(),
                 inline_style_list=contentDB.get_inline_style_list(),
                 external_style_list=contentDB.get_external_style_list(),
                 url_in_js_list=contentDB.get_url_in_js_list())
    

if __name__ == '__main__':
    main()