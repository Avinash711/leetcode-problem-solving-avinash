str_data = 'abcd' 
res_lis_d = []
for i in range(len(str_data)):
    for j in range(i, len(str_data)):
        res_lis_d.append(str_data[i:j+1])
#print(res_lis)
print(res_lis_d)



# return str who has unique charcters with length


def unique_str(res_lis_d):
    uniq_lis =[]
    for str_val in res_lis_d:
        uniq = {}
        count = 0
        for ch in str_val:
            if ch not in uniq:
                #print(f'{str_val} is uniq')
                uniq[ch] = 1
            else:
                count +=1
        if count == 0: #unique strings
                uniq_lis.append(str_val)
    #print(list(set(uniq_lis)))
    #uniq_lis = list(set(uniq_lis))
    print(uniq_lis)

    #res = max(uniq_lis, key = len)
    #print(res)
    max_len = -1
    res = ''
    for ele in uniq_lis:
        if max_len < len(ele):
            res = ele
            max_len = len(ele)

    print(res)
    return res


unique_str(res_lis_d)