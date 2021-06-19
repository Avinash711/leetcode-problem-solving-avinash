dup = {}
str = 'cca'
count = 0
for i in str:
    if i not in dup:
        dup[i] = 1   
    else:
        count += 1
        break
if count :
    print('does contain duplicate')
else:
    print('doesnot contian duplicate')
