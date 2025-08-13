#3.15 (Challenge: Approximating the Mathematical Constant e) Write a script that estimates the value of the mathematical constant e by using the formula below. Your script
#can stop after summing 10 terms.



factorial = 1
sum = 0
for factor in range(1, 11):
	factorial = factorial * factor
	factor -= 1
	sum = sum + (1 / factorial)
print(sum)
	














