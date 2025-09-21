from math import prod

def arbitrary_argument(a, b, *args):
    return prod((a, b, *args))

others = (2, 3, 4, 5, 6, 7, 8, 9, 87)

result = arbitrary_argument(1, 1, *others)
print(result)