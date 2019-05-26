from bs4 import BeautifulSoup
from typing import List

class ConfigDB:
    __instance = None

    url: str = ""

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


    def set_url(self, url: str) -> None:
        self.url = url

    
    def get_url(self) -> str:
        return self.url
