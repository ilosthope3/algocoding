

import sys


class Queue():
  def __init__(self, arr):
    self._items = arr

  def push(self, n):
    self._items.append(n)
    return 'ok'
  
  def pop(self):
    if len(self._items) != 0:
      return self._items.pop(0)
    else:
      return 'error'

  def clear(self):
    self._items = []
    return 'ok'

  @property
  def items(self):
    return self._items

  @property
  def size(self):
    return len(self._items)

  @property
  def front(self):
    if self.size != 0:
      return self._items[0]
    else: 
      return 'error'
  

  

  



def main():
  q = Queue([])
  n = input()
  while n != "exit":
    if n.startswith("push"):
      print(q.push(int(n.split(' ')[1])))
    elif n == "size":
      print(q.size)
    elif n == "front":
      print(q.front)
    elif n == "clear":
      print(q.clear())
    elif n == "pop":
      print(q.pop())

    # print(q.items)
    n = input()
  print("bye")
    

if __name__ == '__main__':
  main()
