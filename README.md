# Amazon Product Scraper

A web application built with **Python (Flask)** and **Selenium** that allows users to scrape product details from Amazon. The application extracts information such as product name, price, description, images, reviews, availability, and specifications. The data is displayed in a clean, structured, and tabular format on the frontend.

---

## Features

- **Scrape Product Details**: Extract product information from Amazon URLs.
- **Structured Display**: Display scraped data in a clean and organized tabular format.
- **Image Carousel**: View product images in a carousel with navigation buttons.
- **Dynamic Loading**: Show a loading spinner while the data is being scraped.
- **Error Handling**: Display user-friendly error messages for invalid URLs or scraping failures.
- **Export Data**: Download the scraped data as a CSV file.

---

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Web Scraping**: Selenium, BeautifulSoup
- **Browser Automation**: ChromeDriver (managed by `webdriver-manager`)
- **Styling**: Custom CSS for a clean and responsive UI

---

## Setup Instructions

### Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Chrome Browser**: The application uses ChromeDriver for web scraping.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/amazon-product-scraper.git
   cd amazon-product-scraper
   
