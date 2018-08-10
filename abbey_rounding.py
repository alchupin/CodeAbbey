f = open('rounding', 'r')
N = int(f.readline())
result_arr = []
for i in range(N):
    arr = f.readline().split()
    result_arr.append(round(int(arr[0])/int(arr[1])))
for ch in result_arr:
    print(ch, end=' ')
    
    
