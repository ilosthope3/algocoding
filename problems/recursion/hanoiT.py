



def move(a,b,n):
  if n != 0:
    for i in [1,2,3]:
      if i not in (a,b):
        free = i
    
    move(a,free,n-1)
    print(n,a,b)
    move(free, b, n-1)


if __name__ == "__main__":
  n = 2
  move(1,3, n)