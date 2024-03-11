import pandas
data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())

# data in columns
# print(data["temp"].max())
# print(data["temp"])
# print(data.temp)

# data in rows
# print(data[data.day == "Monday"])
# print(data)
# print(data[data.temp == data.temp.max()])

# get temperation in Fahrenheit for Monday
monday = data[data.day == "Monday"]
print(monday.temp[0] * 9/5 + 32)