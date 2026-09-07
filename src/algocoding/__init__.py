


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

  @property
  def show(self):
    return self._items

  @property
  def length(self):
    return len(self._items)

  