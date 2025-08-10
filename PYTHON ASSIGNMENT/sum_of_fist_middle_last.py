#write a python function to calculate the sum of the
#first, middle and last elements within a designated
#list.


def sum_of_fist_middle_last(digit):
	sum = 0
	for number in range (0, 12):
		middle = len(digit)
		if(middle % 2 != 0):
			sum = digit[number] + digit[-1] + digit[(middle // 2) ] 
		else:
			sum = digit[number] + digit[-1] + digit[middle // 2] + digit[(middle // 2) + 1] 

		return sum
		
digit = [2,3,4,5,6,7,86,2,3,43,34,45,56]
result = sum_of_fist_middle_last(digit)
print(result)
