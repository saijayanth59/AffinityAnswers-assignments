import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.olx.in/items/q-car-cover"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en;q=0.7",
    "cookie": ";",
    "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}


def extract_details(items):
    data = []
    for li in items:
        price = li.find("span", attrs={'data-aut-id': 'itemPrice'})
        title = li.find('span', attrs={'data-aut-id': 'itemTitle'})
        location = li.find('span', attrs={'data-aut-id': 'item-location'})
        time = li.find("span", class_="_2jcGx")

        image_tag = li.find("figure", attrs={"data-aut-id": "itemImage"})
        image_link = image_tag.find(
            "img")['src'] if image_tag and image_tag.find("img") else None

        data.append({
            "price": price.text.strip() if price else None,
            "title": title.text.strip() if title else None,
            "location": location.text.strip() if location else None,
            "time": time.text.strip() if time else None,
            "image_link": image_link
        })
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"olx_data_{timestamp}.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["price", "title", "location", "time", "image_link"])
        writer.writeheader()
        writer.writerows(data)


def get_data():
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    main_content = soup.find("ul", attrs={"data-aut-id": "itemsList1"})
    items = main_content.find_all("li", attrs={"data-aut-id": "itemBox3"})
    extract_details(items)


if __name__ == "__main__":
    try:
        get_data()
        print("Data extraction completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
