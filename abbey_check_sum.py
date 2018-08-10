f = open('check-sum')
n = f.readline()
SEED = 113
LIMIT = 10000007
result = 0
arr = f.readline().split()
for ch in arr:
    result += int(ch)
    result *= SEED
    result = result%LIMIT


print(result)

f.close()

def check_sum(arr):
    SEED = 113
    LIMIT = 10000007
    result = 0    
    for ch in arr:
        result += int(ch)
        result *= SEED
        result = result%LIMIT
    return(result)

