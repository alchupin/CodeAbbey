f = open('square_root', 'r')
N = int(f.readline())
for i in range(N):
    arr = [int(ch) for ch in f.readline().split()]
    value = arr[0]
    steps = arr[1]
    result = 1
    for j in range(steps):
        result = (result + value/result)/2
        
    print(round(result, 7), end=' ')


f.close()
