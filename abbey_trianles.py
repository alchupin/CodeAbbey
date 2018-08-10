f = open('triangles')
N = int(f.readline())
result_arr = []
for i in range(N):
    arr = f.readline().split()
    a, b, c = int(arr[0]), int(arr[1]), int(arr[2])
    if a+b>c and a+c>b and b+c>a:
        result_arr.append(1)
    else:
        result_arr.append(0)
for ch in result_arr:
    print(ch, end=' ')
f.close()
