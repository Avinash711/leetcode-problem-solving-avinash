'''
count number of occurrence of substring 
'''

def subString(str_data, sub):
    #print(len(str_data)-len(sub)+1)
    count = 0
    for i in range(len(str_data)):
    #for i in range(len(str_data)-len(sub)+1): # optimized loop length
        if str_data[i:i+len(sub)] == sub:
            count += 1
            print(f"found at {i} {i+1}")
    print(count)


subString("acbccaacdc", "ac")
        