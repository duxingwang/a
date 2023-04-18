# a
hi
hi
ls
ls
import json
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        #dummy = head
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next

def stringToListNode(input):
    print(input)
    #numbers = json.loads(input)
    numbers = [bb for bb in input.split()]
    #print(numbers,"*1")
    #numbers = input
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptra = ptr
    #print()
    print(listNodeToString(ptra),"*3")
    #print(listNodeToString(ptra),"*3")
    ptr = dummyRoot.next
    #print()
    #print(listNodeToString(ptr),"*4")
    return ptr



def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    #return result[:-2]
    return result



def main():
    while True:
        try:
            head = stringToListNode(str([1,2,3,4]))
            n = 2
            ret = Solution().removeNthFromEnd(head, n)
            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

#if __name__ == '__main__':
#    main()
main()
