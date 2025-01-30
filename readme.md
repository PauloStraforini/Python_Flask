# E-Commerce API with Flask
This project is a simple e-commerce API built using Flask, SQLAlchemy, and Flask-Login. It was developed by a student as part of a learning exercise to understand web development with Python and Flask. The API allows users to manage products, handle user authentication, and manage a shopping cart.

## Features
User Authentication: Users can log in and log out. Authentication is managed using Flask-Login.

-Product Management:

-Add new products.

-Update existing products.

-Delete products.

-Retrieve product details.

-Shopping Cart:

-Add products to the cart.

-Remove products from the cart.

-View the cart.

-Checkout (clears the cart).

## Technologies Used
Flask: A lightweight web framework for Python.

-SQLAlchemy: An ORM (Object-Relational Mapping) tool for database interactions.

-Flask-Login: Handles user authentication and session management.

-Flask-CORS: Enables Cross-Origin Resource Sharing (CORS) for the API.

## Database Models
-User: Stores user information including username and password.

-Product: Stores product information including name, price, and description.

-CartItem: Represents items in a user's shopping cart, linking users to products.

## API Endpoints
Authentication

POST /login: Logs in a user.

POST /logout: Logs out the current user.

Product Management
POST /api/products/add: Adds a new product (requires authentication).

DELETE /api/products/delete/int:product_id: Deletes a product by ID.

GET /api/products/int:product_id: Retrieves details of a specific product.

PUT /api/products/update/int:product_id: Updates a product's details.

GET /api/products: Retrieves a list of all products.

Shopping Cart
POST /api/cart/add/int:product_id: Adds a product to the cart (requires authentication).

DELETE /api/cart/remove/int:product_id: Removes a product from the cart (requires authentication).

GET /api/cart: Retrieves the current user's cart (requires authentication).

POST /api/cart/checkout: Clears the cart after checkout (requires authentication).

# Setup and Installation
Clone the repository:

bash
Copy
git clone https://github.com/PauloStraforini/ecommerce-flask-api
cd ecommerce-flask-api
Install dependencies:

bash
Copy
pip install -r requirements.txt
Initialize the database:

bash
Copy
python
>>> from app import db
>>> db.create_all()
Run the application:

bash
Copy
python app.py
Access the API:
The API will be running at http://127.0.0.1:5000/.

Usage
Use tools like Postman or cURL to interact with the API.

Ensure you log in first to access protected endpoints. 