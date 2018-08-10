import collections
f = open('rotate_string', 'r')
N = int(f.readline())
for i in range(N):
    str_result=  ''
    arr = [ch for ch in f.readline().split()]
    number = int(arr[0])
    string_1 = arr[1]   
    str_result += string_1[number:] + string_1[:number]
    print(str_result, end=' ')
f.close()
