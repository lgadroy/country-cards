from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://restcountries.com/v3.1/name/"

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("country")
    lang = request.args.get("lang", "en")  # Default language
    countries = []

    if query:
        response = requests.get(f"{API_URL}{query}")
        if response.status_code == 200:
            raw_data = response.json()
            for country in raw_data:
                # Official name changes based on language you choose
                if lang == "fr" and 'translations' in country and 'fra' in country['translations']:
                    country['official_name'] = country['translations']['fra']['official']
                    country['name']['common'] = country['translations']['fra']['common']
                else:
                    country['official_name'] = country.get("name", {}).get("official", "Unknown")
                    country['name']['common'] = country.get("name", {}).get("common", "Unknown")

                countries.append(country)

    return render_template("index.html", countries=countries, lang=lang)

if __name__ == "__main__":
    app.run(debug=True)
