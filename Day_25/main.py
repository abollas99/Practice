import csv
import pandas
with open("weather_data.csv") as data:
    data_list = csv.reader(data)
    temp = []
    for row in data_list:
        if row[1] != "temp":
            temp.append(int(row[1]))

    print(temp)

# Panda is an easier way of doing the code up top
data_list2 = pandas.read_csv("weather_data.csv")
print(data_list2[data_list2.temp == data_list2.temp.max()])
print("this is how to get a column using panda",  data_list2.temp)
print("this is how to get a row using panda", data_list2[data_list2.temp == data_list2.temp.max()])
