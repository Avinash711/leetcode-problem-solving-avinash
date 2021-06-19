# two sum problem
class TwoSum:
    def twoSum(self,lis, target):
        empty = {}
        for ind in range(len(lis)):
            empty[lis[ind]] = ind

        for ind in range(len(lis)):
            if (target - lis[ind]) in empty and ind != empty[target - lis[ind]]:
                return ([ind, empty[target - lis[ind]]]) 


if __name__ == '__main__':
    obj = TwoSum()
    print(obj.twoSum([1,2,3,4,5], 9))


'''
ind != empty[target - lis[ind]]
for lis = [2,3,5]
target is 4
then o/p will be [0, 0] which invalid this this case
'''

