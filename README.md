# 📊 Task Flow - Dynamic CRUD Application

A lightweight, robust Task Management web application built with **Python** and **Django**. This project demonstrates core backend engineering concepts, including dynamic routing, server-side data processing, state persistence, and full CRUD (Create, Read, Update, Delete) operations.

---

## 🚀 Key Features

* **Dynamic Progress Metrics:** Server-side calculation of remaining tasks, completed tasks, and real-time progress percentages using optimized Python logical loops.
* **State Persistence (Toggle Feature):** Interactive checkbox element that asynchronously flips task completion status (`True` / `False`) and updates the SQLite database seamlessly.
* **Safe Database Interaction:** Implements defensive programming principles using Django's `get_object_or_404` shortcut to handle object retrieval and prevent server crashes.
* **Complete CRUD Capabilities:** Standardized workflow for adding, rendering, toggling, and permanently destroying data entries safely.

---

## 🛠️ Tech Stack & Architecture

* **Backend:** Python 3.x / Django MVC Architecture (Models, Views, Templates)
* **Database:** SQLite (Development environment default)
* **Frontend:** Semantic HTML5, CSS3, JavaScript (Form auto-submission triggers)

---

## 🧩 Key Architecture Highlights (What I Learned)

### 1. Dynamic Routing & Context Control
The application uses pattern matching (`<int:task_id>/`) to capture primary keys directly from the HTTP request path, mapping them onto specific view functions:

path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task')
path('delete/<int:task_id>/', views.delete_task, name='delete_task')