# **********************************************
# 160. Intersection of Two Linked Lists
# hash/arithmetic method
# **********************************************

# single list definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# method 1: hash table,O(m + n)
def getIntersectionNode(headA: Node, headB: Node) -> [Node]:
    a_node = set()
    while headA is not None:
        a_node.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in a_node:
            return headB
        headB = headB.next
    return None

# method 2: arithmetic method, a+c+b = b+c+a, O(m + n)
def getIntersectionNode1(headA: Node, headB: Node) -> [Node]:
    p1,p2 = headA,headB
    print(p1.data,p2.data)
    while p1 != p2:
        p1 = headB if p1 == None else p1.next
        p2 = headA if p2 == None else p2.next
    return p1

# **********************************************
# 206. Reverse Linked List
# refer to: https://www.geeksforgeeks.org/reverse-a-linked-list/
# **********************************************
# class Node:
#        def __init__(self, data):
#               self.data = data
#               self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self,data):
        # add new node from the head,change head pointer to the newest one
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while temp:
           print(temp.data)
           temp = temp.next
llst = LinkedList()
llst.push(4)
llst.push(1)
llst.push(8)
llst.push(4)
llst.push(5)
# [4,1,8,4,5]
llst.reverse()
llst1 = LinkedList()
llst1.push(10)
llst1.push(6)
llst1.push(1)
llst1.push(8)
llst1.push(4)
llst1.push(5)
llst1.reverse()
# llst1.printList()
# print(llst.head.data,llst1.head.data)

getIntersectionNode(llst.head,llst1.head)

# **********************************************
# 206. Reverse Linked List (shorten edition)
# **********************************************

def reverseList( head: [Node]) -> [Node]:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
# **********************************************
# 19. Remove Nth Node From End of List
# two pointers, arithmatic calculation
# e.g. k = L-n, the order L-n = the reverse order n
# **********************************************
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: [ListNode], n: int) -> [ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        # edge case
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
