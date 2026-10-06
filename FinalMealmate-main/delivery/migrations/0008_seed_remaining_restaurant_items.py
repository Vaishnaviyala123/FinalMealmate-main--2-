from django.db import migrations


MENUS = {
    "Sushi House": [
        {
            "name": "Salmon Sushi",
            "description": "Fresh salmon served over seasoned sushi rice.",
            "price": 360,
            "vegeterian": False,
            "picture": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=900&q=80",
        },
        {
            "name": "Vegetable Sushi",
            "description": "Colorful rolls filled with cucumber, avocado, and carrot.",
            "price": 240,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1553621042-f6e147245754?w=900&q=80",
        },
        {
            "name": "Chicken Ramen",
            "description": "Warm ramen broth with noodles, chicken, and vegetables.",
            "price": 320,
            "vegeterian": False,
            "picture": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=900&q=80",
        },
        {
            "name": "Edamame",
            "description": "Steamed soybeans lightly seasoned with sea salt.",
            "price": 140,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1606755456206-b25206cde27e?w=900&q=80",
        },
    ],
    "Green Bowl": [
        {
            "name": "Quinoa Power Bowl",
            "description": "Quinoa, roasted vegetables, greens, and lemon dressing.",
            "price": 260,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1512621776951-a57141f2effd?w=900&q=80",
        },
        {
            "name": "Avocado Salad",
            "description": "Fresh avocado, tomato, cucumber, and mixed greens.",
            "price": 220,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=900&q=80",
        },
        {
            "name": "Grilled Chicken Bowl",
            "description": "Grilled chicken with brown rice, greens, and herbs.",
            "price": 310,
            "vegeterian": False,
            "picture": "https://images.unsplash.com/photo-1547592180-85f173990554?w=900&q=80",
        },
        {
            "name": "Fruit Smoothie",
            "description": "A refreshing blend of seasonal fruits and yogurt.",
            "price": 160,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1505252585461-04db1eb84625?w=900&q=80",
        },
    ],
    "Bella Pasta": [
        {
            "name": "Penne Arrabbiata",
            "description": "Penne pasta tossed in a spicy tomato and garlic sauce.",
            "price": 240,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=900&q=80",
        },
        {
            "name": "Margherita Pizza",
            "description": "Classic pizza with tomato, mozzarella, and fresh basil.",
            "price": 350,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=900&q=80",
        },
        {
            "name": "Chicken Alfredo",
            "description": "Creamy fettuccine pasta with grilled chicken.",
            "price": 390,
            "vegeterian": False,
            "picture": "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?w=900&q=80",
        },
        {
            "name": "Tiramisu",
            "description": "Classic Italian dessert layered with coffee mascarpone.",
            "price": 180,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=900&q=80",
        },
    ],
    "Taco Fiesta": [
        {
            "name": "Chicken Tacos",
            "description": "Soft tacos filled with seasoned chicken, salsa, and lime.",
            "price": 260,
            "vegeterian": False,
            "picture": "https://images.unsplash.com/photo-1552332386-f8dd00dc2f85?w=900&q=80",
        },
        {
            "name": "Veggie Burrito",
            "description": "A filling burrito with beans, rice, vegetables, and salsa.",
            "price": 230,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1626700051175-6818013e1d4f?w=900&q=80",
        },
        {
            "name": "Nachos Supreme",
            "description": "Crispy nachos topped with cheese, beans, salsa, and jalapeno.",
            "price": 210,
            "vegeterian": True,
            "picture": "https://images.unsplash.com/photo-1513456852971-30c0a8199d4d?w=900&q=80",
        },
        {
            "name": "Beef Quesadilla",
            "description": "Toasted tortilla filled with spiced beef and melted cheese.",
            "price": 290,
            "vegeterian": False,
            "picture": "https://images.unsplash.com/photo-1618040996337-56904b7850b9?w=900&q=80",
        },
    ],
}


def add_remaining_items(apps, schema_editor):
    Restaurant = apps.get_model("delivery", "Restaurant")
    Item = apps.get_model("delivery", "Item")

    for restaurant_name, items in MENUS.items():
        restaurant = Restaurant.objects.filter(name=restaurant_name).first()
        if restaurant is None:
            continue

        for item in items:
            Item.objects.get_or_create(
                restaurant=restaurant,
                name=item["name"],
                defaults=item,
            )


def remove_remaining_items(apps, schema_editor):
    Restaurant = apps.get_model("delivery", "Restaurant")
    Item = apps.get_model("delivery", "Item")

    for restaurant_name, items in MENUS.items():
        restaurant = Restaurant.objects.filter(name=restaurant_name).first()
        if restaurant is not None:
            Item.objects.filter(
                restaurant=restaurant,
                name__in=[item["name"] for item in items],
            ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("delivery", "0007_seed_spice_route_items"),
    ]

    operations = [
        migrations.RunPython(add_remaining_items, remove_remaining_items),
    ]
