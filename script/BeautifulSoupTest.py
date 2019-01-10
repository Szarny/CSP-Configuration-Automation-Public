import requests
from bs4 import BeautifulSoup
import re

url = "http://localhost:8080/index.php"
html_response = requests.get(url)
html_contents = html_response.text

parsed_html = BeautifulSoup(html_contents, "html.parser")

for tag in parsed_html.find_all(re.compile("[a-zA-Z0-9]+")):
    eventhandler = tag.get(re.compile(""))
    print(eventhandler)