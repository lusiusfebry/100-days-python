# # #
# # # with open("weather_data.csv","r") as file:
# # #     content = file.readlines()
# # #     print (content)
# #
# #
# # import csv
# #
# # with open("weather_data.csv","r") as file:
# #     content  = csv.reader(file)
# #     # temperature = [temp[1] for temp in content if temp[1] != "temp"]
# #     temperature = []
# #     for row in content:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
# # print (temperature)
#
import pandas
#
data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# temp_dict = data.to_dict()
# # print(temp_dict)
#
# # print (help(list))
# # sum_list = sum(temp_list)
# # print ("average: ",sum_list / len(temp_list))
# averange = data["temp"].mean()
# max_value = data["temp"].max()
# print (averange)
# print (max_value)
#
# condition_value = data.condition
# print (data["condition"])
# print(condition_value)

# data_row = data[data.day == "Monday"]
# data_row2 = data[data["day"]=="Monday"]
# print (data_row)
# print (data_row2)

#pullout highest temperature
# data_max = data[data.temp == data["temp"].max()]
# print (data_max)

#pull monday condition
# monday = data[data.day == "Monday"]
# print (monday.condition)

#convert monday temperatur to fahranheit
# monday_data=data[data.day == "Monday"]
# monday_temp_in_cel = int (monday_data.temp)
# print (monday_temp_in_cel)
# monday_temp_to_fahranheit = monday_temp_in_cel * (9/5) + 32
# print (monday_temp_to_fahranheit)

#how to create dataframe from scratch
data_dict = {
    "student" : ["Ani","James","Angela"],
    "score" : [76,56,65]
}

panda_dataframe = pandas.DataFrame(data_dict)
print (panda_dataframe)

#panda to csv
panda_dataframe.to_csv("panda_data_frame.csv")





