N = int(input())

for i in range(N):    
    arr = input().split()
    sum_arr = 0
    for ch in arr:        
        sum_arr += int(ch)
        
    result_arr.append(sum_arr)
        
for ch in result_arr:
    print(ch, end=' ')
