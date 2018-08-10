f = open('vowels', 'r')
N = int(f.readline())
result_arr = []
vowels = 'aeiouy'
for i in range(N):
    v_numbers = 0
    arr = f.readline()
    for ch in arr:
        if ch in vowels:
            v_numbers += 1
    result_arr.append(v_numbers)
for ch in result_arr:
    print(ch, end=' ')
