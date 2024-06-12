import re

def link(url):
    patterns = [
        r"https?://(?:www\.)?([^\s]+)\.([^\s/]{2,}|[a-z]{2,})(/[^\s]*)?"
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True

    return False
input_url = input("Enter the Url: ")

if link(input_url):
    print(f"This URL '{input_url}' might be a phishing link.")
else:
    print(f"This URL '{input_url}' is not a phishing link.")