import re

result = re.findall(
    "https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
    "hogehttp://example.com;afeahttps://www.google.com?hoge=//fafaegei")

print(result)