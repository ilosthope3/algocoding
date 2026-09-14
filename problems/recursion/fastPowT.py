

import sys


def main():
  base = int(input())
  p = int(input())

  r = 1

  while p > 0:
    if p % 2 == 1:
      r *= base

    base *= base
    p //= 2

  return r



  
if __name__ == '__main__':
  print(main())
