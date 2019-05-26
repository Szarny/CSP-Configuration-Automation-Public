class ExternalJS:
    def __init__(self, source_code: str, link: str, full_link: str):
        self.source_code: str = source_code
        self.link: str = link
        self.full_link: str = full_link


    def __str__(self) -> str:
        return "<script src='{link}'>\n".format(link=self.link)


    def get_source_code(self) -> str:
        return self.source_code

    
    def get_link(self) -> str:
        return self.link


    def get_full_link(self) -> str:
        return self.full_link

    
    def get_origin(self) -> str:
        return self.full_link[:self.full_link.index("/", 8)]