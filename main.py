from random import random
def naibolshee(A):
    n = A[0]
    for i in range (len(A)):
        if A[i]>=n:
            n = A[i]
    return n

R = int(input("введите размерность массива:"))
A = [0]*R
for i in range(R):
    A[i] = round(random()*10,1)
print('исходный массив:',A)
m = naibolshee(A)
for i in range(R):
    if A[i] == m:
        for i in range(i + 1,R):
            A[i] = 0
print('результат:',A)