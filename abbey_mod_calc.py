f = open('mod_calc')
N = int(f.readline())

while True:
    arr = f.readline().split()
    if arr[0] == '*':
        N = N * int(arr[1])
    elif arr[0] == '+':
        N = N + int(arr[1])
    else:
        print(N % int(arr[1]))
        break

f.close()
