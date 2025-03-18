from flask import Flask, render_template, request, jsonify
from scraper import scrape_product

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    url = data.get("url")
    product_data = scrape_product(url)
    return jsonify(product_data)


if __name__ == "__main__":
    app.run(debug=True)
