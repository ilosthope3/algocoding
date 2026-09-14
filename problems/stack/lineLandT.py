




def main():
  n = int(input())
  cities = [int(i) for i in input().split()]
  r = [-1] * n

  stack = []

  for i, cost in enumerate(cities):
    while stack and cities[stack[-1]] > cost:
      j = stack.pop()
      r[j] = i

    stack.append(i)

  print(*r)


if __name__ == "__main__":
  main()
