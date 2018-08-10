f = open('bicycle', 'r')
N = int(f.readline())
for i in range(N):
    arr = [int(ch) for ch in f.readline().split()]
    S = arr[0]
    v1 = arr[1]
    v2 = arr[2]
    S1 = round(float((S*v1)/(v1+v2)), 7)
    print(S1, end=' ')

f.close()
