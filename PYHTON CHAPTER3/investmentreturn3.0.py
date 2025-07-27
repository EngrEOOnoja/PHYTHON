p = 1000
r = 0.07
z = p + r*p
n = float(input())
a = z**n

print(a)

for n in range(1,30):
	a = z**n

	print(a)