import csv
import random

countries = ["UAE", "USA", "Germany", "UK", "Switzerland", "Belgium"]
types = ["Residential", "Commercial", "Industrial"]

with open('dubai_leads_sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Lead_ID", "Country", "Property_Type", "Price_USD", "Lead_Status"])
    for i in range(1, 401):
        writer.writerow([
            f"MOMO-{i:03}",
            random.choice(countries),
            random.choice(types),
            random.randint(500000, 15000000),
            "Trial_Available"
        ])
print("Global Database Updated: 400 Trial Leads Ready.")
