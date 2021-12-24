# Day25 of 100 Days Of Code


# Read data from a CSV file
# without importing CSV

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# Read data from a CSV file by importing CSV

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# Read data from a CSV file by importing pandas

import pandas

data = pandas.read_csv("weather_data.csv")

# printing a column
# print(data["temp"])

# convert data into dictionary
# data_dict = data.to_dict()
# print(data_dict)

# convert a particular column into list
temp_list = data["temp"].to_list()
print(temp_list)

# get average temperature without using any pre-defined function
# total_temp = 0
# total_entries = 0
# for temp in temp_list:
#     total_temp += temp
#     total_entries += 1
#
# avg_temp = total_temp / total_entries
# print(avg_temp)

# average temperature using pre-build functions
print(sum(temp_list) / len(temp_list))

# maximum temperature
print(data["temp"].max())

# print row where temperature is maximum
print(data[data.temp == data["temp"].max()])

# print only condition
monday = data[data.day == "Monday"]
print(monday.condition)

# print monday temp into Fahrenheit
print((int(monday.temp) * 9/5) + 32)

# create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

# from new data frame create a csv file
data.to_csv("scores.csv")

