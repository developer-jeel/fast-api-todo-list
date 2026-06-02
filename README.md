# 🚀 FastAPI Todo List App

A clean and modern Todo List application built using **FastAPI**, **SQLAlchemy**, **SQLite**, and **Jinja2 Templates**.

## ✨ Features

* ➕ Create new tasks
* 📋 View all tasks
* ✏️ Update existing tasks
* 🗑️ Delete tasks
* 💾 SQLite database integration
* 🎨 Beautiful custom UI
* ⚡ FastAPI powered backend
* 🔄 Full CRUD operations

## 🛠️ Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Jinja2
* HTML5
* CSS3
* Uvicorn

## 📁 Project Structure

```bash
project/
│
├── main.py
├── crud.py
├── database.py
├── models.py
│
├── templates/
│   ├── todo_list.html
│   ├── create_todo.html
│   └── update.html
│
└── todos.db
```

## 🗄️ Database Model

```python
id = Column(Integer, primary_key=True, index=True)
title = Column(String, index=True)
description = Column(String, nullable=False)
done = Column(Boolean, default=False)
```

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd project-folder
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
```

### 3️⃣ Activate Environment

**Windows**

```bash
env\Scripts\activate
```

**Linux / Mac**

```bash
source env/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

## ▶️ Run Project

```bash
uvicorn main:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000/todo/
```

## 🌐 Routes

| Method | Route               | Description      |
| ------ | ------------------- | ---------------- |
| GET    | `/todo/`            | View all todos   |
| GET    | `/todo/create`      | Open create page |
| POST   | `/todo/create`      | Add new todo     |
| GET    | `/todo/update/{id}` | Open update page |
| POST   | `/todo/update/{id}` | Update todo      |
| GET    | `/todo/delete/{id}` | Delete todo      |

## 📸 Screens

* 🏠 Todo Dashboard
* ➕ Create Todo Page
* ✏️ Update Todo Page

## 🔮 Future Improvements

* 🔍 Search Tasks
* 📄 Pagination
* 👤 User Authentication
* 🏷️ Task Categories
* 📅 Due Dates
* 🌙 Dark Mode
* 📡 REST API Support

## 👨‍💻 Author

**Jeel Tank**

Python Developer 🐍

## ⭐ Support

If you like this project, don't forget to give it a **Star ⭐** on GitHub.
