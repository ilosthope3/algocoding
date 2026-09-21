from algocoding import MinHeap

def main():

  n, _ = map(int, input().split())

  blocks = []

  for i in range(1, n + 1):
    l, w = map(int, input().split()) #[l,r] inclsive
    r = l + w - 1

    blocks.append((l, r, i))

  blocks.sort()

  
  free = MinHeap()

  h = [[] for _ in range(n + 1)]
  hp = 0
  for l, r, num in blocks:
    if free.length > 0 and l>= free.front[0]:
        r1, p = free.pop()
        h[p].append(num)
        free.push([r1 + r - l + 1, p])
    else:
      hp += 1
      free.push([r+1,hp])
      h[hp].append(num)
    

  print(hp)
  for i in h:
    if i!= []:
      print(*i, end=" ")
  print()

  


if __name__ == "__main__":
    main()