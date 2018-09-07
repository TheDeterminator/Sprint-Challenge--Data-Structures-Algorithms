class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if not self.head:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail = new_node
        self.tail.set_next(new_node)


  def add_to_head(self, value):
      new_node = Node(value)
      if not self.head:
          self.head = new_node
          self.tail = new_node
      else:
          new_node.next_node = self.head
          self.head = new_node


  def remove_head(self):
    if self.head:
        removed_head = self.head
        self.head = self.head.get_next()
        self.tail = None
        return removed_head.value

  def contains(self, value):
    node_being_searched = self.head #We start by checking the head value
    while node_being_searched:
        if node_being_searched.value == value:
            return True
        node_being_searched = node_being_searched.get_next() #node to be searched updated to next node
    return False

  def get_max(self):
    current_node = self.head
    if not current_node:
        return None

    max_value = current_node.value

    while current_node:
        if current_node.value > max_value:
            max_value = current_node.value

        current_node = current_node.get_next()

    return max_value

  def display(self):
      elems = []
      cur_node = self.head
      while cur_node.get_next():
          elems.append(cur_node.value)
          cur_node = cur_node.get_next()
      elems.append(cur_node.value)
      print(elems)


class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
    self.size += 1

  def dequeue(self):
      if self.size == 0:
          return None
      self.size -= 1
      return self.storage.remove_head()

  def len(self):
    return self.size

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def push(self, item):
        self.storage.add_to_head(item)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.storage.remove_head()

    def display(self):
        return self.storage.display()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = Stack()
    stack.push(self)
    while stack.size > 0:
        current_node = stack.pop()
        if current_node.right:
            stack.push(current_node.right)
        if current_node.left:
            stack.push(current_node.left)
        cb(current_node.value)

  def breadth_first_for_each(self, cb):
      # queue = Queue()
      # queue.enqueue(self)

      queue = []
      queue.append(self)

      while len(queue) > 0:
          current_node = queue.pop(0)
          if current_node.left:
              queue.append(current_node.left)
          if current_node.right:
              queue.append(current_node.right)
          cb(current_node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value

bst = BinarySearchTree(5)

# bst.insert(2)
# bst.insert(3)
# bst.insert(7)
# bst.insert(9)

arr = []
cb = lambda x: print(x)

# bst.depth_first_for_each(cb)

bst.insert(3)
bst.insert(4)
bst.insert(10)
bst.insert(9)
bst.insert(11)
bst.breadth_first_for_each(cb)
