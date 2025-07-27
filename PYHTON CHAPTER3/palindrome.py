number = int(input())
if(number > 9999 and number < 100000):
	digit1 = number // 10000
	digit2 = (number % 10000)//1000
	digit3 = (number % 1000)//100
	digit4 = (number % 100)//10
	digit5 = (number % 10)//1
	
	
	converted_number = (digit5 * 10000) + (digit4 * 1000) + (digit3 * 100) + (digit2 * 10) + (digit1 * 1)
	
	if (number == converted_number):
		print('Number is a palindrome')
	else:
		print('Number is not a palindrome')
else:
	print('Invalid Input')	