f = open('neumans_random_generator', 'r')
N = int(f.readline())
arr = [int(ch) for ch in f.readline().split()]

for i in arr:
    arr_result = []
    result1 = i
    index = 0
    while True:        
        result2 = ((result1*result1)//100)%10000
        index += 1
        if result2 in arr_result:
            print(index, end=' ')
            break
        else:
            arr_result.append(result2)
            result1 = result2
    
f.close()        
