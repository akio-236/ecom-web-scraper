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
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

## Running the Application
   1. **Start the Flask server:**
      ```bash
      python app.py
   2. **Open your browser and go to:**
      ```bash
      http://127.0.0.1:5000
## Project Structure
  ```bash
 amazon-product-scraper/
├── app.py                      # Flask backend (main application)
├── scraper.py                  # Web scraping logic
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── templates/
│   └── index.html              # Frontend UI
└── static/
    ├── css/
    │   └── styles.css          # Custom CSS
    └── js/
        └── script.js           # Custom JavaScript
```
## Usage

1. **Enter Amazon Product Url:**
   - Paste the URL of an Amazon product into the input field.
2. **Scrape Data:**
   - Click the Scrape button to extract and display the product details.
3. **View Results:**
   - The scraped data will be displayed in a structured format, including:
     - Product Name
     - Price
     - Description
     - Images
     - Specifications
     - Reviews
## Screenshots
### Home Page
![{E340BE40-D0D7-43C7-B11C-6ED9DC87865A}](https://github.com/user-attachments/assets/4d3d8c81-6f92-4df9-8073-1e5823d70b03)
### Scraped Results
![{DB8E42D1-55D4-4F9A-BE4A-DFE5284FD58B}](https://github.com/user-attachments/assets/e171a1c6-cf07-492e-9bf3-b0897e0856a7)
![{D5495BEC-6B13-4601-A383-3D79E2674318}](https://github.com/user-attachments/assets/7a81cad0-95aa-4d67-b0e1-43b8fa16b5cc)
![{A41AA989-B9F6-4C0C-847C-16BBEFB4777D}](https://github.com/user-attachments/assets/361248bb-cda8-4b68-9a68-c584945d7193)

## Contributing
**Contributions are welcome! If you'd like to contribute to this project, please follow these steps:**
   1. Fork the repository.
   2. Create a new branch for your feature or bugfix.
   3. Commit your changes.
   4. Push your branch to your forked repository.
   5. Submit a pull request.
      
