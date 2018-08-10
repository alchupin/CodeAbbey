f = open('sum_of_digits')
N = int(f.readline())
result_arr = []
for i in range(N):
    sum_digits = 0
    arr = f.readline().split()
    sum_number = int(arr[0]) * int(arr[1]) + int(arr[2])
    for ch in str(sum_number):
        sum_digits += int(ch)
    result_arr.append(sum_digits)

for ch in result_arr:
    print(ch, end=' ')
