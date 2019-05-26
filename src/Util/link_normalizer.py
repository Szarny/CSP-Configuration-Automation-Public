def normalize_link(original_url: str, content_link: str) -> str:
    if content_link.startswith("http"):
        return content_link

    origin: str = "/".join(original_url.split("/")[:-1])
    content_path: str = "/".join(content_link.split("/")[1:])
    return origin + "/" + content_path