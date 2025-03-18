document.getElementById('scraper-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent form submission

    // Show loading spinner
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('error-message').style.display = 'none';
    document.getElementById('results').style.display = 'none';

    const url = document.getElementById('url').value;

    try {
        // Send request to the backend
        const response = await fetch('/scrape', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url }),
        });

        const data = await response.json();

        if (data.error) {
            // Display error message
            document.getElementById('error-message').innerText = data.error;
            document.getElementById('error-message').style.display = 'block';
        } else {
            // Update the UI with scraped data
            document.getElementById('product-name').innerText = data['Product Name'];
            document.getElementById('product-price').innerText = data['Price'];
            document.getElementById('product-description').innerText = data['Description'];
            document.getElementById('product-availability').innerText = data['Availability'];

            // Update images
            const carouselImages = document.getElementById('carousel-images');
            carouselImages.innerHTML = '';
            data['Images'].forEach(image => {
                const img = document.createElement('img');
                img.src = image;
                carouselImages.appendChild(img);
            });

            // Update reviews
            const reviewsTable = document.getElementById('reviews').getElementsByTagName('tbody')[0];
            reviewsTable.innerHTML = '';
            data['Reviews'].forEach(review => {
                const row = reviewsTable.insertRow();
                const cell = row.insertCell(0);
                cell.innerText = review;
            });

            // Update specifications
            const specsTable = document.getElementById('specifications').getElementsByTagName('tbody')[0];
            specsTable.innerHTML = '';
            for (const [key, value] of Object.entries(data['Specifications'])) {
                const row = specsTable.insertRow();
                const cell1 = row.insertCell(0);
                const cell2 = row.insertCell(1);
                cell1.innerText = key;
                cell2.innerText = value;
            }

            // Show results section
            document.getElementById('results').style.display = 'block';
        }
    } catch (error) {
        // Handle fetch errors
        document.getElementById('error-message').innerText = 'An error occurred while fetching data.';
        document.getElementById('error-message').style.display = 'block';
    } finally {
        // Hide loading spinner
        document.getElementById('loading-spinner').style.display = 'none';
    }
});

// Image Carousel Navigation
let currentImageIndex = 0;

document.getElementById('next-button').addEventListener('click', () => {
    const images = document.querySelectorAll('#carousel-images img');
    if (currentImageIndex < images.length - 1) {
        currentImageIndex++;
        updateCarousel();
    }
});

document.getElementById('prev-button').addEventListener('click', () => {
    if (currentImageIndex > 0) {
        currentImageIndex--;
        updateCarousel();
    }
});

function updateCarousel() {
    const images = document.querySelectorAll('#carousel-images img');
    images.forEach((img, index) => {
        img.style.transform = `translateX(${-100 * currentImageIndex}%)`;
    });
}