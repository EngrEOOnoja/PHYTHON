largest = 0
second_largest = 0
for counts in range(10):
	number = int(input("Enter an intger: "))
	if(number > largest):
		second_largest = largest
		largest = number 
	if(number > second largest and number < largest and number != largest):
		second_largest = number
	
	print(largest)
print(second_largest)
