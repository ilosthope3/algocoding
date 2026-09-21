def main():

  n = int(input())
  p1 = [(int(i), num) for num, i in enumerate(input().split())]

  p1.sort()

  p = []
  order = []

  for i in p1:
    p.append(i[0])
    order.append(i[1])

  if sum(p) != (n - 1) * n // 2:
    print("NO")
    return

  c = 0
  for i, b in enumerate(p):
    c += b - i
    if c < 0:
      print("NO")
      return

  a = [["1"] * i + ["0"] * (n - i) for i in range(n)]

  d = [p[i] - i for i in range(n)]
  check = [0] * n
  r = n - 1
  while d != check:
    b = 0
    for _ in range(abs(d[r])):
      if d[b] > 0:
        d[b] -= 1
        d[r] += 1

        a[b][r] = "1"
        a[r][b] = "0"
      b += 1
    r -= 1

  print("YES")

  result = [["0"] * n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      result[order[i]][order[j]] = a[i][j]

  for row in result:
    print("".join(row))


if __name__ == "__main__":
  main()