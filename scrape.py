import requests
from bs4 import BeautifulSoup
import json

recipes = []

urls = [
    "https://www.bbcgoodfood.com/recipes/chicken-pasta-bake",
    "https://www.bbcgoodfood.com/recipes/creamy-mushroom-pasta",
    "https://www.bbcgoodfood.com/recipes/cajun-chicken-pasta"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in urls:
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)

    ingredients = []

    items = soup.find_all("li")

    for item in items:
        text = item.get_text(strip=True)

        if text != "":
            ingredients.append(text)

    recipes.append({
        "title": title,
        "ingredients": ingredients[:10]
    })

with open("recipes.json", "w", encoding="utf-8") as file:
    json.dump(recipes, file, indent=4, ensure_ascii=False)

print("BBC Good Food recipes saved")