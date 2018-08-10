N = int(input('Enter number of numbers:\n'))
arr = input('Enter array:\n')
sum = 0
for i in range(N):
    sum += int(arr.split(' ')[i])
print(sum)

