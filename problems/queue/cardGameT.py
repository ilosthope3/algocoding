class Queue(): # problem specific return system
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
  


def game(p1, p2 :Queue) -> str:
  counter = 0
  while (p1.size * p2.size != 0):
    if counter >= 10**6:
      return "botva"
    counter += 1
    c1 = p1.pop()
    c2 = p2.pop()
    if( c1*c2 == 0) and (c1 + c2 == 9):
      if c1 == 0:
        p1.push(c1)
        p1.push(c2)
      else:
        p2.push(c1)
        p2.push(c2)
    else:
      if c1 > c2:
        p1.push(c1)
        p1.push(c2)
      else:
        p2.push(c1)
        p2.push(c2)
  r = "first" if p2.size == 0 else "second"
  return f"{r} {counter}"

def main():
  p1 = Queue([int(i)for i in input().split()])
  p2 = Queue([int(i)for i in input().split()])
  print(game(p1, p2))


if __name__ == "__main__":
  main()