# Country Cards

Country Cards is a lightweight web application built with Python 3.12.4 and Flask. It allows users to search and view detailed information about every countries in the world, thanks to the REST Countries API.

## Features
- Search for countries by name
- Display countries information in flash cards format
- You can now download the flashcards in .png
- Languages supported : French and English

## Project Structure
```
Country-Cards/
│-- static/
│   └── style.css
    └── download.png
    └── favicon.png
    └── logo.png
    └── france.png
    └── uk.png
│-- templates/
│   └── index.html
│-- .gitignore
│-- LICENCE
│-- README.md
│-- app.py
│-- requirements.txt
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lgadroy/country-cards.git
   cd country-cards
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   ```
   # Open a browser and go to:
   http://127.0.0.1:8080/
   ```

## License
This project is licensed under the MIT License.