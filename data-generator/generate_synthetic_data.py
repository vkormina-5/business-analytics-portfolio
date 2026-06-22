import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Set seeds for reproducibility
np.random.seed(42)
random.seed(42)

# Create output folder
os.makedirs('data', exist_ok=True)

# ---- PRODUCTS ----
def generate_products():
    categories = {
        'Smartphones': 'Smartphone',
        'Laptops': 'Laptop',
        'Tablets': 'Tablet',
        'Headphones': 'Headphones',
        'TVs': 'TV',
        'Cameras': 'Camera'
    }
    brands = ['Samsung', 'Apple', 'Xiaomi', 'Huawei', 'Sony', 'LG', 'Asus', 'Lenovo']

    products = []
    for i in range(1, 201):
        cat_full, cat_single = random.choice(list(categories.items()))
        brand = random.choice(brands)
        cost = round(random.uniform(5000, 150000), 2)
        price = round(cost * random.uniform(1.15, 1.35), 2)

        products.append({
            'product_id': i,
            'product_name': f'{brand} {cat_single} {i}',
            'category': cat_full,
            'brand': brand,
            'cost_price': cost,
            'selling_price': price
        })

    pd.DataFrame(products).to_csv("data/products.csv", index=False, encoding="utf-8")
    print("✅ products.csv generated")

# ---- STORES ----
def generate_stores():
    cities = [
        'Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Kazan',
        'Nizhny Novgorod', 'Chelyabinsk', 'Samara', 'Omsk', 'Rostov-on-Don'
    ]

    stores = [{
        'store_id': i,
        'store_name': f'TechMarket{i}',
        'city': random.choice(cities),
        'area': random.randint(50, 300),
        'staff_count': random.randint(5, 20)
    } for i in range(1, 51)]

    pd.DataFrame(stores).to_csv("data/stores.csv", index=False, encoding="utf-8")
    print("✅ stores.csv generated")

# ---- SALES ----
def generate_sales():
    start, end = datetime(2023, 1, 1), datetime(2024, 12, 31)
    dates = pd.date_range(start, end)

    sales = []
    sale_id = 1

    for d in dates:
        for _ in range(random.randint(50, 200)):
            sales.append({
                'sale_id': sale_id,
                'sale_date': d.strftime('%Y-%m-%d'),
                'product_id': random.randint(1, 200),
                'store_id': random.randint(1, 50),
                'quantity': random.randint(1, 5 if d.month in (11, 12) else 3),
                'payment_method': random.choice(['Cash', 'Card', 'Online'])
            })
            sale_id += 1

    pd.DataFrame(sales).to_csv("data/sales.csv", index=False, encoding="utf-8")
    print("✅ sales.csv generated")

# ---- RUN ----
if __name__ == "__main__":
    generate_products()
    generate_stores()
    generate_sales()
    print("\n✅ All synthetic data generated successfully!")
