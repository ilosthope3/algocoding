from algocoding import Stack

TESTS = [
  "(()())",
  "([)]"
  ]

MAP = {
  "{":"}",
  "[":"]",
  "(":")"
  }

def isCorrectOrder(s: str) -> bool:
  stack = Stack()
  for c in s:
    if c in "([{":
      stack.push(c)
    else:
      if stack.isEmpty():
        return False
      else:
        if MAP[stack.peek()] != c:
          return False
      stack.pop()

  return stack.isEmpty()


if __name__ == "__main__":
  for test in TESTS:
    print(test)
    print(isCorrectOrder(test))
    print()

