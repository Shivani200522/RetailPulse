from pathlib import Path
import pandas as pd
import random

# -----------------------------
# Create data/sample folder
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data" / "sample"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Customers
# -----------------------------

first_names = [
    "Rahul", "Priya", "Arjun", "Sneha", "Rohit",
    "Ananya", "Vikram", "Neha", "Kiran", "Aisha"
]

last_names = [
    "Sharma", "Reddy", "Patel", "Verma", "Nair",
    "Singh", "Iyer", "Joshi", "Gupta", "Kumar"
]

cities = [
    ("Bangalore", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Mumbai", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Chennai", "Tamil Nadu"),
    ("Pune", "Maharashtra")
]

segments = ["New", "Regular", "Premium"]

customers = []

occupations = [
    "Student",
    "Software Engineer",
    "Teacher",
    "Doctor",
    "Business Owner",
    "Government Employee",
    "Homemaker",
    "Sales Executive"
]

genders = ["Male", "Female"]

marital_status = ["Single", "Married"]

preferred_categories = [
    "Electronics",
    "Fashion",
    "Groceries",
    "Skincare",
    "Home Appliances",
    "Fitness"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash On Delivery"
]

for i in range(1, 1001):

    city, state = random.choice(cities)

    age = random.randint(18, 60)

    if age <= 23:
        occupation = "Student"
        income = random.randint(10000, 35000)

    elif age <= 35:
        occupation = random.choice([
            "Software Engineer",
            "Sales Executive",
            "Teacher"
        ])
        income = random.randint(30000, 120000)

    elif age <= 50:
        occupation = random.choice([
            "Business Owner",
            "Doctor",
            "Government Employee"
        ])
        income = random.randint(50000, 250000)

    else:
        occupation = random.choice([
            "Business Owner",
            "Homemaker"
        ])
        income = random.randint(25000, 150000)

    customers.append({

        "customer_id": f"CUS{i:04}",

        "first_name": random.choice(first_names),

        "last_name": random.choice(last_names),

        "gender": random.choice(genders),

        "age": age,

        "occupation": occupation,

        "monthly_income": income,

        "marital_status": random.choice(marital_status),

        "city": city,

        "state": state,

        "segment": random.choices(
            segments,
            weights=[20, 55, 25]
        )[0],

        "preferred_category": random.choice(
            preferred_categories
        ),

        "preferred_payment": random.choice(
            payment_methods
        ),

        "loyalty_score": random.randint(1, 100)
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# Products
# -----------------------------

MASTER_DATA_DIR = BASE_DIR / "master_data"

products_df = pd.read_csv(
    MASTER_DATA_DIR / "products.csv"
)

# -----------------------------
# Stores
# -----------------------------

stores = [

("STR001","Bangalore","Karnataka","South"),
("STR002","Hyderabad","Telangana","South"),
("STR003","Mumbai","Maharashtra","West"),
("STR004","Delhi","Delhi","North"),
("STR005","Chennai","Tamil Nadu","South"),
("STR006","Pune","Maharashtra","West")

]

stores_df = pd.DataFrame(
    stores,
    columns=[
        "store_id",
        "city",
        "state",
        "region"
    ]
)

# -----------------------------
# Save CSVs
# -----------------------------

customers_df.to_csv(DATA_DIR / "customers.csv", index=False)

products_df.to_csv(DATA_DIR / "products.csv", index=False)

stores_df.to_csv(DATA_DIR / "stores.csv", index=False)

print("Master data created successfully!")