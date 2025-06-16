from server import create_app
from server.models import db, Restaurant, Pizza, RestaurantPizza

def seed_database():
    app = create_app()
    
    with app.app_context():
        print("🔥 Dropping and recreating all tables...")
        db.drop_all()
        db.create_all()

        print("🍕 Creating restaurants...")
        restaurants = [
            Restaurant(
                name="Tony's Famous Pizza", 
                address="123 Main St, New York, NY"
            ),
            Restaurant(
                name="Mama Mia Pizzeria", 
                address="456 Oak Ave, Brooklyn, NY"
            ),
            Restaurant(
                name="Chicago Deep Dish", 
                address="789 Windy City Lane, Chicago, IL"
            ),
            Restaurant(
                name="California Pizza Kitchen", 
                address="101 Sunny Blvd, Los Angeles, CA"
            ),
            Restaurant(
                name="Neapolitan Express", 
                address="202 Napoli Way, Boston, MA"
            )
        ]
        db.session.add_all(restaurants)

        print("🧀 Creating pizzas...")
        pizzas = [
            Pizza(
                name="Margherita",
                ingredients="San Marzano tomatoes, Mozzarella di Bufala, Fresh basil, Extra virgin olive oil"
            ),
            Pizza(
                name="Pepperoni",
                ingredients="Tomato sauce, Mozzarella, Pepperoni"
            ),
            Pizza(
                name="Quattro Formaggi",
                ingredients="Tomato sauce, Mozzarella, Gorgonzola, Parmigiano-Reggiano, Fontina"
            ),
            Pizza(
                name="Vegetarian",
                ingredients="Tomato sauce, Mozzarella, Bell peppers, Mushrooms, Red onions, Black olives"
            ),
            Pizza(
                name="Hawaiian",
                ingredients="Tomato sauce, Mozzarella, Ham, Pineapple"
            ),
            Pizza(
                name="Diavola",
                ingredients="Tomato sauce, Mozzarella, Spicy salami, Chili flakes"
            ),
            Pizza(
                name="Truffle Mushroom",
                ingredients="White sauce, Mozzarella, Mushrooms, Truffle oil, Arugula"
            )
        ]
        db.session.add_all(pizzas)

        db.session.commit()

        print("🔗 Creating restaurant pizza associations...")
        restaurant_pizzas = [
            # Tony's Famous Pizza
            RestaurantPizza(price=12, pizza_id=1, restaurant_id=1),
            RestaurantPizza(price=14, pizza_id=2, restaurant_id=1),
            RestaurantPizza(price=16, pizza_id=3, restaurant_id=1),
            
            # Mama Mia Pizzeria
            RestaurantPizza(price=11, pizza_id=1, restaurant_id=2),
            RestaurantPizza(price=13, pizza_id=4, restaurant_id=2),
            RestaurantPizza(price=15, pizza_id=6, restaurant_id=2),
            
            # Chicago Deep Dish
            RestaurantPizza(price=18, pizza_id=5, restaurant_id=3),
            RestaurantPizza(price=20, pizza_id=7, restaurant_id=3),
            
            # California Pizza Kitchen
            RestaurantPizza(price=14, pizza_id=4, restaurant_id=4),
            RestaurantPizza(price=16, pizza_id=7, restaurant_id=4),
            
            # Neapolitan Express
            RestaurantPizza(price=13, pizza_id=1, restaurant_id=5),
            RestaurantPizza(price=15, pizza_id=3, restaurant_id=5),
            RestaurantPizza(price=14, pizza_id=6, restaurant_id=5)
        ]
        db.session.add_all(restaurant_pizzas)
        
        db.session.commit()
        print("✅ Database seeded successfully with:")
        print(f"   - {len(restaurants)} restaurants")
        print(f"   - {len(pizzas)} pizza types")
        print(f"   - {len(restaurant_pizzas)} restaurant-pizza associations")

if __name__ == '__main__':
    seed_database()