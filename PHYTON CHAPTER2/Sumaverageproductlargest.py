number1 = int(input())
number2 = int(input())
number3 = int(input())

sum = number1 + number2 + number3
print(sum)
average =sum / 3
print(average)
product = number1 * number2 * number3
print(product)

smallest = number1
if(number2 < smallest):
 smallest = number2
if(number3 < smallest):
 smallest = number3
print(smallest)

largest = number1
number1 = largest
if(number2 > largest):
 largest = number2
if(number3 > largest):
 largest = number3
print(largest)
