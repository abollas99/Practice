import pandas
import csv

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black_count = 0
cinn_count = 0
gray_count = 0
for x in data["Primary Fur Color"]:
    if x == "Gray":
        gray_count += 1
    elif x == "Cinnamon":
        cinn_count += 1
    elif x == "Black":
        black_count += 1
print(gray_count, cinn_count, black_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinn_count]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Squirrel_Data.csv")
