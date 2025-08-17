#Create a tuple of numbers and append a new
#number to it without directly modifying the
#tuple.
#2. Given numbers = (1, 2, [3, 4], 5),
#change the third element's second value to 99.
#3. Convert a tuple of strings ('apple',
#'banana', 'cherry') into a list, add
#'mango', and convert back to tuple.
#4. Write a program to unpack this tuple: (10, 20,
#30, 40) into variables a, b, and the rest
#in the last variable.*/


def toAddTuple(number, number2):

	return (number  + number2 )



number = (2,1,5,6,8,4,67)
number2 = (7,9,23,54)
result =  toAddTuple(number, number2)
print(result)