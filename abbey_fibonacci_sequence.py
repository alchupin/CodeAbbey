from math import sqrt
from decimal import *
def fibonacci(n):
    a, b = 0, 1
    for __ in range(n):
        a, b = b, a + b
    return a
'''
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:        
        return fibo(n-2)+ fibo(n-1)
'''
          

f = open('fibonacci_sequence', 'r')
N = int(f.readline())
result_arr = []
for i in range(N):
    index = 0
    n_fib = float(f.readline())    
    while True:        
        if float(fibonacci(index)) == n_fib:
            result_arr.append(index)
            break
        index += 1
    print(index, end=' ')

f.close()
