f = open('sums_in_loop', 'r')
N = int(f.readline())

result_arr = []
for i in range(N):    
    arr = (f.readline()).split()
    sum_arr = 0
    for ch in arr:        
        sum_arr += int(ch)
        
    result_arr.append(sum_arr)
        
for ch in result_arr:
    print(ch, end=' ')


f.close()
