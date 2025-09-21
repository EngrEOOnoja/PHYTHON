largest = 0
second_largest = 0
for number in range (10):
	digit = int(input("Enter a positive integer :",   ))
	if(digit > largest):
		second_largest = largest
		largest = digit
	if(second_largest < digit and digit < largest and largest != digit):
		second_largest = digit
		
	
print(largest)
print(second_largest)













