matrix = [[0 for i in range(4)] for j in range(4)]
counter = 1
for i in range(4):
    for j in range(4):
        if i == j or i + j == 3:
            matrix[i][j] = counter
        else:
            matrix[i][j] = 17 - counter
        counter += 1

for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()