# import csv

# with open("Day 25\\weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for value in data:
#         if value[1] != "temp":
#           temperatures.append(int(value[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("Day 25\\weather_data.csv")
# print(type(data))
# print(data)

#Make a dictionary from data
# data_dict = data.to_dict()
# print(data_dict)

# Find values from a column
# print(f"Mean: {data['temp'].mean()}")
# print(f"Max: {data['temp'].max()}")

# These are the same
# print(data["condition"])
# print(data.condition)

# Get data from row name
#
# Create a dataframe for scratch
# data_dict = {
#     "students": ["Amy", "James","Angela"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Day 25\\new_data.csv")

#SQUIRRELS

squirrel_data = pandas.read_csv("Day 25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_count)
print(cinnamon_count)
print(black_count)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_count,cinnamon_count,black_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("Day 25\\Squirrel Practice\\squirrel_count.csv")
