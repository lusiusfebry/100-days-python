import pandas

student_dict ={
    "student" : ["Angela","James","Lily"],
    "score" : [56, 79,98]
}
#looping through dict
# for (key,value) in student_dict.items():
#     print (key,value)


#using pandas
student_data_frame = pandas.DataFrame(student_dict)
# print (student_data_frame)

#loop throug data frame
# for (key,value) in student_data_frame.items():
#     print (key)
#     print (value)

#loop trhough rows of a dataframe
for (index,row) in student_data_frame.iterrows():
    # print (index,row)
    print (row.student)