def body_const(BMI):
    if BMI < 18.5:
        return 'under'
    elif 18.5 <= BMI < 25.0:
        return 'normal'
    elif 25.0 <= BMI < 30.0:
        return 'over'
    else:
        return 'obese'
    

f = open('BMI')
N = int(f.readline())
result_arr = []
for i in range(N):
    arr = f.readline().split()
    BMI = float(arr[0])/((float(arr[1]))**2)
    result_arr.append(body_const(BMI))
for ch in result_arr:
    print(ch, end=' ')
