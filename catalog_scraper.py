import requests
from bs4 import BeautifulSoup
import json

base_url = "https://www.shl.com"

url = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

assessments = []

links = soup.find_all("a", href=True)

for link in links:

    href = link["href"]

    if "/products/product-catalog/view/" in href.lower():

        name = link.get_text(strip=True)

        full_url = base_url + href

        assessments.append({
            "name": name,
            "url": full_url
        })

unique_assessments = []

seen = set()

for item in assessments:

    if item["url"] not in seen:

        seen.add(item["url"])

        unique_assessments.append(item)

with open("data/shl_catalog.json", "w") as f:

    json.dump(unique_assessments, f, indent=2)

print(f"Saved {len(unique_assessments)} assessments")