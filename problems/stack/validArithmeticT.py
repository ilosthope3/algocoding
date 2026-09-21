

import sys


def main():
  # s = input()
  s = "(2 + 5)*3 + 12 - 7"
  d = {0 : ''}
  lvl = 0

  for i in s:
    if i not in '1234567890 +-*()':
      return "WRONG"

  for i in s:
    if i != " ":
      if i == "(":
        d[lvl] += " "
        lvl += 1
      else:
        d[lvl]

  stack = []
  for i in s:
    if i != ' ':
      stack.append(i)
    


if __name__ == '__main__':
    main()
