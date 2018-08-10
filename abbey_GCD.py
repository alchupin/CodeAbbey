f = open('GCD')
N = int(f.readline())
for i in range(N):
    arr = [int(ch) for ch in f.readline().split()]
    a, b = arr[0], arr[1]
    
    while True:
        if arr[0] == arr[1]:
            gcd = arr[0]
            break
        elif arr[0] > arr[1]:
            arr[0] -= arr[1]
        else:
            arr[1] -= arr[0]
    lcm = int(a*b/gcd)
    print('(' + str(gcd), str(lcm) + ')', end=' ')


f.close()
