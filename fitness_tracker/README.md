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

## Endpoints

 ## User Endpoints
1.*Register User*
     *POST* /api/register/
     *Request Body*
      json
    {
        "username": "Angel",
        "email" : "angelwall@gmail.com",
        "password": "passA123word@"
    }
      
      *Response*
      json
      {
        "message": "User registered successfully"
      }

2.*User Profile*
     *GET* /api/profile/
     *Request body*
     json
     {
        "id": 1,
        "username": "Angel",
        "email" : "angelwall@gmail.com",
        "date_joined": "2025-08-28T14:07:27"
     }    

## Authentication Endpoints
1. Obtain Token
     *POST*/api/token/
     *Request body*
     json
     {
        "username": "Agnes",
        "password": "xM6NUXSsQmtM@rL"
     }

     *Response*
     json
     {
        "refresh": "refresh_token_here",
        "access": "access_token_here"
     }

2. Refresh Token
     *POST* /api/token/refresh/
     *Request body*
     json
     {
        "refresh": "refresh_token_here"
     }

      *Response*
     json
     {
        "access": "new_access_token_here"
     }

## Activity Endpoints
1. List & Create Activities
      *GET*/*POST*/api/activities/
      *POST*
      *Request body*
      json
      {
          "activity_type": "Squats",
          "duration_minutes": 45,
          "calories": 350,
          "date": "2025-08-28"
      }

       *POST*
       *Response*
       json
       {
          "activity_type": "Squats",
          "duration_minutes": 45,
          "calories": 350,
          "date": "2025-08-28"
       }
2. Retrieve,Update,Delete Activities
      *GET*/*PUT*/*DELETE*/api/activities/<id>/
      *GET*
      *Request*
      json
     
     {
         "id":1,
          "activity_type": "Squats",
          "duration_minutes": 45,
          "calories": 350,
          "date": "2025-08-28"
     }

3. Activity History with Filter
      *GET*/api/activities/history/?type=Squats&date=2025-08-28
      *GET*
      *Request*
       json
       [
      {
          "id":1,
          "activity_type": "Squats",
          "duration_minutes": 45,
          "calories": 350,
          "date": "2025-08-28"
      }
       ]
4. Activity Metric
       *GET*/api/activities/metrics/
       *Response*
        json
        {
           "total_activities": 10,
           "total_duration": 420,
           "total_calories": 3500
       }
     

