# Flask Ecommerce API 🚀

A scalable Ecommerce REST API built with Flask using clean architecture and modern backend practices.

---

# ✨ Features

## Authentication & Security
- User Registration
- User Login
- JWT Authentication
- Protected Routes

## Products & Categories
- Categories CRUD
- Products CRUD
- Product Stock Management

## Cart System
- Add To Cart
- Get User Cart
- Remove From Cart

## Orders & Checkout
- Checkout System
- Orders Management
- Order Items
- Automatic Stock Reduction

## Validation
- Request Validation using Marshmallow

---

# 🛠 Technologies Used

- Python
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Marshmallow
- PostgreSQL
- SQLAlchemy ORM

---

# 📁 Project Structure

```text
app/
│
├── users/
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── products/
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── categories/
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── cart/
│   ├── models.py
│   ├── routes.py
│   └── schemas.py
│
├── orders/
│   ├── models.py
│   └── routes.py
│
├── extensions.py
├── config.py
└── __init__.py
