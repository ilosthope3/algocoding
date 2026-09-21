from algocoding import MinHeap

def main():
  _ = input()
  h = MinHeap(list(map(int, input().split())))
  r = 0
  while h.length > 1:
    res = h.pop() + h.pop()
    r += res*0.05
    h.push(res)
  print(f"{r:.2f}")




if __name__ == "__main__":
  main()