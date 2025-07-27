number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

second_largest = number_1

if(number_2 < number_1 and number_2 > number_3)
	second_largest = number_2
if(number_3 < number_2 and number_3 > number_1)
	second_largest = number_3
print(second_largest)