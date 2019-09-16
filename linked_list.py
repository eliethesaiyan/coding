'''
you are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contains a single digit. Add the two numbers and return it as a linked list.
Example
Input(2->4->3)+(5->6->4)
Output: 7->0->8
Explanation: 342+465 = 807
'''
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def add_two_numbers(self,l1,l2, c=0):
        res =l1.next.next.val + l2.next.next.val
        if res>9:
           res = 10-res
           l1.next.val +=1 
        ln = ListNode(res)
        res2 =l1.next.val + l2.next.val
        if res2>9:
           res2 = 10-res2
           l1.val+=1
        ln.next = ListNode(res2)
        res3 = l1.val + l2.val
        ln.next.next = ListNode(res3)
        return ln 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result =  Solution().add_two_numbers(l1,l2)

while result: 
    print(result.val) 
    result=result.next
        
