#3.15 (Challenge: Approximating the Mathematical Constant e) Write a script that estimates the value of the mathematical constant e by using the formula below. Your script
#can stop after summing 10 terms.



factorial = 1
sum = 1
for factor in range(1, 11):
	factorial = factorial * factor
	sum = sum + (1 / factorial)
print(round(sum,4))
print(f'{sum: .2f}')	














