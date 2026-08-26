from bs4 import BeautifulSoup


def parse_dom(html):
    soup = BeautifulSoup(html, "html.parser")

    elements = []

    for tag in soup.find_all(
        ["input", "button", "a", "textarea"]
    ):
        elements.append({
            "tag": tag.name,
            "text": tag.get_text(strip=True),
            "id": tag.get("id"),
            "name": tag.get("name"),
            "placeholder": tag.get("placeholder"),
            "type": tag.get("type")
        })

    return elements
