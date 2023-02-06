import pandas


#goal : create csv with colomn, fur color,count

data = pandas.read_csv("Squirrel_Data.csv")
# print(data_squirel)

#goal : create csv with colomn, fur color,count

gray_data_squirel = data[data["Primary Fur Color"]=="Gray"]
red_data_squirel = data[data["Primary Fur Color"]=="Cinnamon"]
black_data_squirel = data[data["Primary Fur Color"]=="Black"]

print (len(gray_data_squirel))
print (len(black_data_squirel))
print (len(red_data_squirel))

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[len(gray_data_squirel),len(red_data_squirel),len(black_data_squirel)],

}

print (data_dict)

#convert to dataframe
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")
print (data_frame)