import sys

  
if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    out1 = []
    _, k = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    r = []
    s = 0
    for i in [int(i) for i in sys.stdin.readline().rstrip().split()]:
      if i%3 == 0 or i%5==0:
        r.append(1)
        s+=1
      else: 
        r.append(0)
      
    out1.append(s)
    
    
    for _ in range(k):
      p, i = [int(i) for i in sys.stdin.readline().rstrip().split()]
      if i%3 == 0 or i%5==0:
        if r[p-1] == 0:
          r[p-1] = 1
          s += 1
      else: 
        if r[p-1] == 1:
          r[p-1] = 0
          s -= 1
    
      out1.append(s)
      # print(r)
      
    out.append(out1)
  
  for out2 in out:
    sys.stdout.write(" ".join(map(str, out2)) + "\n")

