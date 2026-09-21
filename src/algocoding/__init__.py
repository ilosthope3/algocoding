


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

class MaxHeap():
  def __init__(self, arr=None):
    self._items = [] if arr == None else sorted(arr)

  def pop(self):
    return self._items.pop()
  
  @property
  def length(self):
    return len(self._items)

  @property
  def front(self):
    if self.length != 0:
      return self._items[-1]
    else: 
      return None

  @property
  def items(self):
    return self._items

  @property
  def min(self):
    return self._items[0]

  def push(self, n):

    def findIndex(l,r):
      if l == r:
        return l
      else:
        m = (l+r)//2
        if n <= self._items[m]:
          return findIndex(l, m)
        else:
          return findIndex(m+1,r)

    i = findIndex(0,self.length)

    self._items.insert(i, n)

class MinHeap(): 
  def __init__(self, arr=None):
    self._items = [] if arr == None else arr

  def pop(self):
    if self.length > 0:
      res = self._items[0]
      curr = self._items.pop()
      if self.length == 0:
        return res
      i = 0
      while True:
        l = 2 * i + 1
        r = l + 1 
        c = l
        
        if l >= self.length:
          break

        if r < self.length and self._items[r] < self._items[l]:
          c = r

        if self._items[c] >= curr:
          break

        self._items[i] = self._items[c]
        i = c

      self._items[i] = curr

      return res
    return None
  
  @property
  def length(self):
    return len(self._items)

  @property
  def front(self):
    if self.length != 0:
      return self._items[0]
    else: 
      return None

  @property
  def items(self):
    return self._items

  def push(self, n):
    self._items.append(n)

    i = self.length - 1

    while i > 0:
      par = (i - 1) // 2
      if self._items[par] <= n:
        break

      self._items[i] = self._items[par]
      i = par

    self._items[i] = n
    
