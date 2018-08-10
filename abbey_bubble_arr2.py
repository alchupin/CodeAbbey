f = open('bubble_sort')
N = f.readline()
arr = [int(ch) for ch in f.readline().split()]
counter = 0
pass_number = 0
while True:
    pass_number += 1
    Flag = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            counter += 1
            Flag = False
                #print(arr)
    if Flag:
        break
    
print(pass_number, counter)
