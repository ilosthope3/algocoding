

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


r = []
f = []
for i in range(16):
  for j in range(16):
    flag = False
    if not(i%3==0 and j%3 == 0):
      for k in range(1,6):
        if xor(i, 3*k)%3 == 0 and xor(j, 3*k)%3 == 0:
          if flag == False:
            r.append([i,j,k])
            flag = True
      if not flag:
        f.append([i,j])
          
          
for i in r: print(i)

# print("\n"*3)
# for i in f: print(i)

# d = {}
# for i in range(16):
#   d[i] = []
  
# for i in range(16):
#   for k in range(1,6):
#     temp = xor(i, 3*k)
#     d[i].append(temp)
    
      
# for key, val in d.items():
#   print(f"{key}: {val}")
        