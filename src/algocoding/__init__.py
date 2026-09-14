


class Stack:
  def __init__(self,arr=[]):
    self._items = arr

  def pop(self):
    return self._items.pop()

  def push(self,item):
    self._items.append(item)

  def peek(self):
    return self._items[-1]

  def isEmpty(self):
    return len(self._items) == 0

  def show(self):
    return self._items

  @property
  def length(self):
    return len(self._items)

class Queue(): # problem specific return system
  def __init__(self, arr = None):
    self._items = [] if arr == None else arr
    self._head = 0


  def push(self, n):
    self._items.append(n)
    return 'ok'
  
  def pop(self):
    if self.size != 0:
      self._head += 1
      return self.items[self._head-1]
    else:
      return 'error'

  def clear(self):
    self._items = []
    self._head = 0
    return 'ok'

  def insertMiddle(self, n):
    mid = self._head + ((self.size+1)//2)
    r = self.size

    while r> mid:
      self._items[r] = self._items[r-1]
    self._items[mid] = n

  @property
  def items(self):
    return self._items

  @property
  def size(self):
    return len(self._items)-self._head

  @property
  def front(self):
    if self.size != 0:
      return self._items[0]
    else: 
      return 'error'
  
class Deque():
  def __init__(self, arr=None, c=100):
    self._items = [None]*c + ([] if arr == None else arr)
    self._head = c

  def popleft(self):
    self._head += 1
    return self._items[self._head-1]

  def popright(self):
    return self._items.pop()

  def pushright(self,n):
    self._items.append(n)

  def pushleft(self, n):
    self._head -= 1
    self._items[self._head] = n

  @property
  def length(self):
    return len(self._items)-self._head

  @property
  def items(self):
    return self._items
