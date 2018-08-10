f = open('time_difference')
N = int(f.readline())
result_arr = []
for i in range(N):
    result = ()
    arr = []
    arr_str = f.readline().split()
    for ch in arr_str:
        arr.append(int(ch))
    time1 = arr[0]*24*60*60 + arr[1]*60*60 + arr[2]*60 + arr[3]
    time2 = arr[4]*24*60*60 + arr[5]*60*60 + arr[6]*60 + arr[7]
    diff = time2 - time1
    days = diff//(24*60*60)
    hours = (diff - (days*24*60*60))//(60*60)
    mins = (diff - (days*24*60*60) - (hours*60*60))//60
    secs = diff - (days*24*60*60) - (hours*60*60) - (mins*60)    
    print('('+ str(days), hours, mins, str(secs)+')', end=' ')


f.close()
