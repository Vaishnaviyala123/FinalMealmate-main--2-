from django.db import migrations


ITEMS = [
    {
        "name": "Butter Chicken",
        "description": "Tender chicken in a creamy tomato and butter gravy.",
        "price": 320,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?w=900&q=80",
    },
    {
        "name": "Paneer Tikka",
        "description": "Chargrilled paneer with peppers and Indian spices.",
        "price": 240,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?w=900&q=80",
    },
    {
        "name": "Biryani",
        "description": "Fragrant basmati rice layered with aromatic spices.",
        "price": 280,
        "vegeterian": False,
        "picture": "https://images.unsplash.com/photo-1589302168068-964664d93dc0?w=900&q=80",
    },
    {
        "name": "Garlic Naan",
        "description": "Soft tandoor-baked naan finished with garlic and herbs.",
        "price": 80,
        "vegeterian": True,
        "picture": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=900&q=80",
    },
]


def add_spice_route_items(apps, schema_editor):
    Restaurant = apps.get_model("delivery", "Restaurant")
    Item = apps.get_model("delivery", "Item")
    restaurant = Restaurant.objects.filter(name="Spice Route").first()

    if restaurant is None:
        return

    for item in ITEMS:
        Item.objects.get_or_create(
            restaurant=restaurant,
            name=item["name"],
            defaults=item,
        )


def remove_spice_route_items(apps, schema_editor):
    Restaurant = apps.get_model("delivery", "Restaurant")
    Item = apps.get_model("delivery", "Item")
    restaurant = Restaurant.objects.filter(name="Spice Route").first()

    if restaurant is not None:
        Item.objects.filter(
            restaurant=restaurant,
            name__in=[item["name"] for item in ITEMS],
        ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("delivery", "0006_seed_restaurants"),
    ]

    operations = [
        migrations.RunPython(add_spice_route_items, remove_spice_route_items),
    ]
