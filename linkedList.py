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


def add_before(self, data, x):
    if self.head is None:
        print("List is empty.")
        return

    # Case 1: insert before head
    if self.head.data == x:
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return

    # Case 2: insert before a middle or last node
    n = self.head
    while n.next is not None:
        if n.next.data == x:
            break
        n = n.next

    if n.next is None:
        print("Node with value", x, "not found.")
    else:
        new_node = Node(data)
        new_node.prev = n
        new_node.next = n.next
        n.next.prev = new_node
        n.next = new_node

def delete_begin(self):
    if self.head is None:
        print('msg')
        return
    if self.head.next is None:
        self.head = None
        return
    else:
        self.head = self.head.next
        self.head.prev = None

def delete_end(self):
    if self.head is None:
        print('msg')
        return
    if self.head.next is None:
        self.head = None
        return
    n = self.head
    while n.next is not None:
        n = n.next
    n.prev.next = None


def delete_by_value(self, x):
    # Case 1: If the list is empty, nothing to delete
    if self.head is None:
        print("List is empty!")
        return

    # Case 2: If there's only one node
    if self.head.next is None:
        if self.head.data == x:
            self.head = None           # Delete the only node
        else:
            print("Node with value", x, "not found!")
        return

    # Case 3: If the node to delete is the head node
    if self.head.data == x:
        self.head = self.head.next     # Move head forward
        self.head.prev = None          # Remove backward link
        return

    # Case 4: Traverse the list to find the node containing x
    n = self.head
    while n is not None and n.data != x:
        n = n.next

    # Case 5: If node with value x is not found
    if n is None:
        print("Node with value", x, "not found!")
        return

    # Case 6: If the node to delete is the last node
    if n.next is None:
        n.prev.next = None             # Remove last node
        return

    # Case 7: Node is in the middle
    n.prev.next = n.next               # Connect previous node to next node
    n.next.prev = n.prev               # Connect next node back to previous node


def delete_by_value(self, x):

    if self.head is None:
        print("List is empty!")
        return

    if self.head.next is None:
        if self.head.data == x:
            self.head = None
        else:
            print("Node with value", x, "not found!")
        return

    if self.head.data == x:
        self.head = self.head.next
        self.head.prev = None
        return


    n = self.head
    while n is not None and n.data != x:
        n = n.next

    if n is None:
        print("Node with value", x, "not found!")
        return

    if n.next is None:
        n.prev.next = None
        return

    n.prev.next = n.next
    n.next.prev = n.prev

def count_number_frequencies(arr):
    frequency_map = {
    }
    for number in arr:
        if number in frequency_map:
            frequency_map[number] += 1
        else:
            frequency_map[number] = 1
    return frequency_map

my_array = [10, 5, 20, 10, 8, 5, 20, 10, 8, 20, 20]
counts = count_number_frequencies(my_array)

# print(f"Original Array: {my_array}")
# print("-" * 30)
# print("Number Frequencies:")

for number, count in counts.items():
    print(f"The number {number} occurs {count} time(s).")


def functionnumOfOccurrences(Head, value):
    count = 0
    current = Head
    while current is not None:
        if current.data == value:
            count = count + 1
        current = current.next
    return count

def is_identical(list1, list2):

  identical = True
  if list1.size!=list2.size:
    return False
  else:
    if list1.size!=0 and list2.size!=0:
      current_node1 = list1.head
      current_node2 = list2.head

      while current_node1 is not None:
        if current_node1.data == current_node2.data:
          identical = True
        else:
          identical = False
          return identical
        current_node1 = current_node1.next
        current_node2 = current_node2.next

  return identical

def addNodeBeforeValue(self, givenValue, newValue): # ( self , x , data )
        if self.head is None:
            print("List is empty!")
            print("Not found")
            return

        if self.head.data == givenValue:
            new_node = Node(newValue)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            if current.next.data == givenValue:
                break
            current = current.next

        if current.next is None:
            print("Not found")

        else:
            new_node = Node(newValue)
            new_node.next = current.next
            current.next = new_node


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, v):
        new_node = Node(v)

        # Case 1: Empty list or new node should be first
        if self.head is None or v < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        # Case 2: Insert in middle or end
        current = self.head
        while current.next is not None and current.next.data < v:
            current = current.next

        # Insert new_node after current
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# 🔹 Example usage:
sll = LinkedList()
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(7)
sll.sorted_insert(6)
sll.sorted_insert(5)

sll.display()


def sorted_insert(self, v):

        new_node = Node(v)
        if self.head is None or v < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.data < v:
            current = current.next
        new_node.next = current.next
        current.next = new_node


def reverse(Head):

    current_node = Head
    prev = None
    while current_node is not None :
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
    return prev

def combine(dllA, dllB):
    new_list = DoublyLinkedList()

    # Copy elements from dllA
    current = dllA.head
    while current is not None:
        new_list.append(current.data)
        current = current.next

    # Copy elements from dllB
    current = dllB.head
    while current is not None:
        new_list.append(current.data)
        current = current.next

    return new_list

def countEven(self):
  count=0
  while self.head is not None:
    if self.head.data %2== 0:
      count+=1
    else:
      count=1
    return count


def isSymmetric(self):
        left = self.head
        right = self.tail

        while left is not None and right is not None:
            if left.data != right.data:
                return False
            # Stop when pointers cross or meet
            if left == right or left.next == right:
                break
            left = left.next
            right = right.prev

        return True


def trim(self):
  if self.head is None:
    print('msg')
    return
  while self.head.next is not None:
    if self.head.next.data == 55:
      self.head.next=self.head.next.next.next.next
      self.tail.prev.prev.prev.prev=self.head
  return

def minsquares(x):
  i=0
  sum=0
  while sum < x:
    i+=1
    sum+=i**2
    print(sum)
  return i



k = 50
print(minsquares(k))