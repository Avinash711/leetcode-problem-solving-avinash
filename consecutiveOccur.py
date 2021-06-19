'''
count the consecutive occurrence when consecutive occurrence is more than 2 included
00100
o/p
00, 00

ip 01100011
o/p 11,000,11 (3 consecutive terms)
'''

str = '000110000111000' # 000 11 0000 111 000
count = 0
for i in range(len(str)-1-1): # for ist and middle element occurrence
    if str[i] != str[i+1]:
        continue
    else: # when atleast one consecutive occurency
        print(str[i], str[i+2]) # at i and i+2 element transisiton will happen
        if str[i] != str[i+2]: # increasing count when transition occurred
                              # multiple occurence is considered single seq
            count += 1
#for last element
if str[-1] == str[-2]:
    count +=1

print(count)

