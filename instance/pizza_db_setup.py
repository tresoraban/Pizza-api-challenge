# pizza_db_setup.py
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, SQLite version {sqlite3.version}")
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables(conn):
    """ Create all tables """
    sql_create_restaurants_table = """
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
    );
    """

    sql_create_pizzas_table = """
    CREATE TABLE IF NOT EXISTS pizzas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT NOT NULL
    );
    """

    sql_create_restaurant_pizzas_table = """
    CREATE TABLE IF NOT EXISTS restaurant_pizzas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        price INTEGER NOT NULL CHECK (price BETWEEN 1 AND 30),
        pizza_id INTEGER NOT NULL,
        restaurant_id INTEGER NOT NULL,
        FOREIGN KEY (pizza_id) REFERENCES pizzas (id),
        FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
    );
    """

    tables = [sql_create_restaurants_table, 
              sql_create_pizzas_table,
              sql_create_restaurant_pizzas_table]

    try:
        c = conn.cursor()
        for table in tables:
            c.execute(table)
        print("Tables created successfully")
    except Error as e:
        print(e)

def seed_data(conn):
    """ Seed initial data """
    restaurants = [
        ("Tony's Famous Pizza", "123 Main St, New York, NY"),
        ("Mama Mia Pizzeria", "456 Oak Ave, Brooklyn, NY"),
        ("Chicago Deep Dish", "789 Windy City Lane, Chicago, IL")
    ]

    pizzas = [
        ("Margherita", "San Marzano tomatoes, Mozzarella, Basil"),
        ("Pepperoni", "Tomato sauce, Mozzarella, Pepperoni"),
        ("Vegetarian", "Tomato sauce, Mozzarella, Vegetables")
    ]

    restaurant_pizzas = [
        (12, 1, 1),  # Tony's Margherita
        (14, 2, 1),  # Tony's Pepperoni
        (11, 1, 2),  # Mama Mia Margherita
        (13, 3, 2),  # Mama Mia Vegetarian
        (15, 2, 3)   # Chicago Pepperoni
    ]

    try:
        c = conn.cursor()
        
        # Insert restaurants
        c.executemany("INSERT INTO restaurants (name, address) VALUES (?, ?)", restaurants)
        
        # Insert pizzas
        c.executemany("INSERT INTO pizzas (name, ingredients) VALUES (?, ?)", pizzas)
        
        # Insert restaurant_pizzas
        c.executemany("""
            INSERT INTO restaurant_pizzas (price, pizza_id, restaurant_id) 
            VALUES (?, ?, ?)
        """, restaurant_pizzas)
        
        conn.commit()
        print("Data seeded successfully")
    except Error as e:
        print(e)

def main():
    database = "pizza.db"
    
    # Create database connection
    conn = create_connection(database)
    
    if conn is not None:
        # Create tables
        create_tables(conn)
        
        # Seed data
        seed_data(conn)
        
        # Verify data
        print("\nSample data verification:")
        c = conn.cursor()
        c.execute("SELECT name FROM restaurants")
        print(f"Restaurants: {[row[0] for row in c.fetchall()]}")
        
        c.execute("SELECT name FROM pizzas")
        print(f"Pizzas: {[row[0] for row in c.fetchall()]}")
        
        c.execute("""
            SELECT r.name, p.name, rp.price 
            FROM restaurant_pizzas rp
            JOIN restaurants r ON rp.restaurant_id = r.id
            JOIN pizzas p ON rp.pizza_id = p.id
        """)
        print("Restaurant Pizzas:")
        for row in c.fetchall():
            print(f"- {row[0]} serves {row[1]} for ${row[2]}")
        
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()