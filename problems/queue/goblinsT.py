class Queue(): # problem specific return system
  def __init__(self, arr = None, front=0):
    self._items = [None]*front + ([] if arr == None else arr)
    self._head = front


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

  def frontInsert(self, n):
    self._head-=1
    self._items[self._head] = n

  @property
  def items(self):
    return self._items

  @property
  def size(self):
    return len(self._items)-self._head

  @property
  def front(self):
    if self.size != 0:
      return self._items[self._head]
    else: 
      return 'error'
  



def main():
  

  n = int(input())
  left = Queue([])
  right = Queue([], n)
  for _ in range(n):
    i = input()
    if i[0] == "+":
      right.push(i.split()[1])
      if right.size > left.size:
        left.push(right.pop())
    elif i[0] == "-":
      print(left.pop())
      if right.size > left.size:
        left.push(right.pop())
    else:
      if left.size == right.size:
        left.push(i.split()[1])
      else:
        right.frontInsert(i.split()[1])

  


if __name__ == "__main__":
  main()