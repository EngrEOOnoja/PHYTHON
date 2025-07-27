miles = 1
count = 0
mileage = 0
while(miles != -1):
	gallon_used = float(input('Enter gallon Used (-1 to exit)'))
	if(gallon_used == -1):
		break
	miles = float(input('Enter miles driven '))
	
	mileage = miles/gallon_used
	print(round(mileage,2))
	mileage += 0
	count += 1
average = (mileage/count)
print(f'The Total average mileage was {average:.2f}')






 