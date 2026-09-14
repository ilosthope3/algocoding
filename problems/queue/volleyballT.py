from algocoding import Queue





def main():
  n = int(input())
  q = Queue([int(i) for i in input().split()])
  n = int(input())
  k = [int(input()) for i in range(n)]
  r = ['' for i in range(n)]

  t1 = q.pop()
  t2 = q.pop()
  c = 1
  m = max(k)
  while c <= m:

    if c in k:
      r[k.index(c)] = f"{t1} {t2}"

    q.push(min(t1,t2))
    t1 = max(t1, t2)
    t2 = q.pop()
    
    c+=1
  for i in r:
    print(i)
  



if __name__ == "__main__":
  main()