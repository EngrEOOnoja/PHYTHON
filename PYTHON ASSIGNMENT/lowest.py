def is_multiply(digit):
	for number in digit:
		lowest = digit[0]
		for number in range(1,13):
			if (lowest > digit[2]):
				lowest = digit[2]
		return lowest
		
digit = [2,3,4,5,6,7,86,2,3,43,34,45,56]
result = is_multiply(digit)
print(result)

 


