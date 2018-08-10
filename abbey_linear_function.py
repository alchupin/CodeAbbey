f = open('linear_function')

N = int(f.readline())

for i in range(N):
    arr = f.readline().split()
    x1 = int(arr[0])
    y1 = int(arr[1])
    x2 = int(arr[2])
    y2 = int(arr[3])

    a = int((y2-y1)/(x2-x1))
    b = int((x2*y1 - y2*x1)/(x2-x1))
    print('('+str(a), str(b)+')', end=' ')



f.close()
