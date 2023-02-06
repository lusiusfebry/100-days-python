weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
#celsius to fahrenheit :(temp_c * 9/5) + 32 = temp_f
weather_f={temp:key * (9/5) + 32 for (temp,key) in weather_c.items()}

# for item in weather_c.values():
#     print (item)

print(weather_f)



