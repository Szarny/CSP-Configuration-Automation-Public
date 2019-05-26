from typing import List

class EventListener:
    def __init__(self):
        self.event_listener_list: List[str] = [
            "onclick", 
            "onmousemove", 
            "onmouseover", 
            "onmousedown", 
            "onmouseup", 
            "onmouseout",
            "onkeypress", 
            "onkeydown", 
            "onkeyup",
            "onselect", 
            "onchange", 
            "onsubmit", 
            "onreset", 
            "onfocus", 
            "onblur",
            "onload", 
            "onscroll", 
            "onresize"
        ]