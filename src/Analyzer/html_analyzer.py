import re

import bs4
from bs4 import BeautifulSoup
from typing import Optional

from IO import out
from DB.configdb import ConfigDB
from DB.contentdb import ContentDB
from DB.cspdb import CSPDB
from Model.violation import Violation
from Model.violation_category import ViolationCategory
from Model.event_listener import EventListener
from Model.inline_js import InlineJS
from Model.event_handler import EventHandler
from Model.inline_style import InlineStyle


configDB: ConfigDB = ConfigDB()
contentDB: ContentDB = ContentDB()
cspDB: CSPDB = CSPDB()


def analyze_html(parsed_html: BeautifulSoup) -> None:
    extract_javascript_scheme_in_anchor_tag(parsed_html)
    extract_inline_js(parsed_html)
    extract_event_handler(parsed_html)
    extract_inline_style(parsed_html)


def extract_javascript_scheme_in_anchor_tag(parsed_html: BeautifulSoup) -> None:
    for a_tag in parsed_html.find_all("a"):
        if a_tag.get("href").startswith("javascript:"):
            out.warn("Extracted javascript: Scheme : {a_tag}".format(a_tag=a_tag))

            cspDB.add_violation_list(Violation(category=ViolationCategory.VIOLATION_CATEGORY_JAVASCRIPT_SCHEME,
                                               filename=configDB.get_url(),
                                               line=None))


def regist_inline_js(inline_js: InlineJS) -> None:
    source_code_for_display: str = inline_js.get_source_code().replace("\n", " ").strip()
    out.add("Extracted Inline JavaScript: {source_code_for_display}".format(
        source_code_for_display=source_code_for_display if len(source_code_for_display) < 20 else source_code_for_display[:17] + "..."
    ))

    contentDB.add_inline_js_list(inline_js=inline_js)


def extract_inline_js(parsed_html: BeautifulSoup) -> None:
    for script_tag in parsed_html.find_all("script"): 
        if script_tag.get("src") is None:
            regist_inline_js(InlineJS(source_code=script_tag.text))


def regist_event_handler(event_handler: EventHandler) -> None:
    source_code_for_display: str = event_handler.get_source_code().replace("\n", " ").strip()
    out.add("Extracted event hander({event_listener}): {source_code_for_display}".format(
        event_listener=event_handler.get_event_listener(),
        source_code_for_display=source_code_for_display if len(source_code_for_display) < 20 else source_code_for_display[:17] + "..."
    ))

    contentDB.add_event_handler_list(event_handler=event_handler)


def extract_event_handler(parsed_html: BeautifulSoup) -> None:
    for tag in parsed_html.find_all(re.compile("[a-zA-Z0-9]+")):
        for event_listener in EventListener().event_listener_list:
            if tag.get(event_listener) is not None:
                regist_event_handler(EventHandler(source_code=tag.get(event_listener),
                                                  event_listener=event_listener,
                                                  tag=tag))

 
def regist_inline_style(source_code: str) -> None:
    out.add("Extracted Inline Style: {source_code}".format(
        source_code=source_code if len(source_code) < 20 else source_code[:17] + "..."
    ))

    contentDB.add_inline_style_list(InlineStyle(source_code=source_code))


def extract_inline_style(parsed_html: BeautifulSoup) -> None:
    for style_tag in parsed_html.find_all("style"):
        regist_inline_style(source_code=style_tag.text)

    for tag in parsed_html.find_all(re.compile("[a-zA-Z0-9]+")):
        style_attribute = tag.get("style")

        if style_attribute is not None:
            out.warn("Extracted style attribute : {tag}".format(tag=tag))

            cspDB.add_violation_list(Violation(category=ViolationCategory.VIOLATION_CATEGORY_STYLE_ATTRIBUTE,
                                               filename=configDB.get_url(),
                                               line=None))
