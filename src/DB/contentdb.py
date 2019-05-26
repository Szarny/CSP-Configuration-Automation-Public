from typing import List
from bs4 import BeautifulSoup

from Model.external_js import ExternalJS
from Model.external_style import ExternalStyle
from Model.inline_js import InlineJS
from Model.event_handler import EventHandler
from Model.inline_style import InlineStyle


class ContentDB:
    __instance = None

    parsed_html: BeautifulSoup = ""
    js_links: List[str] = []
    external_js_list: List[ExternalJS] = []
    external_style_list: List[ExternalStyle] = []
    inline_js_list: List[InlineJS] = []
    inline_style_list: List[InlineStyle] = []
    event_handler_list: List[EventHandler] = []
    url_in_js_list: List[str] = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def __str__(self) -> str:
        retstr: str = ""
        retstr += "External JavaScript: {external_js_list}\n".format(external_js_list=self.external_js_list)
        retstr += "External Style: {external_style_list}\n".format(external_style_list=self.external_style_list)
        retstr += "Inline JavaScript: {inline_js_list}\n".format(inline_js_list=self.inline_js_list)
        retstr += "Event Handler: {event_handler_list}\n".format(event_handler_list=self.event_handler_list)
        retstr += "Inline Style: {inline_style_list}\n".format(inline_style_list=self.inline_style_list)
        retstr += "URL in JavaScript: {url_in_js_list}\n".format(url_in_js_list=self.url_in_js_list)
        return retstr


    def set_parsed_html(self, parsed_html: BeautifulSoup) -> None:
        self.parsed_html = parsed_html

    
    def get_parsed_html(self) -> BeautifulSoup:
        return self.parsed_html

    
    def set_js_links(self, js_links: List[str]) -> None:
        self.js_links = js_links

    
    def get_js_links(self) -> List[str]:
        return self.js_links


    def set_style_links(self, style_links: List[str]) -> None:
        self.style_links = style_links

    
    def get_style_links(self) -> List[str]:
        return self.style_links


    def add_external_js_list(self, external_js: ExternalJS) -> None:
        self.external_js_list.append(external_js)

    
    def get_external_js_list(self) -> List[ExternalJS]:
        return self.external_js_list

    
    def add_external_style_list(self, external_style: ExternalStyle) -> None:
        self.external_style_list.append(external_style)

    
    def get_external_style_list(self) -> List[ExternalStyle]:
        return self.external_style_list


    def add_inline_js_list(self, inline_js: InlineJS) -> None:
        self.inline_js_list.append(inline_js)

    
    def get_inline_js_list(self) -> List[InlineJS]:
        return self.inline_js_list


    def add_event_handler_list(self, event_handler: EventHandler) -> None:
        self.event_handler_list.append(event_handler)

    
    def get_event_handler_list(self) -> List[EventHandler]:
        return self.event_handler_list


    def add_inline_style_list(self, inline_style: InlineStyle) -> None:
        self.inline_style_list.append(inline_style)

    
    def get_inline_style_list(self) -> List[InlineStyle]:
        return self.inline_style_list


    def add_url_in_js_list(self, url: str) -> None:
        self.url_in_js_list.append(url)

    
    def get_url_in_js_list(self) -> List[str]:
        return self.url_in_js_list
