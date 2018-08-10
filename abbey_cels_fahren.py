arr = input().split()
N = int(arr.pop(0))
for ch in arr:
    print(round(5*((int(ch)) - 32)/9), end=' ')
