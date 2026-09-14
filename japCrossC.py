
def main():
  [m,n] = map(int, input().split())

  matrix = [input() for _ in range(m)]
  rhor = []
  for row in matrix:
    s = row.replace(".", " ").split()
    rhor.append([len(s)] + [len(j) for j in s])

  rver = []
  for i in range(n):
    col = "".join([row[i] for row in matrix])
    s = col.replace(".", " ").split()
    rver.append([len(s)] + [len(j) for j in s])

  for ans in [rhor, rver]:
    for i in ans:
      print(*i)
    print()


if __name__ == '__main__':
    main()
    # s = ".##..##.".replace(".", " ").split()
    # print(s)
