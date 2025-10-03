import re


def is_valid_youtube_url(url):
    pattern = r"^https://www\.youtube\.com/watch\?v=[\w-]+(&[\w\-=%]*)?$"
    return re.match(pattern, url) is not None
