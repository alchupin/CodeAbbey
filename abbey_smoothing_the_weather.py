
f = open('smoothing_the_weather', 'r')
N = int(f.readline())
arr_result = []
arr = [float(ch) for ch in f.readline().split()]
arr_result.append(arr[0])
for i in range(1, N-1):
    arr_result.append(round((arr[i-1] + arr[i] + arr[i+1])/3, 10))
arr_result.append(arr[N-1])
for j in arr_result:
    print(j, end=' ')

f.close()
