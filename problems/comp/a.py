import sys



def main(k, arr):

  counter = {}
  for i in arr:
    counter[i] = counter.get(i,0) + 1
  r = 0
  for x, count in counter.items():
    y = k-x

    if x == y:
      r += count-1
    elif x < y:
      county = counter.get(y, 0)
      if county > 0:
        r += min(count, county)
  print(r)


if __name__ == "__main__":
  inp = input().split(' ')
  n = int(inp[0])
  k = int(inp[1])
  arr = [int(i) for i in input().split(' ')]
  main(k, arr)