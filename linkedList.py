class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next
            print()

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def add_after(self, data, x):
        n = self.head
        if n is None:
            print("List is empty!")
            return
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node with data", x, "not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node with data", x, "not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            self.head = self.head.next


    def delete_end(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next is None:
            # Only one node
            self.head = None
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None


    def delete_by_value(self, x):
        if self.head is None:
            print("List is empty!")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("Node with value", x, "not found!")
        else:
            n.next = n.next.next



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.next
            print("None")



    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Node with data", x, "not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node with data", x, "not found!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

    def delete_by_value(self, x):
        if self.head is None:
            print("List is empty!")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("Node with value", x, "not found!")
        else:
            n.next = n.next.next


# -------------------------------
# Test the linked list
# -------------------------------

LL = SinglyLinkedList()

# Add elements
LL.add_end(10)
LL.add_end(20)
LL.add_end(30)
LL.add_begin(5)
LL.print_LL()       # 5 --> 10 --> 20 --> 30 --> None

# Add after and before
LL.add_after(15, 10)
LL.add_before(25, 30)
LL.print_LL()       # 5 --> 10 --> 15 --> 20 --> 25 --> 30 --> None

# Delete nodes
LL.delete_begin()
LL.delete_end()
LL.delete_by_value(20)
LL.print_LL()       # 10 --> 15 --> 25 --> None



def add_after(self, data, x):
    # Start traversing from the head node
    n = self.head

    # Traverse the list to find the node with value x
    while n is not None:
        if x == n.data:      # If current node's data matches x
            break             # Stop searching — we found the node
        n = n.next            # Otherwise, move to the next node

    # If we reached the end (x not found)
    if n is None:
        print("Node with data", x, "not found!")

    # If we found the node containing x
    else:
        # Step 1: Create a new node with the given data
        new_node = Node(data)

        # Step 2: Point new_node.next to the node currently after n
        new_node.next = n.next

        # Step 3: Link n to new_node — so new_node comes after n
        n.next = new_node



def add_before(self, data, x):
    # Case 1: If the list is empty, nothing to do
    if self.head is None:
        print("List is empty!")
        return

    # Case 2: If the first node (head) itself contains the value x
    # We have to insert the new node before the head
    if self.head.data == x:
        new_node = Node(data)      # Create new node
        new_node.next = self.head  # Link new_node to current head
        self.head = new_node       # Update head to the new node
        return

    # Case 3: For other positions (not the first node)
    n = self.head
    # Traverse the list until we find a node such that
    # the *next* node contains the data 'x'
    while n.next is not None:
        if n.next.data == x:       # If next node has data x
            break                  # Stop — we found the correct spot
        n = n.next                 # Otherwise, move forward

    # Case 4: If we reached the end and didn't find x
    if n.next is None:
        print("Node with data", x, "not found!")

    # Case 5: Found x — insert before that node
    else:
        new_node = Node(data)         # Create a new node
        new_node.next = n.next        # Link new node to the node containing x
        n.next = new_node             # Link previous node (n) to new node



#  DLL


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head   # new_node’s next → old head
            self.head.prev = new_node   # old head’s prev → new_node
            self.head = new_node        # update head to new_node


def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node          # if list empty, new node becomes head
        else:
            n = self.head
            while n.next is not None:     # go to the last node
                n = n.next
            n.next = new_node             # last node → new node
            new_node.prev = n             # new node → back to last node


def add_after(self, data, x):
    # Case 2: Traverse to find node with value x
    n = self.head
    while n is not None:
        if x == n.data:
            break
        n = n.next

    # Case 3: If node not found
    if n is None:
        print("Node with value", x, "not found.")
    else:
        # Case 4: Node found → insert new node after it
        new_node = Node(data)
        new_node.prev = n
        new_node.next = n.next

        # Update the next node’s prev link (if it exists)
        if n.next is not None:
            n.next.prev = new_node

        # Link current node to the new node
        n.next = new_node