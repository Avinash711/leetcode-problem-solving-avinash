'''
count consecutive seq or occurence
i/p:
101001011
as can be seen 00 count 1
111 count 1
total = 2
**NOTE** valid for only two consecutive occurrences
'''

str = "0010111"
count = 0
for i in range(len(str)-1):
    if str[i] == str[i+1]:
        print(str[i], str[i+1])
        count += 1
print(count)