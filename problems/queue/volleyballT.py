class Queue():
  def __init__(self, arr=None):
    self._items = [] if arr is None else arr
    self._head = 0

  def push(self, n):
    self._items.append(n)

  def pop(self):
    if self._head < len(self._items):
      item = self._items[self._head]
      self._head += 1
      return item

  @property
  def size(self):
    return len(self._items) - self._head

  @property
  def front(self):
    return self._items[self._head]

  @property
  def items(self):
    return self._items[self._head:]




def main():
  n1 = int(input())
  q = Queue([int(i) for i in input().split()])
  n = int(input())
  k = [int(input()) for i in range(n)]

  t1 = q.pop()
  t2 = q.pop()
  c = 1

  # 1 2 3 4
  # 1 2

  # 2  3 4 1
  # 2 3

  # 3  4 1 2
  # 3 4

  # 4  1 2 3

  answers = {}
  while c <= (n1 -1): 

    answers[c]= f"{t1} {t2}"

    q.push(min(t1,t2))
    t1 = max(t1, t2)
    t2 = q.pop()
    
    c+=1

  
  
  rem = [t2] + q.items 
  for i, item in enumerate(k):
      if item<= n1-1:
        print(answers[item])
      else:
        print(f"{t1} {rem[(item-n1)%(n1-1)]}")

if __name__ == "__main__":
  main()