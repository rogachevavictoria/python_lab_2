# n = int(input())
# L1 = []
# for i in range (0,n):
#     a = pow(2, pow(2, int(i))) + 1
#     L1.append(a)
# print(L1)
# L2 = [pow(2, pow(2, int(j))) + 1 for j in range (0,n)]
# print(L2)
# import random
# L = []
# n = int(input())
# ans = int(input())
# if ans == 1:
#     for i in range(0, n):
#         L.append(int(input()))
# else:
#     for i in range(0, n):
#         L.append(random.randint(1, 100))
# print(L)
# a = L[1:len(L):2]
# b = L[0:len(L):2]
# a1 = 0
# b1 = 0
# for i in range(0,len(a)):
#     a1 += a[i]
# print('even: ' + str(a1))
# for i in range(0,len(b)):
#     b1 += b[i]
# print('odd: ' + str(b1))
# if a1 > b1:
#     print('Answer: even')
# else:
#     print('Answer: odd')
# import random
# import math
# n = int(input())
# X = []
# Y = []
# a = 0; b = 0; c = 0; d = 0; e = 0;
# for i in range (0,n):
#     X.append(random.randint(1, 100))
#     Y.append(random.randint(1, 100))
# for i in range (0,n):
#     a += (X[i] * Y[i])
#     b += X[i]
#     c += Y[i]
#     d += pow(X[i],2)
#     e += pow(Y[i],2)
# r = (n * a - b * c)/math.sqrt((n * d - pow(b,2)) * (n * e - pow(c,2)))
# print(X)
# print(Y)
# print("r = " + str(r))
n = int(input())
m = int(input())
L = []
for i in range (0,n):
    L.append(i+1)
res = 0
for i in range(1, n + 1):
    res = (res + m) % i
print(res + 1)