f = open('wsd')
N = f.readline()
result_arr = []
arr = f.readline().split()

for number in arr:
    i = 1
    wsd = 0
    for ch in number:
        wsd += int(ch) * i
        i += 1
    result_arr.append(wsd)
for ch in result_arr:
    print(ch, end=' ')
    
