f = open('arr_counters')
n = f.readline()
result_arr = [0 for x in range(1, 21)]

arr = f.readline().split()
for ch in arr:
    if int(ch)>0:
        result_arr[int(ch)+1] += 1
    
for ch in result_arr:
    if int(ch)>0:
        print(ch, end=' ')

f.close()
