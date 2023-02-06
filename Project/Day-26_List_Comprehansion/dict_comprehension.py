#formula
#new_dict = {new_key:new_value for item in list}
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

from random import randint
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

student_score = {name:randint(1,100) for name in names}
print (student_score)

passed_student = {student:key for (student,key) in student_score.items() if key > 80}
print (passed_student)





