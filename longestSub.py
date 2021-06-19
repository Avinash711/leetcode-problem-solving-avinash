s = 'aabcaad'
if not s:
    print( 0)
        
lensub = [1] * len(s)
for i in range(len(s) - 2, -1, -1):
    if s[i] not in s[i+1: i+1+lensub[i+1]]:
        lensub[i] = lensub[i+1] + 1
    else:
        sindex = s[i+1: i+1+lensub[i+1]].index(s[i])
        lensub[i] = sindex + 1
        
print(max(lensub))