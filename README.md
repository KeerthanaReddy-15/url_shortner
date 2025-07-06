# 🔗 Flask URL Shortener

This is a simple Flask-based web application that allows users to generate short links from long URLs. It uses SQLite to store the original and shortened URLs and supports redirection to the original address.

---

## 🚀 Live Demo

👉 [Click here to try it](https://url-shortener-keerthana.onrender.com)

---

## 📸 Screenshot

![Screenshot](screenshot.png)

---

## 🛠 Tech Stack

- 🐍 Python 3
- 🔥 Flask (Web Framework)
- 🧱 SQLite (Database)
- 📄 Jinja2 (HTML Templates)
- 🌐 Render (Deployment)
- 🗂 Git + GitHub (Version Control)

---

## 🧪 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/KeerthanaReddy-15/url_shortner.git
cd url_shortner

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows

# 3. Install dependencies
pip install flask flask_sqlalchemy

# 4. Run the app
python app.py