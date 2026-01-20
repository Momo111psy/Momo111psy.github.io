import csv
import random

countries = ["UAE", "USA", "UK", "Germany", "Belgium"]
with open('dubai_leads_sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Country", "Type", "Status"])
    for i in range(1, 400):
        writer.writerow([f"GLO-{i:03}", random.choice(countries), "Premium", "Verified"])
print("Global CSV updated for all country frames.")
