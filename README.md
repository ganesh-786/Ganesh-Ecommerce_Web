# AgriCart: E-Commerce Platform for Farmers

**Built solely by Ganesh Chaudhary.**

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technology Stack](#technology-stack)  
4. [Installation & Setup](#installation--setup)  
5. [Configuration](#configuration)  
6. [Running the Application](#running-the-application)  
7. [Folder Structure](#folder-structure)  
8. [Usage](#usage)  
9. [Translation & Localization](#translation--localization)  
10. [Weather Forecast Integration](#weather-forecast-integration)  
11. [Techniques for Farmers](#techniques-for-farmers)  
12. [License](#license)  

---

## Project Overview

AgriCart is a Flask-based e-commerce platform tailored for farmers. It provides a seamless shopping experience, allowing users to browse agricultural products, add items to their cart, and complete checkouts. Key differentiators include:

- **User Authentication**: Secure login/logout functionality powered by Flask-Login.  
- **Weather Forecast**: Real-time weather information to help farmers plan activities.  
- **Farming Techniques**: A dedicated section offering best practices and tips.  
- **Nepali Language Support**: Full translation/localization for Nepali-speaking users.  
- **Shopping Cart Management**: Add-to-cart, view/edit cart, and checkout flows.  
- **Payment Integration**: Supports IntaSend’s payment gateway via `intasend-python`.  

This project was built solely by the author from the ground up.

---

## Features

- **Authentication**  
  - User registration, login, logout (Flask-Login).  
  - Password hashing and session management.  

- **Product Catalog & Shopping Cart**  
  - Browse farm-related products.  
  - “Add to Cart” button for each product.  
  - View, update, and remove items in the cart.  

- **Weather Forecast**  
  - Fetches current weather data from a third-party API (e.g., OpenWeatherMap) using `requests`.  
  - Displays temperature, humidity, and condition summaries.  

- **Techniques for Farmers**  
  - Static/static-dynamic pages containing crop rotation, pest control, irrigation, and soil management tips.  
  - Categorized by season and crop type.  

- **Nepali Language Translation**  
  - Bilingual pages (English / Nepali).  
  - Uses Flask-Babel or custom Jinja2 templates and `.po` files for localization.  

- **Cart & Checkout Flow**  
  - Session-based cart handling (Flask sessions or SQLAlchemy models).  
  - User can review cart, adjust quantities, and view subtotal/total.  
  - Checkout page integrated with IntaSend (sandbox).  

---

## Technology Stack

- **Framework & Libraries**  
  - Python 3.x  
  - Flask 2.3.2  
  - Flask-Login 0.6.2  
  - Flask-SQLAlchemy 3.0.5  
  - Flask-WTF 1.1.1  
  - WTForms 3.0.1  
  - Jinja2 3.1.2  

- **Database**  
  - SQLite (development) / PostgreSQL or MySQL (production) via SQLAlchemy  

- **Payment Gateway**  
  - IntaSend (via `intasend-python 0.1.0`)  

- **HTTP Requests**  
  - `requests 2.31.0` for external APIs  

- **Internationalization**  
  - Python’s `gettext` / Flask-Babel (Nepali translation)  

- **Weather API**  
  - Any public endpoint (e.g., OpenWeatherMap—requires API key)  

- **Other Dependencies**  
  - blinker 1.6.2  
  - certifi 2023.7.22  
  - charset-normalizer 3.2.0  
  - click 8.1.4  
  - colorama 0.4.6  
  - greenlet 2.0.2  
  - idna 3.4  
  - importlib-metadata 6.7.0  
  - itsdangerous 2.1.2  
  - MarkupSafe 2.1.3  
  - SQLAlchemy 2.0.18  
  - typing_extensions 4.7.1  
  - urllib3 2.0.4  
  - Werkzeug 2.3.6  
  - zipp 3.15.0  

All dependencies are listed in `requirements.txt`.

---

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ganesh-786/Ganesh-Ecommerce_Web
   cd agricart

2. **Virtual Environment**
   ```bash
     python3 -m venv venv
    source venv/bin/activate         # On Windows: venv\Scripts\activate
3. **Installing Dependencies**
   ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
   
## Running the application
  ```bash
    flask run
---

## Folder Struture
├── agricart/
│   ├── __init__.py
│   ├── models.py
│   ├── forms.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── main.py
│   │   ├── products.py
│   │   ├── cart.py
│   │   └── weather.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── weather.html
│   │   ├── techniques.html
│   │   └── translations/
│   │       ├── nepali/
│   │       │   └── *.po / *.mo
│   │       └── english/
│   │           └── *.po / *.mo
│   ├── translations/           # Flask-Babel translation files (if used)
│   ├── seed_data.py
│   ├── run.py                  # Entry point
│   ├── config.py
│   └── requirements.txt
└── README.md


## Licence
This project is licensed under the name of Ganesh Chaudhary. Please, Don't copy the code.
