'''
Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(head is None or head.next is None):
            return None
        
        fast = head
        slow = head
        
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                temp = head
                while(temp != slow):
                    temp = temp.next
                    slow = slow.next
                return slow    
                
            
            
        return None  
    
    





'''
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.
'''




# A Linked List Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(msg, head):
 
    print(msg, end='')
    while head:
        print(head.data, end=' —> ')
        head = head.next
    print('None')
 
 
# Function to reverse a given linked list
def reverse(head):
 
    prev = None
    current = head
 
    # traverse the list
    while current:
        # tricky: note the next node
        next = current.next
 
        # fix the current node
        current.next = prev
 
        # advance the two pointers
        prev = current
        current = next
 
    # fix the head pointer to point to the front
    head = prev
    return head
 
 
# Function to add a single-digit number to a singly linked list
# whose nodes represent digits of a number
def addDigit(head, digit):
 
    # empty list
    if head is None:
        return Node(digit)
 
    # reverse the linked list
    head = reverse(head)
 
    # initialize carry with the given digit
    carry = digit
 
    # traverse the reversed list
    curr = head
    while carry > 0:
 
        # get a sum of the current node and carry
        total = curr.data + carry
 
        # update value of the current node with the single-digit sum
        curr.data = total % 10
 
        # set carry for the next node
        carry = total // 10
 
        # break if the current node is the last
        if curr.next is None:
            break
 
        # move to the next node
        curr = curr.next
 
    # add a new node at the end of the linked list if there is any carry left
    if carry > 0:
        curr.next = Node(carry)
 
    # reverse the list again to restore the original order
    head = reverse(head)
    return head
 
 
if __name__ == '__main__':
 
    head = Node(9)
    head.next = Node(9)
    head.next.next = Node(9)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(3)
 
    digit = 7
 
    printList('Original linked list: ', head)
    head = addDigit(head, digit)
    printList('Resultant linked list: ', head)
    
    
    
'''
You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**

Construct a copy of the given list. The copy should consist of exactly **N** new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes **X** and **Y** in the original list, where **X.arb** **-->** **Y**, then for the corresponding two nodes **x** and **y** in the copied list, **x.arb --> y.**

Return the head of the copied linked list.
'''


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)

        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
    
    
    
    
    
'''
Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.
'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        
        odd,even = head, head.next
        pointer1,pointer2 = odd,even
        prev = None
        while(pointer1 != None and pointer2 != None):
            pointer1.next = pointer2.next
            prev = pointer1
            pointer1 = pointer1.next
            if pointer1 == None:
                pointer2.next = None
            else:
                pointer2.next = pointer1.next
            pointer2 = pointer2.next
        if pointer1 == None:
            prev.next = even
        else:
            pointer1.next = even
        return odd
    
    
    
    '''
    You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.
    '''
    
    

class Solution:
    def nextLargerNodes(self, n: Optional[ListNode]) -> List[int]:
        head = []
        while(n):
            head.append(n.val)
            n = n.next
        res = [0] * len(head)   
        stack  =[]
        for i in range(len(head)):
            while stack and head[stack[-1]] < head[i]:
                res[stack.pop()] = head[i]
            stack.append(i)
        return res
    
    
    
    
    
    
'''
Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)
'''


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(0, head)
        
        d = {0: fake}
        
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            d[prefix_sum] = head
            head = head.next
            
        head = fake
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            head.next = d[prefix_sum].next
            head = head.next
            
        return fake.next