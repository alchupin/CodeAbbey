f = open('sort_indexes', 'r')
N = int(f.readline())

arr = [int(ch) for ch in f.readline().split()]
dic_number = {}
for i in range(len(arr)):
    dic_number[arr[i]] = i+1
arr.sort()
for i in range(len(arr)):
    print(dic_number[arr[i]], end=' ')

f.close()

#print(' '.join(str(v.index(i) + 1) for i in sorted(v)))
