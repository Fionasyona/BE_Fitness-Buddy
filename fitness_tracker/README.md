# Fitness Tracker API

A Django REST Framework (DRF) based API that allows users to **track fitness activities** such as exercises, sets, reps, and weights.  

---

## Features
- User authentication (via Django’s auth system)
- CRUD operations for fitness activities
- REST API endpoints using Django REST Framework
- PostgreSQL support for production (SQLite for local dev)
- Static file handling with Whitenoise

---

## Installation & Setup (Local)

fitness_tracker/
│── fitness_tracker/       # Main project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
│── static/                # Static assets (optional for frontend), yet to implement
│── staticfiles/           # Collected static files
│── manage.py
│── requirements.txt
│── Procfile
│── .env
│── README.md

| Method | Endpoint                | Description               |
| ------ | ----------------------- | ------------------------- |
| GET    | `/api/activities/`      | List all activities       |
| POST   | `/api/activities/`      | Create a new activity     |
| GET    | `/api/activities/<id>/` | Retrieve activity details |
| PUT    | `/api/activities/<id>/` | Update an activity        |
| DELETE | `/api/activities/<id>/` | Delete an activity        |
