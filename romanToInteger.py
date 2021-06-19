value = {"I":1, "V":5, "X": 10, "L":50, "C":100, 
                 "D": 500, "M":1000}
s = "MCDLXXVI"
res_sum = 0

for i in range(len(s)-1):
    #print(value[s[i]],value[s[i+1]])
    if value[s[i]] < value[s[i+1]]:
        print()
        res_sum -= value[s[i]] 
    else:
        res_sum += value[s[i]]
        
print(res_sum + value[s[-1]])
    