🍋 Little Lemon Restaurant Backend API

Coursera Meta Back-End Developer Capstone Project

## Project Overview

Little Lemon Restaurant Backend API is a Django REST Framework based backend application developed as part of the Coursera Meta Back-End Developer Capstone Project.

The application provides RESTful APIs for restaurant menu management, table booking management, user registration and authentication, and Django Admin management.

## API Paths for Peer Testing

### Authentication APIs

1. POST `/api-token-auth/`

   * Generate an authentication token using Django REST Framework Token Authentication.

   Request body:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

2. POST `/auth/token/login/`

   * Djoser token login.

3. GET `/auth/users/me/`

   * Get the currently authenticated user's details.

4. POST `/auth/token/logout/`

   * Logout from Djoser token authentication.

### Menu APIs

5. GET `/restaurant/menu/`

   * List all menu items.

6. POST `/restaurant/menu/`

   * Create a new menu item.
   * Manager authentication is required.

7. GET `/restaurant/menu/{id}/`

   * Retrieve a single menu item.

8. PUT `/restaurant/menu/{id}/`

   * Update a menu item.

9. PATCH `/restaurant/menu/{id}/`

   * Partially update a menu item.

10. DELETE `/restaurant/menu/{id}/`

    * Delete a menu item.

### Booking APIs

11. GET `/restaurant/booking/`

    * List all bookings.
    * Authentication is required.

12. POST `/restaurant/booking/`

    * Create a new booking.
    * Authentication is required.

13. GET `/restaurant/booking/{id}/`

    * Retrieve a single booking.

14. PUT `/restaurant/booking/{id}/`

    * Update a booking.

15. PATCH `/restaurant/booking/{id}/`

    * Partially update a booking.

16. DELETE `/restaurant/booking/{id}/`

    * Delete a booking.

### Static Web Page

GET `/restaurant/`

This route serves the Little Lemon `index.html` page using Django templates.

### Django Admin

GET `/admin/`

Django Admin is available for managing users, menu items, bookings and other administrative data.

## Local Base URL

```text
http://127.0.0.1:8000/
```

## API Testing

The APIs have been tested using Insomnia and Django Admin.

### Token Authentication

Send a POST request to:

```text
/api-token-auth/
```

with:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

The response returns an authentication token.

Use the returned token in the Authorization header when testing protected APIs:

```text
Authorization: Token your_token_here
```

### Tested Operations

* User authentication
* Token authentication
* User details
* User logout
* Menu GET
* Menu POST
* Menu PUT
* Menu PATCH
* Menu DELETE
* Booking GET
* Booking POST
* Booking PUT
* Booking PATCH
* Booking DELETE
* Django Admin operations
* Static `index.html` page

## Unit Testing

The project contains separate unit test files:

```text
restaurant/test_models.py
restaurant/test_views.py
```

Run all restaurant tests with:

```bash
python manage.py test restaurant
```

The current test suite passes successfully.

## Database

The project uses MySQL as the database backend.

Example database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/ranvirignou0516-dot/Little-Lemon--Meta-Back-End-Developer-Capstone-Project.git
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment on Windows

For Windows Command Prompt:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Tests

```bash
python manage.py test restaurant
```

### 8. Start Development Server

```bash
python manage.py runserver
```

## Project Structure

```text
Little-Lemon-Meta-Back-End-Developer-Capstone-Project/
│
├── littlelemon/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── restaurant/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── test_models.py
│   ├── test_views.py
│   └── ...
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── img/
│
├── screenshots/
│   ├── Authentication/
│   ├── Menu/
│   ├── Booking/
│   ├── Admin/
│   └── Terminal/
│
├── manage.py
├── requirements.txt
├── Readme.txt
└── README.md
```

## Static Web Application

The project uses Django templates to serve the Little Lemon static web page.

Template:

```text
templates/index.html
```

Static files:

```text
static/css/
static/img/
```

The web page can be accessed at:

```text
http://127.0.0.1:8000/restaurant/
```

## Repository

GitHub Repository:

https://github.com/ranvirignou0516-dot/Little-Lemon-Meta-Back-End-Developer-Capstone-Project.git

## Author

Ranvir Kumar

Coursera Meta Back-End Developer Capstone Project
