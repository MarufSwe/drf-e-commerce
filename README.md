# DRF E-Commerce Project

## Overview

This is an E-Commerce project built with Django and Django REST Framework, with PostgreSQL as the chosen database. It includes modules for user authentication, user profile product management, shopping cart functionality, purchases, product reviews, and more.


## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/MarufSwe/drf-e-commerce.git
   
   cd e_commerce

2. Set up a virtual environment (optional but recommended):
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Apply database migrations:

   ```bash
   python manage.py migrate


5. Create a superuser account:
   ```bash
   python manage.py createsuperuser


6. Run the development server:

   ```bash
   python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/admin/ to access the Django admin. Use the superuser credentials created in step 5.

Additionally, you can explore the API using Swagger by visiting [http://127.0.0.1:8000]


## Running with Docker
1. Install Docker and Docker Compose.
   
2. Build and run the Docker containers:
3. 
   ```bash
   docker-compose up --build



## Project Features

1. **Token-Based Authentication:**
   - Users must authenticate using tokens for secure access to the API.
   - Token generation during user login for authenticated sessions.

2. **User Login:**
   - Token generation during user login for authenticated sessions.

3. **User Registration:**
   - New users can register, including user profile information.

4. **Product Management:**
   - CRUD operations for products.
   - Register users can review products.

5. **Shopping Cart:**
   - Users can add/remove products to/from their shopping cart.
   - The shopping cart updates dynamically as items are added or removed.
   - Stock status is updated as purchases are made.

6. **Checkout Process:**
   - Seamless checkout process with shipping information and payment details.
   
7. **API Documentation:**
   - Swagger is integrated for clear API documentation for ease of understanding.
   - Explore the API interactively at [http://127.0.0.1:8000]

9. **Dockerization:**
   - Docker support for containerizing the application.

10. **Unit Testing:**
    - Comprehensive unit tests for the product module to ensure code reliability.



