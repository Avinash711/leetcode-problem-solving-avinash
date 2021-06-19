# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        result = curr = ListNode(0)
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        #print(l1_list, l2_list)
        l1_list_str = ''.join(map(str, l1_list[::-1]))
        l2_list_str = ''.join(map(str, l2_list[::-1]))
        print(l1_list_str, l2_list_str)
        res = list(str((int(l1_list_str) + int(l2_list_str))))[::-1]
        #print(res)
        for i in res:
            #print(i)
            result.next = ListNode(i)
            result = result.next
            #print(result)
        return curr.next

'''
if __name__ == '__main__':
    data = ListNode(2,)
    sol = Solution()
'''
