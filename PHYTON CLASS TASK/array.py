scores= [12,6,4,5,9]
highest = scores[0]
smallest = scores[0]
for numbers in scores :
	if (numbers > highest): 
		highest = numbers
	if (numbers < smallest):
		smallest = numbers

	
print(highest - smallest)


