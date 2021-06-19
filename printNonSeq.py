'''
from itertools import groupby
test_list = [1, 1, 3, 4, 4, 4, 5,6, 6, 7, 8, 8, 6]
[k for k, g in groupby(test_list) if len(list(g)) == 1]
#[3, 5, 7, 6]
test_list = [1, 1, 3, 4, 4, 4, 5,4,6, 6, 7, 8, 8, 6]
[k for k, g in groupby(test_list) if len(list(g)) == 1]
#[3, 5, 4, 7, 6]
'''
test_list = [1, 1, 3, 4, 4, 4,4,4, 5,6, 6, 7, 8, 8, 8,6]
res_list =[]

if test_list[0] != test_list[1]:  # <-- check if first element should belong to result
    res_list.append(test_list[0])  

for i in range(len(test_list[1:-1])):  # Here we use input list, but without first and last element.
    if test_list[i+1] == test_list[i+2] or test_list[i+1] == test_list[i]:
        continue
    else:
        res_list.append(test_list[i+1])

if test_list[-2] != test_list[-1]:  # <-- check if last element should belong to result
    res_list.append(test_list[-1])
print(res_list)