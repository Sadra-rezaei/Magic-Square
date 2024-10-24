number = int(input())

matrix = [[0 for i in range(number)] for j in range(number)]


i = 0
j = int(number/2)
counter = 2

matrix[i][j] = 1
while counter <= number*number:
    if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == 0:
        i -= 1
        j -= 1
    elif i - 1 < 0 and j - 1 < 0:
        if matrix[number -1][number -1] == 0:
            i = number -1
            j = number-1
        else:
            i += 1
    elif i - 1 < 0:
        if matrix[number-1][j-1] == 0:
            i = number-1
            j -= 1
        else:
            i += 1
    elif j - 1 < 0:
        if matrix[i-1][number-1] == 0:
            j = number -1
            i -= 1
        else:
            i += 1
    elif i == number-1:
        i = 0
    else:
        i += 1


    matrix[i][j] = counter
    counter += 1



for i in range(number):
    for j in range(number):
        print(matrix[i][j], end=" ")
    print()



sumP = 0
sumC = 0
sumZ1 = 0

for i in range(number):
    for j in range(number):
        if i == j:
            sumP += matrix[i][j]
        if i+j == number-1:
            sumC += matrix[i][j]
        if i == 0:
            sumZ1 += matrix[i][j]

if sumP == sumC == sumZ1:
    print("MAGIC SQUARE")