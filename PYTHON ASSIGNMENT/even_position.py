#Create an empty tuple
#Add integers between 1 - 20 in the tuple
#Sum of the elements at odd positions in the
#tuple
#Sum of the elements at even positions in the
#tuple
#Sum up the smallest and highest element in the
#tuple
#unpack the first five elements in the tuple




digit = tuple(range(1,21))
sum = 0
for number in range (0, len(digit), 2):
	sum += digit[number]
print(sum)

















