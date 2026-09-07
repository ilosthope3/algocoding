from algocoding import Stack

TESTS = [
    # Standard order: '(' < ')' < '[' < ']'
    [2, "()[]", "", "()"],
    [4, "()[]", "", "(())"],
    [4, "()[]", "(", "(())"],
    [4, "()[]", "()", "()()"],
    [4, "()[]", "[", "[[]]"],
    [6, "()[]", "[[]", "[[]()]"],
    [6, "()[]", "(())", "(())()"],

    # Order: '[' < ']' < '(' < ')'  (square brackets are smaller)
    [4, "[]()", "", "[][]"],
    [4, "[]()", "[", "[[]]"],
    [4, "[]()", "(", "([)]"],   # '[' is smaller than '(' so we insert it before closing

    # Order: ')' < '[' < ']' < '('   (closing bracket is smallest)
    [4, ")[](", "", "[[]]"],     # Smallest opening is '['
    [6, ")[](", "[", "[[[]]]"],
    [4, ")[](", "(", "()()"],

    # Order: ']' < '(' < ')' < '['  (closing square is smallest)
    [4, "]( )[", "", "(())"],    # Smallest opening is '('

    # Edge: prefix already complete
    [6, "()[]", "(())()", "(())()"],
    [4, "()[]", "()", "()()"],
]

MAP = {
  "(":")",
  "[":"]",
  }

def remainingBrackets(s: str) -> str:
  
  stack = Stack()
  for c in s:
    if c in "([":
      stack.push(c)
    else:
      stack.pop()

  return "".join([MAP[stack.pop()] for _ in range(len(stack.show()))])

def minPair(s: str, n: int) -> str:
  c = min([s.find(key) for key,_ in MAP.items()])
  return s[c]*(n//2) + MAP[s[c]]*(n//2), c
  

def minBracketOrder(n: int, order, s: str) -> str:

  r = remainingBrackets(s)
  print(": ", s+r)
  if len(s + r) == n:
    return s+r
  else:
    t, index = minPair(order, n-(len(s+r)))
    for i in range(len(r)):
      if order.find(r[i]) > index:
        return s + r[0:i] + t + r[i::]
    return s + r +t
  


if __name__ == "__main__":
  for test in TESTS:
    print(test)
    print(minBracketOrder(test[0], test[1], test[2]))
    print()






# Пусть символы ’[’, ’]’, ’(’ и ’)’ некоторым образом упорядочены. Рассмотрим все ПСП длины n n состоящие из круглых и квадратных скобок и начинающиеся со строки s s. Среди этих ПСП необходимо найти лексикографически минимальную.

# Строка A A лексикографически меньше строки B B (их длина совпадает), если существует такое i i, что для всех j < i j<i A j = B j Aj​=Bj​, а A i < B i Ai​<Bi​.

# Лексикографический порядок скобок задается строкой w w, состоящей из 4 символов. При этом w 1 < w 2 < w 3 < w 4 w1​<w2​<w3​<w4​. Например, если w = ( ) [ ] w=()[], то ( < ) < [ < ] (<)<[<].
# Формат ввода

# В первой строке записано число n n ( 1 ≤ n ≤ 100000 1≤n≤100000).

# Во второй строке записана строка w w, состоящая из 4 различных скобок.

# В третьей строке записана строка s s, ее длина не превосходит n n.
