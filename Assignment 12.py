'''
Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL
'''

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        slow, fast = head, head
        mid = None

        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next

        mid.next = mid.next.next

        return head
    
    
    
    
'''
Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.
'''

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        walker = runner = head
        
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker == runner: return True
        
        return False



'''
Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if (not head):
            return False

        # count nodes
        pCounter = head
        countNodes = 0
        while (pCounter):
            countNodes += 1
            pCounter = pCounter.next
        
        # add alements to list
        p1 = head
        p2 = head
        elements = []
        for i in range(countNodes // 2):
            elements.append(p2.val)
            p2 = p2.next
        
        if (countNodes % 2 != 0):
            p2 = p2.next
        
        # compare last element and current value
        while (p2):
            if (not elements or p2.val != elements.pop()):
                return False
            p2 = p2.next
        return True
    
    
    
'''
Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie
'''

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node


	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next

	def skipMdeleteN(self, M, N):
		curr = self.head
		
		while(curr):
			
			for count in range(1, M):
				if curr is None:
					return
				curr = curr.next
					
			if curr is None :
				return

			
			t = curr.next
			for count in range(1, N+1):
				if t is None:
					break
				t = t.next
	
			
			curr.next = t
			
			curr = t

llist = LinkedList()
M = 2
N = 3
llist.push(10)
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("M = %d, N = %d\nGiven Linked List is:" %(M, N))
llist.printList()
print()

llist.skipMdeleteN(M, N)

print ("\nLinked list after deletion is")
llist.printList()




'''
Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.
'''

class Node(object):
	def __init__(self, data:int):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		
	def push(self, new_data:int):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
	def printList(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next
			
	def merge(self, p, q):
		p_curr = p.head
		q_curr = q.head
		while p_curr != None and q_curr != None:

			p_next = p_curr.next
			q_next = q_curr.next
			q_curr.next = p_next 
			p_curr.next = q_curr 
			q_curr = q_next
			q.head = q_curr

llist1 = LinkedList()
llist2 = LinkedList()

llist1.push(3)
llist1.push(2)
llist1.push(1)
llist1.push(0)

for i in range(8, 3, -1):
	llist2.push(i)

print("First Linked List:")
llist1.printList()

print("Second Linked List:")
llist2.printList()

llist1.merge(p=llist1, q=llist2)

print("Modified first linked list:")
llist1.printList()

print("Modified second linked list:")
llist2.printList()



