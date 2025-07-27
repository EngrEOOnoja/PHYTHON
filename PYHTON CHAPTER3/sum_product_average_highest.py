number = int(input('Enter Digit: '))
counter = 1
add = 0
product = 1
highest = 0
smallest = number
for index in range(1,5):
	number = int(input('Enter Digit: '))
	if( number > highest):
		 highest = number
	if(number < smallest):
		 smallest = number
	add = add + number 
	average = add / index
	product = product * number
	
print(f'{add}\n{average}\n{product}\n{highest}\n{smallest}')



