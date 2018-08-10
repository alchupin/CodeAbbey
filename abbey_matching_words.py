w_list = sorted((input('Enter a list:\n')).split(' '))
#print(w_list)
result_list = []
for word in w_list:
    if word in result_list:
        continue
    if w_list.count(word)>1:
        result_list.append(word)
for ch in result_list:    
    print(ch, end=' ')
