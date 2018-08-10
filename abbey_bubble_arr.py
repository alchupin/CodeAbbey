def check_sum(arr):
    SEED = 113
    LIMIT = 10000007
    result = 0
    for ch in arr:
        result += int(ch)
        result *= SEED
        result = result%LIMIT
    return(result)

arr_str = input('\n').split()[:-1]
counter = 0
arr = []
for ch in arr_str:
    arr.append(int(ch))
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        counter += 1
    
print(counter, check_sum(arr))
