arr = [int(ch) for ch in input().split()]
arr_r = [i for i in range(1, arr[0]+1)]
multi = arr[1]
arr_cut = [i for i in arr_r if i%multi != 0]
while True:
    if len(arr_cut) == 1:
        print(arr_cut)
        break
    else:
        arr_cut = [i for i in arr_r if i%multi != 0]
