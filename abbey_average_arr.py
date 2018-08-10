f = open('average_array')
N = int(f.readline())
result_arr = []
for i in range(N):
    arr = f.readline().split()[:-1]
    arr_sum = 0
    for ch in arr:
        arr_sum += int(ch)
    arr_average = arr_sum/len(arr)
    if (str(arr_average).split('.')[1][0]) == '5' and int(str(arr_average).split('.')[0][-1])%2 == 0:
        result_arr.append((round(arr_average) + 1))
    else:
        result_arr.append(round(arr_average))

for ch in result_arr:
    print(ch, end=' ')
f.close()
