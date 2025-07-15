integer = int(input())
if(integer > 9999 and integer < 100000):
 integer1 = (integer // 10000)
 integer2 = (integer % 10000)//1000
 integer3 = (integer % 1000)//100
 integer4 = (integer % 100)//10
 integer5 = (integer % 10)//1

print(integer1,'   ',integer2,'    ',integer3,'    ',integer4,'    ',integer5)
 