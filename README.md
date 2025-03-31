# Country Cards

Country Cards is a web application developed in Python (version 3.12.4) using Flask. It allows users to search for information about a given country using the REST Countries API.

## Features
- Search for countries by name
- Display countries information in flash cards
- Support for displaying names in French or English

## Project Structure
```
Country-Cards/
│-- static/
│   └── style.css
│-- templates/
│   └── index.html
│-- .gitignore
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
   Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## `requirements.txt` Content
```
Flask
requests
```

## License
This project is licensed under the MIT License.