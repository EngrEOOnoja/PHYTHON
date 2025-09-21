


#[filter(...)]	Creates a list with one filter object inside#
#list(filter(...))	Actually runs the filter and gives you the filtered list

cars = [ "lambo", "Volvo", "Toyota", "Lexus", "Merceddes", "Audi", "Ferrari"]

def is_five_letters_max(car):
	if len(car) <= 5:
		return True



#reserved_cars = [filter( is_five_letters_max, cars)]
#print(list(filter( is_five_letters_max, cars)))			


numbers = ["game", "car", "house", "kingdom"]
numbers2 = [2, 4, 5, 6, 7]

print(list(map(str.upper,numbers)))
print(list(map(len ,numbers)))
#print(list(map,number2))



#reduce function
from functools import reduce
#import functools
numbers = [7, 3, 5, 6, 1, 2, 9]
def addition(x,y):
	return x + y
	
summation = reduce(addition, numbers)


print(summation)

#using maps in reduc function .....#
numbers = [7, 3, 5, 6, 1, 2, 9]
def addition(x,y):
	return x + y
	
summation = list(map(addition, [6,7,1, 2], numbers))
print(summation)










#Two Dimentional List.
#unpacking
numbers = [["Ade", "Musa", "Bayo"], [79.8, 54.3,87.6], [10, 12, 15] ]

names,  scores, age = numbers

print("student names : ",  names )
print("student scores : ",  scores )
print("student ages : ",  age )



student_record =, [79.8, 54.3,87.6], [10, 12, 15] ]   #by their index.

for index, student_details in enumerate(student_records):
	student_name = student_details[index]


names = student_record[0]
scores = student_record[1]
age = student_record[2]


print("student names : ",  names )
print("student scores : ",  scores )
print("student ages : ",  age )





print(student_records[0][9], 








































