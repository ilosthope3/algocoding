import sys



if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    ledge, redge = 0
    l,r = min(k, n-k+1), max(k, n-k+1)
    score = 0
    while n >= k:
      
      if vals[l] > vals[r]:
        score += vals[l]
        vals[l] = 0
        l -=1
        if l < ledge:
          while vals[ledge] == 0:
            ledge += 1
            r += 1
        
    
    
    
    # out.append(calc(vals))
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")