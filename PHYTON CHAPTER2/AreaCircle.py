(Separating the Digits in an Integer) Write a script that inputs a five-digit integer
from the user. Separate the number into its individual digits. Print them separated by three
spaces each. For example, if the user types in the number 42339, the script should print
4 2 3 3 9



integer = input()
if(integer > 9999 && integer < 100000):
integer1 = (integer / 10000)
integer2 = (integer % 10000)/1000
integer3 = (integer % 1000)/100
integer4 = (integer % 100)/10
integer5 = (integer % 10)/1

print(integer1,'   ',integer2,'    'integer3,'    'integer4,'    '.integer5')
 