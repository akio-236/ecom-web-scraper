import requests
from bs4 import BeautifulSoup


def scrape_product(url):
    try:
        # Simulate a real browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, "lxml")

        # Extract product details (customize for Amazon's structure)
        product_name = (
            soup.find("span", id="productTitle").get_text(strip=True)
            if soup.find("span", id="productTitle")
            else "N/A"
        )
        price = (
            soup.find("span", class_="a-price-whole").get_text(strip=True)
            if soup.find("span", class_="a-price-whole")
            else "N/A"
        )
        description = (
            soup.find("div", id="productDescription").get_text(strip=True)
            if soup.find("div", id="productDescription")
            else "N/A"
        )
        images = [
            img["src"]
            for img in soup.find_all("img", class_="a-dynamic-image")
            if img.get("src")
        ]
        reviews = [
            review.get_text(strip=True)
            for review in soup.find_all("span", class_="a-size-base review-text")
        ]
        availability = (
            soup.find("div", id="availability").get_text(strip=True)
            if soup.find("div", id="availability")
            else "N/A"
        )
        specifications = {
            spec.get_text(strip=True): value.get_text(strip=True)
            for spec, value in zip(
                soup.find_all(
                    "th", class_="a-color-secondary a-size-base prodDetSectionEntry"
                ),
                soup.find_all("td", class_="a-size-base prodDetAttrValue"),
            )
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
