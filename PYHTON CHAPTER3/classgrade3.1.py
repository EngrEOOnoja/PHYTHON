passed = 0
failed = 0
for student_score in range(10):
	result = int(input('Enter result (1= passed, 2=failed)  :' ))
	while True:
		if(result == 1 ):
			passed += 1
			break
		elif(result == 2):
			failed += 1
			break
		else:
			result = int(input('Enter result (1= passed, 2=failed)  :' ))

print('passed :',passed)
print('failed :',failed)

if passed >= 8:
	print ('Bonus to instructor')
 