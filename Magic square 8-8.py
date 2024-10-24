def GhadrMotlagh(number):
    if number < 0:
        number *= -1
    return number

matrix = [[0 for i in range(8)] for j in range(8)]
counter = 1
for i in range(8):
    for j in range(8):
        if i == j or i + j == 3 or i + j == 7 or i + j == 11 or GhadrMotlagh(i - j) == 4:
            matrix[i][j] = counter
        else:
            matrix[i][j] = 65 - counter
        counter += 1

for i in range(8):
    for j in range(8):
        print(matrix[i][j], end=" ")
    print()