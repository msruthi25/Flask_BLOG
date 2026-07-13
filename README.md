# 📝 Flask Blog - Portfolio Project

A lightweight, feature-rich blogging web application built with **Flask**, **SQLAlchemy (SQLite)**, and styled with custom CSS. This project features user authentication (Signup/Login), blog post creation, category organization, and dynamic routing to showcase a clean Python-based web architecture.

---

## 🚀 Key Features

*   **User Authentication System:** Secure Signup and Login using SQLAlchemy ORM to manage user credentials.
*   **Dynamic Blogging Engine:** Create, read, and filter blog posts based on categories and custom titles.
*   **Database Management:** Powered by SQLite with structured schemas for Users, Posts, and Categories.
*   **Intuitive UI/UX:** Clean, responsive, and lightweight templates designed using standard HTML5 and custom CSS.
*   **Clean Architecture:** Separated concerns utilizing Flask blueprints-style modules (main app, routes, database models, and extensions).

---

## 🛠️ Tech Stack & Dependencies

*   **Backend Framework:** Flask 3.1.2
*   **Database ORM:** SQLAlchemy / Flask-SQLAlchemy
*   **Database Engine:** SQLite (Local instance)
*   **Frontend Technologies:** HTML5, CSS3, Jinja2 Templating
*   **Environment Configuration:** Python dotenv / safe environment variables

---

## 📁 Repository Structure

```text
Flask_Blog/
├── app/
│   ├── instance/           # SQLite Local Database (ignored by Git)
│   ├── static/             # Static Assets (CSS, JS, Images)
│   ├── templates/          # Jinja2 HTML Templates
│   ├── extensions.py       # Shared database/extensions initializer
│   ├── main.py             # Flask App Entrypoint & Configuration
│   ├── models.py           # Database Schemas (User, Posts, Category)
│   └── routes.py           # Route Handlers and Controller Logic
├── .gitignore              # Files to ignore in Git
├── README.md               # Project Documentation
└── requirements.txt        # Python Dependencies
```

---

## ⚙️ Quick Start & Installation

To run this application locally, follow these steps:

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Flask_Blog
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Configurations (Optional)
By default, the application runs with a default development fallback key. To configure custom environment configurations, set the `SECRET_KEY` env variable:
```bash
# Windows (PowerShell)
$env:SECRET_KEY="your-custom-secret-key"

# macOS/Linux
export SECRET_KEY="your-custom-secret-key"
```

### 5. Initialize the Database & Run the App
To start the Flask development server:
```bash
python app/main.py
```
Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 📊 Database Schema

The SQLite database consists of three primary tables managed by Flask-SQLAlchemy:

### 1. User
*   `id` (Integer, Primary Key)
*   `username` (Text, Nullable=False)
*   `password` (Text, Nullable=False)
*   `email` (Text, Nullable=False)

### 2. Posts
*   `id` (Integer, Primary Key, Auto-increment)
*   `title` (Text, Nullable=False)
*   `snippet` (Text)
*   `full_content` (Text)
*   `img_url` (Text)
*   `category_data` (Text)
*   `created_date` (Text)

### 3. Category
*   `id` (Integer, Primary Key)
*   `name` (Text, Nullable=False)
