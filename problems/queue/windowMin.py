import sys





def main():
  [n, w] = list(map(int, input().split()))
  v = list(map(int, input().split()))

  currMin = min(v[0:w])
  deck = []
  l = 0
  r = 0
  while r-l!=w:
    if not deck:
      deck.append(r)
      r+=1
    else:
      if deck[-1] > v[r]:
        deck.pop() 
      deck.append(r)
      r+=1




if __name__ == '__main__':
    main()
