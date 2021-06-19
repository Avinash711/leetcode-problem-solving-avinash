strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
#strs = ["ab", "a"]
#strs =['a']

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        #print(shortest)
        for i, ch in enumerate(shortest):
            print(i, ch)
            for other in strs:
                print(other)
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
print(longestCommonPrefix(strs))

'''
res_str = ''
        least_lengthy_str = '' # to stop overflow of iteration
        for i in range(len(strs)-1):
            if len(strs[i]) < len(strs[i+1]):
                least_lengthy_str = strs[i]
            else:
                least_lengthy_str = strs[i+1]



    
        for i in range(len(strs)):
            if least_lengthy_str != strs[i]:
                for j in range(len(least_lengthy_str)):
                    #print(strs[i][j], least_lengthy_str[j])
                    if least_lengthy_str[j] == strs[i][j]:
                        res_str += least_lengthy_str[j]
                    else:
                        break

        if res_str != "":
            first = res_str[0]
            ind = 0
            if len(res_str) > 1:
                for i in range(1,len(res_str)):
                    if res_str[i] == first:
                        ind_last = i
                res_str = res_str[i-1:]
            else:
                res_str = res_str[0]
        if len(strs) == 1:
            return strs[0]
        return res_str

        '''