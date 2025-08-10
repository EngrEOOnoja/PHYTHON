def is_multiply(digit):
	for number in digit:
		average = ((digit[0] + digit[1] + digit[2] + digit[3] + digit[4] + digit[5] + digit[6] + digit[7] + digit[8] + digit[9] + digit[10] + digit[11] + digit[12]) / len(digit))
		return average
		
digit = [2,3,4,5,6,7,86,2,3,43,34,45,56]
result = is_multiply(digit)
print(result)

 
