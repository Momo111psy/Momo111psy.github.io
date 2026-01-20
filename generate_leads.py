import csv
import random

areas = ["Downtown Dubai", "Dubai Marina", "Palm Jumeirah", "Business Bay", "JVC", "Dubai Hills"]
types = ["Apartment", "Villa", "Penthouse", "Townhouse"]
statuses = ["Available", "Sold", "Under Offer"]

with open('dubai_leads_sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Property_ID", "Area", "Type", "Price_AED", "Status"])
    for i in range(1, 101):
        writer.writerow([
            f"DXB-{i:03}",
            random.choice(areas),
            random.choice(types),
            random.randint(800000, 25000000),
            random.choice(statuses)
        ])
