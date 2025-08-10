def is_multiply(digit):
	multiply = 1
	for number in range(2, len(digit), 3):
		multiply *= digit[number]
	return multiply
		
digit = [2,3,4,5,6,7,86,2,3,43,34,45,56]
result = is_multiply(digit)
print(result)

 