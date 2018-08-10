import string
f = open('palindrome', 'r')
N = int(f.readline())

for i in range(N):
    arr_lower = []
    arr = [ch for ch in f.readline() if ch in string.ascii_letters]
    for ch in arr:
        arr_lower.append(ch.lower())
    
    if arr_lower == arr_lower[::-1]:
        print('Y', end=' ')
    else:
        print('N', end=' ')


f.close()
