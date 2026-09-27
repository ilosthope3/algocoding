

def xor(a,b):
  n1 = bin(a)[2:]
  n2 = bin(b)[2:]
  
  d = len(n1) - len(n2)
  if d > 0:
    n2 = "0"*d + n2
  else:
    n1 = "0"*abs(d) + n1
    
  # print(n1)
  # print(n2)
  
  r = ""
  for i in range(len(n1)):
    r += "0" if n1[i] == n2[i] else "1"
  
  # print(f"{int(r,2)}    {a}     {b}\n")
  return int(r,2)

def transform(arr):
  r = []
  for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
      r.append(xor(arr[i],arr[j]))
      
  return sorted(r)[:len(arr)]


if __name__ == "__main__":
  q = 2
  # arr = [56, 73, 81, 23, 17, 92, 50, 34, 67, 78]
  arr = [int(i) for i in "6 7 8 9 15".split()]
  print(arr)
  for _ in range(q):
    arr = transform(arr)
  
    print(arr)
    print(max(arr) - min(arr))
  