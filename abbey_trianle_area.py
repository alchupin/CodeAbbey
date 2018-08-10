
import math
f = open('triangle_area', 'r')
N = int(f.readline())
for i in range(N):
    arr = [int(ch) for ch in f.readline().split()]
    x1 = arr[0]
    y1 = arr[1]
    x2 = arr[2]
    y2 = arr[3]
    x3 = arr[4]
    y3 = arr[5]

    S = math.fabs((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3))/2
    print(round(S, 7), end=' ')

    

f.close()
