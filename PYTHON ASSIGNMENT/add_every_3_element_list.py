def add_every_3_element_list(digit):
	add = 0
	for number in range(2, len(digit), 3):
		add += digit[number]
	return add
		
digit = [2,3,4,5,6,7,86,2,3,43,34,45,56]
result = add_every_3_element_list(digit)
print(result)

 
