# 🛋️ Furniture Shop Project

**Furniture Shop Project** is a Django-based online furniture store, built with Django and Django REST Framework.  
It provides full functionality for browsing products, managing a shopping cart, user registration, and order management.

## 📋 Project Objective
Create an online furniture store with Django and Django REST Framework, including:
- Product catalog
- User registration and authentication
- Shopping cart management
- Order management

  ## 🚀 Features
- Product catalog with categories
- User registration and authentication (CustomUser)
- Shopping cart management
- Order creation and management
- Admin panel fully configured for managing categories, products, users, carts, and orders
- REST API endpoints for all main models

## 🧰 Technologies Used
- Python 3.12
- Django 4.2.3
- Django REST Framework 3.x
## 📦 Models Overview

### Category
- Fields: `name`, `slug`, `description`, `image`, `is_active`, `created_at`  
- Required categories: Chair, Sofa, Table, Wardrobe, Bed, Cabinet/Nightstand, Shelf, Armchair, Outdoor Furniture  

### Product
- Fields: `name`, `slug`, `category`, `description`, `price`, `stock`, `is_available`, `featured`, `created_at`, `updated_at`  
- Attributes (choices): `color`, `material`  
- Multiple images allowed  

### CustomUser
- Fields: `first_name`, `last_name`, `phone`, `address`, `birth_date`  
- Method: `get_full_name()`  

### Cart & CartItem
- Cart linked OneToOne with CustomUser  
- CartItem links products to cart  
- Methods: `get_total_price()`, `get_total_items()`, `get_total_items_count()`  

### Order & OrderItem
- Order linked to CustomUser  
- Fields: `order_number`, `status`, `total_amount`, `shipping_address`, `phone`, `notes`, `created_at`, `updated_at`  
- OrderItem stores product price at the moment of order  
## 🌐 API Endpoints

### Categories
- `GET /api/categories/` – List all categories  
- `GET /api/categories/<id>/` – Retrieve a specific category  

### Products
- `GET /api/products/` – List all products  
- `GET /api/products/<id>/` – Retrieve a specific product  
- Filter by category, color, material  

### Users (CustomUser)
- `POST /api/register/` – Register a new user  
- `POST /api/login/` – User login  
- `GET /api/profile/` – Get authenticated user profile  

### Cart
- `GET /api/cart/` – View current user cart  
- `POST /api/cart/add/` – Add product to cart  
- `POST /api/cart/remove/` – Remove product from cart  

### Orders
- `GET /api/orders/` – List all orders (auth user)  
- `GET /api/orders/<id>/` – Retrieve a specific order  
- `POST /api/orders/create/` – Create a new order  


### 🧑‍💻 Author Miranda Kachlavashvili
