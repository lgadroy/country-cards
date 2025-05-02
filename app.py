from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://restcountries.com/v3.1/name/"

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("country")
    lang = request.args.get("lang", "en")  # Langue par défaut
    countries = []

    if query:
        response = requests.get(f"{API_URL}{query}")
        if response.status_code == 200:
            raw_data = response.json()
            for country in raw_data:
                # Le nom commun et officiel du pays est basé sur la langue choisie
                if lang == "fr" and 'translations' in country and 'fra' in country['translations']:
                    country['official_name'] = country['translations']['fra']['official']
                    country['name']['common'] = country['translations']['fra']['common']
                else:
                    country['official_name'] = country.get("name", {}).get("official", "Unknown")
                    country['name']['common'] = country.get("name", {}).get("common", "Unknown")

                countries.append(country)

    return render_template("index.html", countries=countries, lang=lang)

if __name__ == "__main__":
    from waitress import serve
    app.run(debug=True, host="127.0.0.1", port=8080)
    #serve(app, host="0.0.0.0", port=8080)
