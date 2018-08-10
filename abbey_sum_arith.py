f = open('sum_arith')
sums = int(f.readline())
result_arr = []
for i in range(sums):
    arr = f.readline().split()
    a1 = int(arr[0])
    d = int(arr[1])
    n = int(arr[2])
    Sn = int((a1 + d*(n-1)/2)*n)
    result_arr.append(Sn)
for ch in result_arr:
    print(ch, end=' ')
