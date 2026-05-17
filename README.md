# Flask E-Commerce API

RESTful e-commerce backend built with Flask, PostgreSQL, JWT authentication, and Marshmallow validation.

## Features

- JWT authentication (register / login)
- User roles (admin for product & category management)
- Products & categories CRUD
- Shopping cart with stock checks
- Checkout with order history
- Consistent JSON responses
- CORS enabled for frontend integration
- Automated tests with pytest

## Tech Stack

- Python 3.11+
- Flask 3
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Marshmallow
- PostgreSQL
- pytest

## Project Structure

```text
ecommerc_api/
├── app/
│   ├── users/
│   ├── products/
│   ├── categories/
│   ├── cart/
│   ├── orders/
│   ├── config.py
│   ├── extensions.py
│   ├── utils.py
│   └── __init__.py
├── tests/
├── run.py
├── requirements.txt
└── .env.example
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/aifpro123-cloud/flask-ecommerc-API.git
cd flask-ecommerc-API
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/ecommerce_db
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
DEBUG=True
```

### 5. Database note (existing projects)

If you previously used the old cart table name `card_items`, drop it or reset your database before running again. The correct table name is now `cart_items`.

### 6. Create an admin user

Register a user via API, then set `is_admin = true` in the database for that user (or use your DB client).

### 7. Run the application

```bash
python run.py
```

API runs at `http://127.0.0.1:5000`

### 8. Run tests

```bash
pytest -v
```

## Authentication

Protected routes require:

```http
Authorization: Bearer <your_token>
```

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/register` | No | Register user |
| POST | `/login` | No | Login user |
| GET | `/category` | No | List categories |
| POST | `/category` | Admin | Create category |
| GET | `/product` | No | List products |
| GET | `/product/<id>` | No | Get product |
| POST | `/product` | Admin | Create product |
| PUT | `/product/<id>` | Admin | Update product (partial) |
| DELETE | `/product/<id>` | Admin | Delete product |
| GET | `/cart` | User | Get cart |
| POST | `/cart` | User | Add to cart |
| DELETE | `/cart/<item_id>` | User | Remove cart item |
| POST | `/checkout` | User | Checkout |
| GET | `/orders` | User | List user orders |

## Example Responses

**Success**

```json
{
  "success": true,
  "data": {}
}
```

**Validation error**

```json
{
  "success": false,
  "errors": {
    "email": ["Not a valid email address."]
  }
}
```

## Author

**Saif Elsayed**

## License

MIT
