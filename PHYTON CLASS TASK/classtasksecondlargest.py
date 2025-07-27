number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
second_highest_number = number_2
if (number_1 < second_highest_number and number_1 > number_3):
	second_highest_number = number_1
if(number_3 < second_highest_number and number_3 > number_1):
	second_highest_number = number_3
print(second_highest_number)	
