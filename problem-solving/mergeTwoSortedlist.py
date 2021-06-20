# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        list1 = []
        list2 = []
        dummy = cur = ListNode(0)
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        print("-----",list1, list2)
        
        
        for ele in list2:
            list1.append(ele)
            
        
        list1 = sorted(list1)
        print("----------",list1)
        for i in list1:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return cur.next
        
##formed the driver code
if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]

    dummy = cur = ListNode(0)
    for i in l1:
        dummy.next = ListNode(i)
        dummy = dummy.next

    dummy2 = cur2 = ListNode(0)
    for j in l2:
        dummy2.next = ListNode(j)
        dummy2 = dummy2.next

    #passing the two list
    obj = Solution()
    res = obj.mergeTwoLists(cur.next, cur2.next)

    while res:
        print(res.val, end= " ")
        res = res.next
                