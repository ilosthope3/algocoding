import sys


def fullPath(n):
  passed = []
  r = sum([int(i)**2 for i in str(n)])
  while r not in passed:
    passed.append(r)
    r = sum([int(i)**2 for i in str(r)])
  
  passed.append(r)
  return passed
    

def calc(vals):
  count = 0
  
  hashset = {}
  for i in vals:
    hashset[i] = hashset.get(i, 0) + 1
  # print(hashset)
  new = []
  for key,n in hashset.items():
    count+= n*(n-1)//2
    new.append(key)
  # print(count)
    
  # print(new)
  paths = [fullPath(i) for i in new]
  # for i in paths: print(i)
  # for i in paths: print(i)
  
  for i in range(len(paths)-1):
    for j in range(i+1, len(paths)):
      p1 = paths[i]
      p2 = paths[j]
    
      
      o1, c1 =p1.index(p1[-1]), p1[p1.index(p1[-1]):-1]
      o2, c2 =p2.index(p2[-1]), p2[p2.index(p2[-1]):-1]
      
      # if c1 == c2: count +=1
      if len(c1) == len(c2):
        if len(c1) != 1:
          d = o2 - o1
          if d >0:
            for _ in range(d):
              c1 = c1[1:] + c1[0]
          else:
            for _ in range(abs(d)):
              c2 = c2[1:] + c2[0]
        
        if c2 == c1:
          count += 1
          
          
        
        
  return count



# 1
# 3
# 42 20 2


  
if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    sys.stdin.readline()
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()]
    out.append(calc(vals))
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")