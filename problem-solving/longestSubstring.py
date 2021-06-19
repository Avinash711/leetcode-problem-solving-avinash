
length=0
startIndex=0
longestSubstring=[]
s = 'aabcaad'
for i in range(len(s)):
    if s[i] in longestSubstring:
        if length<len(longestSubstring):
            length=len(longestSubstring)
        longestSubstring=longestSubstring[longestSubstring.index(s[i])+1:]
        print(s[i],longestSubstring, length)
        longestSubstring.append(s[i])
        #print(longestSubstring)
    else:
        longestSubstring.append(s[i])
if length<len(longestSubstring):
            length=len(longestSubstring)
print(length)