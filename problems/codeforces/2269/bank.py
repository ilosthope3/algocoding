import sys

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    out.append((k-1) * 2 + 2**(n-k+1))
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    