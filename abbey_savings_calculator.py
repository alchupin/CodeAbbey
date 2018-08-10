f = open('percent', 'r')
N= int(f.readline())
for i in range(N):
    arr = [int(ch) for ch in f.readline().split()]
    init = arr[0]
    goal = arr[1]
    percent = arr[2]
    years = 0
    while (init < goal):
        init = round(init*(100 + percent)/100, 2)
        years += 1
    print(years, end=' ')
        
        
        
    


    
f.close()
