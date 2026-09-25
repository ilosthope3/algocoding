
def main():
  _ = [int(i) for i in input().split()]
  a = sorted([int(i) for i in input().split()])
  b = sorted([int(i) for i in input().split()])
  c = sorted([int(i) for i in input().split()])

  pa, pb, pc = 0, 0,0
  print()
  while pc < len(c):
    print(a[pa], b[pb], c[pc], '              ', pa, pb, pc)
    if a[pa] + b[pb] == c[pc]:
      
      if pa+1 == len(a) and pb+1 == len(b):
        if pc+1 == len(c):
          return True
        return False
      elif pb+1 == len(b):
        pa += 1
      elif pa+1 == len(a):
        pb += 1
      else:
        if a[pa+1] + b[pb] <= b[pb + 1] + a[pa]:
          pa += 1
        else:
          pb += 1
      pc+=1
    else:
      return False

  return False



if __name__ == "__main__":
  if main():
    print("YES")
  else:
    print("NO")
