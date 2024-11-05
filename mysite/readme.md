# 📄 WebScraper

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-3.x-green.svg)](https://www.djangoproject.com/)

WebScraper is a Django-powered web application that lets users scrape web page elements like links, images, headers, and paragraphs with ease. Choose specific elements or scrape everything at once, and export the results to Excel or CSV.

---

## 🚀 Features

- 🌐 **Flexible Web Scraping**: Scrape links, images, headers (H1, H2), and paragraphs from any webpage.
- 🛠️ **Element-Specific Selection**: Choose which elements to scrape or scrape all elements at once.
- 📊 **Export Options**: Download scraped data as an Excel or CSV file.
- 🧹 **Data Management**: Easily clear scraped data from the database.
- 🎨 **Responsive Design**: Built with Bootstrap 4 for a smooth, responsive experience.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sankalpkumar111/webscraper.git
cd webscraper
```

### 2. Install Dependencies

Make sure you have Python and pip installed. Then install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

Run the following commands to initialize the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Start the Server

Run the Django server:

```bash
python manage.py runserver
```

Access the app at `http://127.0.0.1:8000`.

---

## 📝 Usage Guide

1. **Input a URL**: Enter the website URL you want to scrape.
2. **Select Elements**: Choose from links, images, headers (H1, H2), paragraphs, or select "All" to scrape all.
3. **Scrape and View Data**: Click **Scrape** to extract and view the data in a table format.
4. **Export Data**: Use the **Export to Excel** or **Export to CSV** button to download the data.
5. **Clear Data**: Click **Clear All** to delete all scraped data from the database.

---

## 📂 Exporting Data

### Export Formats

- **Excel (.xlsx)**: Generates an Excel file (requires `XlsxWriter`).
- **CSV (.csv)**: Generates a CSV file.

### Export Instructions

1. Scrape the desired data.
2. Use the export buttons to download your data in the preferred format.

---

## 🛠️ Requirements

- **Python** 3.x
- **Django**
- **BeautifulSoup**
- **Requests**
- **XlsxWriter**

Install all required libraries:

```bash
pip install -r requirements.txt
```

---

## 🌍 Project Structure

```plaintext
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   └── result1.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
└── manage.py
```

---

## 📜 License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more details.

---

## 📬 Contact

**Sankalp Kumar**  
Email: [sankalpkumar911@gmail.com](mailto:sankalpkumar911@gmail.com)  

Follow me on [GitHub](https://github.com/sankalpkumar111), [LinkedIn](https://www.linkedin.com/in/sankalp-kumar-986b12218/), and [Instagram](https://www.instagram.com/sankalp._kr/).

---

## ⭐ Acknowledgements

Thanks to [Django](https://www.djangoproject.com/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for powering this project. Enjoy scraping responsibly!
```
