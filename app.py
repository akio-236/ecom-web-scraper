# Flask backend (main application)

from flask import Flask, render_template, request, send_file
import pandas as pd
from scraper import scrape_product

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        product_data = scrape_product(url)
        if isinstance(product_data, dict):
            # Convert to DataFrame for display and CSV download
            df = pd.DataFrame([product_data])
            return render_template(
                "index.html",
                table=df.to_html(classes="table"),
                data=df.to_dict("records"),
            )
        else:
            return render_template("index.html", error=product_data)
    return render_template("index.html")


@app.route("/download")
def download():
    data = request.args.get("data")
    df = pd.DataFrame(eval(data))
    csv_file = "product_data.csv"
    df.to_csv(csv_file, index=False)
    return send_file(csv_file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
