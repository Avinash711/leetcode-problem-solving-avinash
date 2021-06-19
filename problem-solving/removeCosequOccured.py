
'''
ip
[3,4,4,5,6,6,6,8,8,9,9,9,10,4]
o/p
[3,5,10,4]
'''
test_list = [3,3,3,3,4,4,5,5,6,6,6,8,8,9,9,9,10,10,4,4,4]
res_list =[]
count = 0
if test_list[0] != test_list[1]:  # <-- check if first element should belong to result
    res_list.append(test_list[0])  
else:
    if test_list[1] != test_list[2]:
        count += 1
#print(test_list[1:-1])
for i in range(len(test_list[1:-1])):  # Here we use input list, but without first and last element.
    print(test_list[i], test_list[i+1], test_list[i+2])
    if test_list[i+1] == test_list[i+2] or test_list[i+1] == test_list[i]:
        if (test_list[i+1] != test_list[i+2]):
            count +=1
        continue
    else:
        res_list.append(test_list[i+1])

if test_list[-2] != test_list[-1]:  # <-- check if last element should belong to result
    res_list.append(test_list[-1])
else:
    count+=1

print(res_list, count)



