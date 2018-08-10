f = open('dice_rolling')
N = int(f.readline())
result_arr = []
for i in range(N):
    result_arr.append(int(float(f.readline())*6) + 1)
for ch in result_arr:
    print(ch, end=' ')
