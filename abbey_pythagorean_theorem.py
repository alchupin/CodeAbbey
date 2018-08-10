import math
f = open('pythagorean_theorem', 'r')
N = int(f.readline())
for i in range(N):
    arr = [int(ch) for ch in f.readline().split()]
    a = arr[0]
    b = arr[1]
    c = arr[2]
    length = math.sqrt((a*a) + (b*b))
    if length < c:
        print('O', end=' ')
    elif length > c:
        print('A', end=' ')
    else:
        print('R', end=' ')


f.close()
