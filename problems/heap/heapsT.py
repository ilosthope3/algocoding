from algocoding import Heap #deprecated to maxheap



def main():
  h = Heap()
  n = int(input())
  for _ in range(n):
    i = input()
    if i[0] == "1":
      print(h.pop())
    else:
      h.push(int(i.split()[1]))




if __name__ == "__main__":
  main()