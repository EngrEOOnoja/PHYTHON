passed = 0
failed = 0
for student_score in range(10):
	result = int(input('Enter result (1= passed, 2=failed)  :' ))
	if(result == 1 or result == 2):
		if(result == 1):
			passed += 1
		if result == 2:
			failed += 1
print('passed :',passed)
print('failed :',failed)

2


#3



#4#
#count = 1
#for row in range(7):
#	count +=1
#	for row in range(1):
#		count +=1
#		print('\n @', end="")	
#	print('@',end='')

	