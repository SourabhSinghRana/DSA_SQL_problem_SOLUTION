'''
Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.
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

	def deleteNode(self, key):

		temp = self.head

		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

			return
		prev.next = temp.next

		temp = None

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=' ')
			temp = temp.next

	def removeDuplicates(self):
		temp = self.head
		if temp is None:
			return
		while temp.next is not None:
			if temp.data == temp.next.data:
				new = temp.next.next
				temp.next = None
				temp.next = new
			else:
				temp = temp.next
		return self.head

llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
	"duplicate elements:")
llist.removeDuplicates()
llist.printList()



'''
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).
'''

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=b=ListNode()
        i=0
        z=None
        while head:
            i=i+1
            if i<=k:
                x=head.next
                head.next=z
                z=head
                head=x
            if i==k:
                b.next=z
                while b and b.next:
                    b=b.next
                z=None
                i=0
        zz=None
        while z:
            #Reverse
            g=z.next
            z.next=zz
            zz=z
            z=g
        b.next=zz
        return a.next
   
    
'''
Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.
'''


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev_group = dummy
        while head:
            j, group_end = 1, head #start of group = end after reverse
            while j < k and head.next:
                head = head.next 
                j+=1
            group_start = head #end of group = start after reverse
            next_group = head = head.next #start of next group

            if j != k:  #don't need reverse (not enough nodes)
                break
            prev, cur = None, group_end
            while cur != next_group:
                cur.next, cur, prev = prev, cur.next, cur  

            prev_group.next = group_start
            prev_group = group_end
            group_end.next = next_group

        return dummy.next
    


'''
Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.
'''


class Node:
    def __init__(self, new_data):
        
        self.data = new_data
        self.next = None

def deleteLast(head, x):

    temp = head
    ptr = None
    
    while (temp != None):

        if (temp.data == x):
            ptr = temp    
        temp = temp.next
    
    if (ptr != None and ptr.next == None):
        temp = head
        while (temp.next != ptr):
            temp = temp.next
            
        temp.next = None
    
    if (ptr != None and ptr.next != None):
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next
        
    return head
    
def newNode(x):

    node = Node(0)
    node.data = x
    node.next = None
    return node

def display(head):

    temp = head
    if (head == None):
        print("NULL\n")
        return
    
    while (temp != None):
        print( temp.data, end = " ")
        temp = temp.next
    
    print("NULL")

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(7)
head.next.next.next = newNode(5)
head.next.next.next.next = newNode(2)
head.next.next.next.next.next = newNode(10)

print("Created Linked list: ", end = '')
display(head)

# Pass the address of the head pointer
head = deleteLast(head, 2)
print("List after deletion of 4: ", end = '')

display(head)







'''
Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

def deleteNode(head_ref, del_):
	if (head_ref == None or del_ == None):
		return
	if (head_ref == del_):
		head_ref = del_.next
	if (del_.next != None):
		del_.next.prev = del_.prev
	if (del_.prev != None):
		del_.prev.next = del_.next
		
	return head_ref

def deleteNodeAtGivenPos(head_ref,n):
	if (head_ref == None or n <= 0):
		return

	current = head_ref
	i = 1
	while ( current != None and i < n ):
		current = current.next
		i = i + 1
	if (current == None):
		return
	deleteNode(head_ref, current)
	return head_ref

def push(head_ref, new_data):

	new_node = Node(0)

	new_node.data = new_data

	new_node.prev = None
	new_node.next = (head_ref)

	if ((head_ref) != None):
		(head_ref).prev = new_node

	(head_ref) = new_node
	
	return head_ref

def printList(head):

	while (head != None) :
		print( head.data ,end= " ")
		head = head.next
	
head = None

head = push(head, 5)
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)

print("Doubly linked list before deletion:")
printList(head)

n = 2
head = deleteNodeAtGivenPos(head, n)

print("\nDoubly linked list after deletion:")

printList(head)
