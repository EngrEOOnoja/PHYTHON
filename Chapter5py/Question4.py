rows, cols = 2, 3

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

counter = 1
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = counter
        counter += 1

print("   ", end="")
for j in range(cols):
    print(f"{j:>5}", end="")
print()

for i in range(rows):
    print(f"{i:<3}", end="")   
    for j in range(cols):
        print(f"{matrix[i][j]:>5}", end="")
    print()
