import pandas as pd
player = {"Last Name": ["Bacot", "Davis", "Cadeau", "Evans", "High", "Brown", "Dixon", "Young", "Denis", "Davis"],
          "First Name": ["Armando", "RJ", "Elliot", "Kyan", "Zayden", "James","Derek","Jaydon", "Isaiah", "Elijah"],
          "height": [83, 72, 73, 72.24, 73.2, 73.2, 72.6, 72.48, 72.48, 72.36],
          "weight": [240, 180, 180, 175, 230, 240, 200, 200, 180, 205]}
data =pd.DataFrame(player)
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)
data["bmi"] = data["bmi"].round(2)
print(data)
data.to_csv("bmi.csv")

