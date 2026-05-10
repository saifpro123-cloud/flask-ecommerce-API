# 🛒 Flask E-Commerce API

A clean and scalable RESTful API built with Flask for managing a full e-commerce system.  
This project includes authentication, products, categories, cart management, and checkout functionality.

---

## ✨ Features

- 🔒 JWT Authentication
- 👤 User Registration & Login
- 📦 Product Management
- 📁 Category Management
- 🛒 Shopping Cart System
- 🧾 Checkout System
- ✅ Data Validation using Marshmallow
- 🔑 Password Hashing
- 🏗️ Modular Flask Architecture (Blueprints)
- ⚡ RESTful API Design

---

## 🧰 Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Marshmallow
- PostgreSQL
- Git & GitHub

---

## 📁 Project Structure

```bash
app/
├── users/
│   ├── models.py
│   ├── routes.py
│   └── schema.py
├── products/
│   ├── models.py
│   ├── routes.py
│   └── schema.py
├── categories/
│   ├── models.py
│   ├── routes.py
│   └── schema.py
├── cart/
│   ├── models.py
│   ├── routes.py
│   └── schema.py
├── orders/
│   ├── models.py
│   ├── routes.py
│   └── schema.py
├── config.py
├── extensions.py
└── __init__.py
```

---

## ⚡ Installation

### 1. Clone The Repository

```bash
git clone https://github.com/saifpro123-cloud/flask-ecommerce-API.git
cd flask-ecommerce-API
```

### 2. Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
DEBUG=True
JWT_SECRET_KEY=your_jwt_secret
```

### 5. Run The Application

```bash
python app.py
```

---

## 🔐 Authentication

Protected routes require a JWT token in the header:

```http
Authorization: Bearer <your_token>
```

---

## 🚀 API Endpoints

### 👤 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Login user |

---

### 📦 Products

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/product` | Get all products |
| GET | `/product/<int:product_id>` | Get single product |
| POST | `/product` | Create product |
| PUT | `/product/<int:product_id>` | Update product |
| DELETE | `/product/<int:product_id>` | Delete product |

---

### 📁 Categories

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/category` | Get all categories |
| POST | `/category` | Create category |

---

### 🛒 Cart

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/cart` | Get cart items |
| POST | `/cart` | Add item to cart |
| DELETE | `/cart/<int:item_id>` | Remove item from cart |

---

### 🧾 Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/checkout` | Checkout order |
| GET | `/orders` | Get user orders |

---

## 📋 Example Requests

### Register

```json
{
  "name": "Saif",
  "email": "saif@example.com",
  "password": "123456"
}
```

### Login

```json
{
  "email": "saif@example.com",
  "password": "123456"
}
```

### Create Product

```json
{
  "name": "iPhone 15",
  "price": 1200,
  "stock": 5,
  "category_id": 1
}
```

### Add To Cart

```json
{
  "product_id": 1,
  "quantity": 2
}
```

---

## ✅ Example Response

```json
{
  "success": true,
  "message": "Operation completed successfully"
}
```

---

## 🔥 Key Highlights

- Clean modular structure
- RESTful API architecture
- Secure authentication system
- Validation using Marshmallow
- SQLAlchemy ORM integration
- Scalable backend design

---

## 🚀 Future Improvements

- Pagination for products
- Product filtering & search
- Swagger API documentation
- Docker support
- Unit testing
- Payment gateway integration
- Refresh tokens

---

## 👨‍💻 Author

**Saif Elsayed**  
GitHub: [https://github.com/saifpro123-cloud](https://github.com/saifpro123-cloud)

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
