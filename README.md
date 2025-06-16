# 🍕 Pizza Restaurant API

A RESTful API for a pizza restaurant built with Flask and SQLAlchemy following MVC pattern.

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- pipenv (recommended) or pip
- PostgreSQL (or SQLite for development)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tresoraban/pizza-restaurant-api.git
   cd pizza-restaurant-api

2. Install dependencies:
```bash
pipenv install
pipenv shell
```
3. Set up database:
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
4. Seed the database:
```bash
python server/seed.py
```
5. Run the server:
```bash
flask run
```
6. **Start the server:**
```bash
export FLASK_APP=server/app.py
pipenv run flask run
```
The server will start at http://localhost:5000

> **Troubleshooting:**
> - If you see `Error: Could not locate a Flask application`, make sure you have run `export FLASK_APP=server/app.py` in your terminal **before** running `pipenv run flask run`.
> - If you visit `http://localhost:5000/` and see "Not Found", this is normal. Use the API endpoints like `/restaurants` or `/pizzas` as described below.

## 📚 API Routes

### Restaurants

#### GET /restaurants
Returns a list of all restaurants.

Response:
```json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  }
]
```

#### GET /restaurants/<int:id>
Returns details of a single restaurant and its pizzas.

Response:
```json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Mozzarella"
    }
  ]
}
```

Error Response (404):
```json
{
  "error": "Restaurant not found"
}
```

#### DELETE /restaurants/<int:id>
Deletes a restaurant and all related RestaurantPizzas.

Success: 204 No Content
Error (404):
```json
{
  "error": "Restaurant not found"
}
```

### Pizzas

#### GET /pizzas
Returns a list of all pizzas.

Response:
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella"
  }
]
```

### Restaurant Pizzas

#### POST /restaurant_pizzas
Creates a new RestaurantPizza association.

Request:
```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

Success Response:
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella"
  },
  "restaurant": {
    "id": 3,
    "name": "Pizza Place",
    "address": "456 Oak St"
  }
}
```

Error Response (400):
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## 🔍 Validation Rules

- RestaurantPizza price must be between 1 and 30
- All required fields must be present in requests
- Restaurant and Pizza IDs must exist in the database

## 🧪 Testing with Postman

1. Open Postman
2. Click Import → Upload `challenge-1-pizzas.postman_collection.json`
3. Test each route using the provided collection

## 📁 Project Structure

```
.
├── server/
│   ├── __init__.py
│   ├── app.py                # App setup
│   ├── config.py             # DB config
│   ├── models/               # Models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/          # Route handlers
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py              # Seed data
├── migrations/
└── README.md
``` 