def is_even(digit):
	new_list = [num for num in digit if num % 2 == 0]
	sum = new_list[0] + new_list [1] + new_list [2] + new_list [3] + new_list [4] + new_list[5] + new_list[6]
	return sum
	
digit = [2,3,4,5,6,7,86,2,3,43,34,45,56]
result = is_even(digit)
print(result)
