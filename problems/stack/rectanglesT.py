import sys


def main():
    
    h = [int(i) for i in input().split()]
    n = len(h)
    stack = []
    ans = 0
  
    for i in range(n):
        while stack and h[stack[-1]] > h[i]:
            j = stack.pop()

            left = stack[-1] + 1 if stack else 0
            width = i - left

            ans = max(ans, h[j] * width)

        stack.append(i)

    # Process bars that extend all the way to the right
    while stack:
        j = stack.pop()

        left = stack[-1] + 1 if stack else 0
        width = n - left

        ans = max(ans, h[j] * width)

    print(ans)


if __name__ == "__main__":
    main()
