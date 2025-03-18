# Web scraping logic

import requests
from bs4 import BeautifulSoup


def scrape_product(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        # Example scraping logic (customize for the target website)
        product_name = (
            soup.find("h1").get_text(strip=True) if soup.find("h1") else "N/A"
        )
        price = (
            soup.find("span", class_="price").get_text(strip=True)
            if soup.find("span", class_="price")
            else "N/A"
        )
        description = (
            soup.find("div", class_="description").get_text(strip=True)
            if soup.find("div", class_="description")
            else "N/A"
        )
        images = [img["src"] for img in soup.find_all("img") if img.get("src")]
        reviews = [
            review.get_text(strip=True)
            for review in soup.find_all("div", class_="review")
        ]
        availability = (
            soup.find("span", class_="availability").get_text(strip=True)
            if soup.find("span", class_="availability")
            else "N/A"
        )
        specifications = {
            spec.get_text(strip=True): value.get_text(strip=True)
            for spec, value in zip(soup.find_all("dt"), soup.find_all("dd"))
        }

        return {
            "Product Name": product_name,
            "Price": price,
            "Description": description,
            "Images": ", ".join(images),
            "Reviews": ", ".join(reviews),
            "Availability": availability,
            "Specifications": str(specifications),
        }

    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL: {e}"
