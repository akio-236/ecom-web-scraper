from flask import Flask, render_template, request
from scraper import scrape_product

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        product_data = scrape_product(url)
        if isinstance(product_data, dict):
            return render_template("index.html", product=product_data)
        else:
            return render_template("index.html", error=product_data)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
