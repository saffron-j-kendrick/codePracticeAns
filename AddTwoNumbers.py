# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # linked lists
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node

            return prev
        def listToInt(head: ListNode) ->list[int]:
            result = []
            while head:
                result.append(head.val)
                head = head.next
            return int(''.join(map(str, result)))

        def intToList(num: int) -> ListNode:
            head = ListNode()
            current = head
            for digit in str(num):
                current.next = ListNode(int(digit))
                current = current.next
            return head.next

        
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        l1 = listToInt(l1)
        l2 = listToInt(l2)

        total = l1 + l2

        total = intToList(total)
        total = reverseList(total)
    

        return total


    
if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))

