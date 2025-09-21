largest = -100
second_largest = 0
for count in range (10):
	digit = int(input("Enter a positive input", ))
	if(digit > largest):
		second_largest = largest
		largest = digit
	if(digit < largest and digit > second_largest and digit != largest):
		second_largest = digit
	
	
	
	
	
	
print("largest", largest)
print("secondlargest", second_largest)
		






