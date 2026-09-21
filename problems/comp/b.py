

def main(s):
  k = s.count("/")
  if k == 0: return "Impossible"
  if s.count("<") != 2*k:
    return "Impossible"
  if s.count(">") != 2*k:
    return "Impossible"
  c = {}
  su = 0
  for i in s:
    if i>="a" and i<="z":
      c[i] = c.get(i,0) +1
      su += 1 

  if su < 2*k: return "Impossible"


  pairs = []
  for i, v in c.items():
    if v%2 == 1:
      return "Impossible"
    for _ in range(v//2):
      pairs.append(i)
  r = ""
  
  for i in range(k):
    if i!= k-1:
      r = f"<{pairs[i]}>{r}</{pairs[i]}>"
    else:
      v = "".join(pairs[i::])
      r = f"<{v}>{r}</{v}>"
  return r




if  __name__ == "__main__":
  s = input()
  print(main(s))