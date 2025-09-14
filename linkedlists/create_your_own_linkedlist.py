class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    
    def insert_head(self, val):
       new_node = Node(val)
       
       new_node.next = self.head
       self.head = new_node
       self.n += 1

    def append(self, val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.n += 1

    def insert_after(self, after, val):
        new_node = Node(val)

        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return "Item Not Found!"
        
    def clear(self):
        self.head = None
        self.n = 0
        print("LL is Empty!")

    def delete_head(self):
        if self.head == None:
            return "Empty Linked List!"
        self.head = self.head.next
        self.n -= 1

    def delete_tail(self):
        if self.head == None:
            return "Empty LL!"
        
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    def delete_by_val(self, val):
        if self.head == None:
            return "Empty LL!"
        
        if self.head.data == val:
            return self.delete_head()
        
        curr = self.head
        while curr.next != None:
            if curr.next.data == val:
                break
            curr = curr.next
        
        if curr.next == None:
            return "Item Not Found!"
        else:
            curr.next = curr.next.next
            self.n -= 1

    def search(self, val):
        curr = self.head
        pos = 0

        while curr != None:
            if curr.data == val:
                return pos
            curr = curr.next
            pos += 1

        return "Not found!"

    def __getitem__(self, index):
        curr = self.head
        pos = 0

        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        
        return "Invalid Index!"

    def __str__(self):
        curr = self.head
        result = ''

        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        
        return result[:-2]

L = LinkedList()