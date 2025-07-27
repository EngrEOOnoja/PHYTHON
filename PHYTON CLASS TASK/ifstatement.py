a = input()
b = input()
c= input()
highest_score = a
if (b < a): 
	highest_score = b
elseif (c < a) 
	highest_score = c

	print(highest_score)

a = input()
b = input()
c= input()
second_highest_score = a
if (b < a and b > c):break
	second_highest_score = b
elseif (c < b and c > a ): 
		second_highest_score = c

	print(second_highest_score)

print"""
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thursday
5 = Friday
6 = Saturday
7 = Sunday
	   """


days_of_week
match:
case 1: 
	print(Monday)
case 2: 
	print(Tuesday)
case 3:
	print(Wednesday)
case 4:
	print(Thursday)
case 5:
	print(friday)
case 6:
	print(Saturday)
case 7:
	print(sunday)