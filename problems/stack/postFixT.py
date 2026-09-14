



def main():
  n = input().split()

  stack = []

  for i in n:
    if i in "+-*":
      if i == "+":
        stack.append(stack.pop()+stack.pop())
      elif i == "-":
        stack.append((stack.pop()-stack.pop())*-1)
      else:
        stack.append(stack.pop()*stack.pop())
    else:
      stack.append(int(i))

  print(stack.pop())



if __name__ == "__main__":
  main()