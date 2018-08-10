def median_of_three(a, b, c):
    if (a >= b and a <= c) or (a <= b and a >= c) :
        return a
    elif (b >= a and b <= c) or (b <=a and b >= c):
        return b
    else:
        return c
    
f = open('median', 'r')
N = int(f.readline())
result_arr = []
for i in range(N):
    arr = list(f.readline().split())
    result_arr.append(median_of_three(int(arr[0]), int(arr[1]), int(arr[2])))
for ch in result_arr:
    print(ch, end=' ')


f.close()
