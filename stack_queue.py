# -------------------------------
# Singly Linked List (SLL)
# -------------------------------

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_head(self, value):
        """O(1): add at head (useful for Stack)"""
        node = SLLNode(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def push_tail(self, value):
        """O(1): add at tail (useful for Queue)"""
        node = SLLNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_head(self):
        """O(1): remove from head; raises if empty"""
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return node.data

    def peek_head(self):
        if self.head is None:
            raise IndexError("peek from empty list")
        return self.head.data

    def peek_tail(self):
        if self.tail is None:
            raise IndexError("peek from empty list")
        return self.tail.data

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# -------------------------------
# Doubly Linked List (DLL)
# -------------------------------

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_head(self, value):
        node = DLLNode(value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def push_tail(self, value):
        node = DLLNode(value)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.size += 1

    def pop_head(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return node.data

    def pop_tail(self):
        if self.tail is None:
            raise IndexError("pop from empty list")
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return node.data

    def print_all(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def print_reverse(self):
        cur = self.tail
        while cur:
            print(cur.data)
            cur = cur.prev



# Stack (using SinglyLinkedList)
# LIFO: push/pop at HEAD for O(1)


class Stack:
    def __init__(self):
        self.data = SinglyLinkedList()
        self.size = 0

    def push(self, val):
        self.data.push_head(val)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        self.size -= 1
        return self.data.pop_head()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.data.peek_head()

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def print_all(self):
        self.data.print_all()


# Queue (using SinglyLinkedList)
# FIFO: enqueue at TAIL, dequeue at HEAD for O(1)


class Queue:
    def __init__(self):
        self.data = SinglyLinkedList()
        self.size = 0

    def enqueue(self, val):
        self.data.push_tail(val)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        self.size -= 1
        return self.data.pop_head()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.data.peek_head()

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size



def check_balanced(s):
  mp={ ')' : '(' , ']' : '[' , '}' : '{' }
  stk=Stack()
  for ch in s:
    if ch in '({[':
       stk.push(ch)
    elif ch in mp:
      if stk.isEmpty() or stk.pop() != mp[ch] :
        return False
    else:
      continue
  return stk.isEmpty()
check_balanced('{()}')


def reverse_first_k(q: Queue, k: int) -> None:

    n = len(q)
    if k < 0 or k > n:
        raise ValueError("k must be between 0 and size of the queue")

    stk = Stack()

    # Step 1: Move first k elements into stack
    for _ in range(k):
        stk.push(q.dequeue())

    # Step 2: Pop from stack → enqueue back (reversed order)
    while not stk.isEmpty():
        q.enqueue(stk.pop())


ok = [30, 40, 50, 60, 70, 80, 90]

q = Queue()
for val in ok:
    q.enqueue(val)

reverse_first_k(q, 4)

while not q.isEmpty():
    print(q.dequeue(),end=' ')


# -------------------------------
# Singly Linked List (SLL)
# -------------------------------

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_head(self, value):
        """O(1): add at head (useful for Stack)"""
        node = SLLNode(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def push_tail(self, value):
        """O(1): add at tail (useful for Queue)"""
        node = SLLNode(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_head(self):
        """O(1): remove from head; raises if empty"""
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return node.data

    def peek_head(self):
        if self.head is None:
            raise IndexError("peek from empty list")
        return self.head.data

    def peek_tail(self):
        if self.tail is None:
            raise IndexError("peek from empty list")
        return self.tail.data

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# -------------------------------
# Doubly Linked List (DLL)
# -------------------------------

class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_head(self, value):
        node = DLLNode(value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def push_tail(self, value):
        node = DLLNode(value)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.size += 1

    def pop_head(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return node.data

    def pop_tail(self):
        if self.tail is None:
            raise IndexError("pop from empty list")
        node = self.tail
        self.tail = node.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return node.data

    def print_all(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def print_reverse(self):
        cur = self.tail
        while cur:
            print(cur.data)
            cur = cur.prev


class Stack:
    def __init__(self):
        self.data = SinglyLinkedList()
        self.size = 0

    def push(self, val):
        self.data.push_head(val)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        self.size -= 1
        return self.data.pop_head()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.data.peek_head()

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def print_all(self):
        self.data.print_all()


class Queue:
    def __init__(self):
        self.data = SinglyLinkedList()
        self.size = 0

    def enqueue(self, val):
        self.data.push_tail(val)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        self.size -= 1
        return self.data.pop_head()

    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from empty queue")
        return self.data.peek_head()

    def isEmpty(self):
        return self.size == 0

    def __len__(self):
        return self.size

def shift_top_to_bottom(stk):

    if stk.isEmpty():
        return

    top = stk.pop()
    tmp = []
    while not stk.isEmpty():
       tmp.append(stk.pop())
    stk.push(top)
    while tmp:
      stk.push(tmp.pop())

stack = Stack()
for i in [10, 20, 30, 40, 50]:
    stack.push(i)

shift_top_to_bottom(stack)   # Print the stack after shifting
while not stack.isEmpty():
    print(stack.pop())

def push_sorted(stack,val):
    temp =Stack()
    while not stack.isEmpty() and stack.peek() > val:
        temp.push(stack.pop())
    stack.push(val)
    while not temp.isEmpty():
        stack.push(temp.pop())

stack = Stack()
for i in [10, 20, 30]:
    stack.push(i)

push_sorted(stack,25)
stack.data.print_all()