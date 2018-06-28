import json
import csv

with open("file_userss.json") as file:
    data = json.load(file)

with open("data.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['pk'], item['model']] + item['fields'].values())