# LittleLemon Restaurant API

Welcome to the LittleLemon Restaurant API! This API provides endpoints for managing restaurant bookings, menu items, and user authentication. Below you'll find all the details you need to get started.

## Features

### Bookings
- **GET /restaurant/bookings/tables/**: Retrieve all bookings. (Requires authentication)
- **POST /restaurant/bookings/tables/**: Create a new booking. (Requires authentication)
- **GET /restaurant/bookings/tables/{id}/**: Retrieve a single booking by ID.
- **PUT /restaurant/bookings/tables/{id}/**: Update a booking by ID.
- **PATCH /restaurant/bookings/tables/{id}/**: Partially update a booking by ID.
- **DELETE /restaurant/bookings/tables/{id}/**: Delete a booking by ID.

### Menu
- **GET /restaurant/menu/**: Retrieve all menu items.
- **POST /restaurant/menu/**: Create a new menu item.
- **GET /restaurant/menu/{id}/**: Retrieve a single menu item by ID.
- **PUT /restaurant/menu/{id}/**: Update a menu item by ID.
- **PATCH /restaurant/menu/{id}/**: Partially update a menu item by ID.
- **DELETE /restaurant/menu/{id}/**: Delete a menu item by ID.

### Authentication
- **POST /api-token-auth/**: Login with username and password to get a token.
- **GET /auth/users/**: Retrieve all users.
- **POST /auth/users/**: Create a new user.
- **POST /auth/token/login/**: Login with username and password to get a token.

## Setup

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- MySQL

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/HeidariAshkan/LittleLemon.git
    cd LittleLemon
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    - Ensure MySQL is running.
    - Create a database and a database user.
    - Update `settings.py` with your database credentials:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'your_database_name',
              'USER': 'your_database_user',
              'PASSWORD': 'your_database_password',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
      ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **Bookings**
  - **GET /restaurant/bookings/tables/**: Retrieve all bookings (requires authentication).
  - **POST /restaurant/bookings/tables/**: Create a new booking (requires authentication).
  - **GET /restaurant/bookings/tables/{id}/**: Retrieve a single booking by ID.
  - **PUT /restaurant/bookings/tables/{id}/**: Update a booking by ID.
  - **PATCH /restaurant/bookings/tables/{id}/**: Partially update a booking by ID.
  - **DELETE /restaurant/bookings/tables/{id}/**: Delete a booking by ID.

- **Menu**
  - **GET /restaurant/menu/**: Retrieve all menu items.
  - **POST /restaurant/menu/**: Create a new menu item.
  - **GET /restaurant/menu/{id}/**: Retrieve a single menu item by ID.
  - **PUT /restaurant/menu/{id}/**: Update a menu item by ID.
  - **PATCH /restaurant/menu/{id}/**: Partially update a menu item by ID.
  - **DELETE /restaurant/menu/{id}/**: Delete a menu item by ID.

- **Authentication**
  - **POST /api-token-auth/**: Login with username and password to get a token.
  - **GET /auth/users/**: Retrieve all users.
  - **POST /auth/users/**: Create a new user.
  - **POST /auth/token/login/**: Login with username and password to get a token.
