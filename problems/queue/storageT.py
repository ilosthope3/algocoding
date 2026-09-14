from algocoding import Queue




class Car():
  def __init__(self, id_, dire, time):
    self._dir = dire
    self._time = time
    self._id = id_

  @property 
  def dir(self):
    return self._dir

  @property
  def time(self):
    return self._time

  @property
  def id(self):
    return self._id


def isEmpty(arr):
  r = 0
  for i in arr:
    r+=i.size
  return r==0

def reorder(order):
  def pair_order(arr):
    [x,y] = arr
    if y == x % 4 + 1:
        return [y, x]
    return [x, y]
  sub = [x for x in range(1, 5) if x not in order]

  return pair_order(order) + pair_order(sub)


def main():
  crossroads = [Queue([]) for i in range(4)]

  n = int(input())
  order = [int(i) for i in input().split()]
  angled = abs(order[0] - order[1]) != 2
  order = reorder(order)
  for k in range(n):
    [d,t] = [int(i) for i in input().split()]
    c = Car(k, d, t)
    crossroads[d-1].push(c)


  def isValid(q, t):
    if q.size == 0:
      return False
    if t < q.front.time:
      return False
    return True

  currTime = 1
  index = 0
  # for i in crossroads:
  #   for j in i.items:
  #     print(j.dir, j.time, end="    ")
  #   print()
  # print()
  r = [0 for _ in range(n)]
  while not isEmpty(crossroads):
    
    # print(index, currTime, isValid(crossroads[order[index]-1], currTime))
    # time.sleep(1)
    if isValid(crossroads[order[index]-1], currTime):
      # print(index)
      car = crossroads[order[index]-1].pop()
      r[car.id] = currTime
      if (not angled) and (index==0 or index ==2) and isValid(crossroads[order[index+1]-1], currTime):
        car = crossroads[order[index+1]-1].pop()
        r[car.id] = currTime
      currTime += 1
      index = 0
    else:
      index += 1
      
    if index == 4:
      index = 0
      currTime+=1
  for i in r:
    print(i)
        

if __name__ == "__main__":
  main()