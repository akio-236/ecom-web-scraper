from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_product(url):
    try:
        # Check if the URL is from Amazon
        if "amazon" not in url:
            return "Unsupported website. Please provide an Amazon URL."

        # Configure Selenium
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )

        # Set up WebDriver using webdriver-manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Fetch the page
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Scrape product details
        product_name = (
            driver.find_element(By.ID, "productTitle").text.strip()
            if driver.find_elements(By.ID, "productTitle")
            else "N/A"
        )
        price = (
            driver.find_element(By.CLASS_NAME, "a-price-whole").text.strip()
            if driver.find_elements(By.CLASS_NAME, "a-price-whole")
            else "N/A"
        )
        description = (
            driver.find_element(By.ID, "productDescription").text.strip()
            if driver.find_elements(By.ID, "productDescription")
            else "N/A"
        )
        images = [
            img.get_attribute("src")
            for img in driver.find_elements(By.CLASS_NAME, "a-dynamic-image")
            if img.get_attribute("src")
        ]
        reviews = [
            review.text.strip()
            for review in driver.find_elements(By.CLASS_NAME, "a-size-base.review-text")
        ]
        availability = (
            driver.find_element(By.ID, "availability").text.strip()
            if driver.find_elements(By.ID, "availability")
            else "N/A"
        )
        specifications = {
            spec.text.strip(): value.text.strip()
            for spec, value in zip(
                driver.find_elements(
                    By.CLASS_NAME, "a-color-secondary.a-size-base.prodDetSectionEntry"
                ),
                driver.find_elements(By.CLASS_NAME, "a-size-base.prodDetAttrValue"),
            )
        }

        driver.quit()  # Close the browser

        # Return structured data
        return {
            "Product Name": product_name,
            "Price": price,
            "Description": description,
            "Images": images,
            "Reviews": reviews,
            "Availability": availability,
            "Specifications": specifications,
        }

    except Exception as e:
        return f"Error fetching the URL: {e}"
