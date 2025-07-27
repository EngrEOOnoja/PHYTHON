#if(integer > 9999 and integer < 100000):
# integer1 = (integer // 10000)
 #integer2 = (integer % 10000)//1000
 #integer3 = (integer % 1000)//100
# integer4 = (integer % 100)//10
 #integer5 = (integer % 10)//1

print(integer1,'   ',integer2,'    ',integer3,'    ',integer4,'    ',integer5)
 

user = input()
counter = 10000
modulus = 10000
while user > 9999 and user < 100000:
	if cunter < 10:
		number1 = user // counter
		print('The number is', + number1)
		number1 % counter
		 counter /= 10
		 
	
	