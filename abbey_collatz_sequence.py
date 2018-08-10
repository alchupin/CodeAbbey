f = open('collatz-sequence')
n = f.readline()
STEP_NUMBER = 0
result_arr = []

arr = f.readline().split()
arr_int = []
for ch in arr:
    arr_int.append(int(ch))
for i in arr_int:
    STEP_NUMBER = 0
    while True:
        if i == 1:
            result_arr.append(STEP_NUMBER)
            break
        if i%2 == 0:
            i = i/2
            STEP_NUMBER += 1
        else:
            i = i*3 + 1
            STEP_NUMBER += 1
for j in result_arr:
    print(j, end=' ')
f.close()        
