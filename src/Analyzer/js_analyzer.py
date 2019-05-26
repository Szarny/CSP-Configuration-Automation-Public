import re

from typing import List

from IO import out
from DB.configdb import ConfigDB
from DB.contentdb import ContentDB
from DB.cspdb import CSPDB
from Model.inline_js import InlineJS
from Model.event_handler import EventHandler
from Model.external_js import ExternalJS
from Model.violation import Violation
from Model.violation_category import ViolationCategory


configDB: ConfigDB = ConfigDB()
contentDB: ContentDB = ContentDB() 
cspDB: CSPDB = CSPDB()


def regist_inner_outer_html(filename: str, line: int) -> None:
    out.warn("Detect innerHTML/outerHTML @ {filename}:{line}".format(filename=filename, line=line))
    cspDB.add_violation_list(Violation(category=ViolationCategory.VIOLATION_CATEGORY_INNER_OUTER_HTML,
                                       filename=filename,
                                       line=line))


def regist_document_write(filename: str, line: int) -> None:
    out.warn("Detect document.write(ln) function @ {filename}:{line}".format(filename=filename, line=line))
    cspDB.add_violation_list(Violation(category=ViolationCategory.VIOLATION_CATEGORY_DOCUMENT_WRITE,
                                       filename=filename,
                                       line=line))


def regist_eval_function(filename: str, line: int) -> None:
    out.warn("Detect eval function @ {filename}:{line}".format(filename=filename, line=line))
    cspDB.add_violation_list(Violation(category=ViolationCategory.VIOLATION_CATEGORY_EVAL,
                                       filename=filename,
                                       line=line))


def regist_Function_constructor(filename: str, line: int) -> None:
    out.warn("Detect Function() constructor @ {filename}:{line}".format(filename=filename, line=line))
    cspDB.add_violation_list(Violation(category=ViolationCategory.VIOLATION_CATEGORY_FUNCTION_CONSTRUCTOR,
                                       filename=filename,
                                       line=line))


def detect_violation(filename: str, source_code: str) -> None:
    for line_number, js_line in enumerate(source_code.split("\n"), start=1):

        if ("innerHTML" in js_line) or ("outerHTML" in js_line):
            regist_inner_outer_html(filename=filename, line=line_number)
        
        if "document.write" in js_line:
            regist_document_write(filename=filename, line=line_number)

        if "eval(" in js_line:
            regist_eval_function(filename=filename, line=line_number)

        if "new Function(" in js_line:
            regist_Function_constructor(filename=filename, line=line_number)



def detect_url(filename: str, source_code: str) -> None:
    url_list: List[str] = re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", source_code)

    for url in url_list:
        out.add("Detect URL @ {filename}".format(filename=filename))
        contentDB.add_url_in_js_list(url=url)


def analyze_js(inline_js_list: List[InlineJS], event_handler_list: List[EventHandler], external_js_list: List[ExternalJS]) -> None:
    inline_js: InlineJS
    event_handler: EventHandler
    external_js: ExternalJS

    for inline_js in inline_js_list:
        detect_violation(filename=configDB.get_url(), source_code=inline_js.get_source_code())
        detect_url(filename=configDB.get_url(), source_code=inline_js.get_source_code())

    
    for event_handler in event_handler_list:
        detect_violation(filename=configDB.get_url(), source_code=event_handler.get_source_code())
        detect_url(filename=configDB.get_url(), source_code=event_handler.get_source_code())
        

    for external_js in external_js_list:
        detect_violation(filename=external_js.get_full_link(), source_code=external_js.get_source_code())
        detect_url(filename=external_js.get_full_link(), source_code=external_js.get_source_code())
