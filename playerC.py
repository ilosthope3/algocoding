def main():
  n = int(input())
  queue = []
  for _ in range(n):
    name, l = input().split()
    queue.append((name, int(l)))

  m = int(input())
  events = []
  for _ in range(m):
    t, name, l = input().split()
    events.append((int(t), name, int(l)))

  stack = []
  qp = 0
  evp = 0
  t = 0

  while qp < n or stack or evp < m:

    if qp == n and not stack and evp < m:
      t = max(t, events[evp][0])

    while evp < m and events[evp][0] <= t:
      _, name, l = events[evp]
      stack.append((name, l))
      evp += 1

    if stack:
      name, l = stack.pop()
    elif qp < n:
      name, l = queue[qp]
      qp += 1
    else:
      continue

    print(name, t)

    t += l

    while evp < m and events[evp][0] <= t:
      _, name, l = events[evp]
      stack.append((name, l))
      evp += 1


if __name__ == "__main__":
  main()
