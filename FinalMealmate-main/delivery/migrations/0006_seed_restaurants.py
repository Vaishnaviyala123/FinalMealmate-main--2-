from django.db import migrations


RESTAURANTS = [
    {
        "name": "Spice Route",
        "picture": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=900&q=80",
        "cuisine": "North Indian",
        "rating": 4.5,
    },
    {
        "name": "Sushi House",
        "picture": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=900&q=80",
        "cuisine": "Japanese",
        "rating": 4.7,
    },
    {
        "name": "Green Bowl",
        "picture": "https://images.unsplash.com/photo-1512621776951-a57141f2effd?w=900&q=80",
        "cuisine": "Healthy and Salads",
        "rating": 4.2,
    },
    {
        "name": "Bella Pasta",
        "picture": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=900&q=80",
        "cuisine": "Italian",
        "rating": 4.4,
    },
    {
        "name": "Taco Fiesta",
        "picture": "https://images.unsplash.com/photo-1552332386-f8dd00dc2f85?w=900&q=80",
        "cuisine": "Mexican",
        "rating": 4.1,
    },
]


def add_sample_restaurants(apps, schema_editor):
    Restaurant = apps.get_model("delivery", "Restaurant")
    for restaurant in RESTAURANTS:
        Restaurant.objects.get_or_create(
            name=restaurant["name"],
            defaults=restaurant,
        )


def remove_sample_restaurants(apps, schema_editor):
    Restaurant = apps.get_model("delivery", "Restaurant")
    Restaurant.objects.filter(name__in=[restaurant["name"] for restaurant in RESTAURANTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("delivery", "0005_cart"),
    ]

    operations = [
        migrations.RunPython(add_sample_restaurants, remove_sample_restaurants),
    ]
