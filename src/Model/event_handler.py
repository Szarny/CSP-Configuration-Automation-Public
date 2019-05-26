import bs4

class EventHandler:
    def __init__(self, source_code: str, event_listener: str, tag: bs4.element.Tag):
        self.source_code: str = source_code
        self.event_listener: str = event_listener
        self.tag:bs4.element.Tag = bs4.element

    
    def get_source_code(self) -> str:
        return self.source_code


    def get_event_listener(self) -> str:
        return self.event_listener


    def get_tag(self) -> bs4.element.Tag:
        return self.tag