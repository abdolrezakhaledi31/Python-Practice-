import csv

data = [
    ["name", "age", "city"],
    ["Ali", 25, "Tehran"],
    ["Sara", 30, "Shiraz"],
    ["Reza", 28, "Mashhad"],
    ["Mohamd", 40, "Ahwaz"],
]
with open("students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
