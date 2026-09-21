class Stack:

    def __init__(self):
        self._items = []

    def pop(self):
        return self._items.pop()

    def push(self, item):
        self._items.append(item)

    def isEmpty(self):
        return len(self._items) == 0


def main():

    def recur(l, r, arr):
        if r - l <= 1:
            return

        x = arr[l]

        ls = Stack()
        rs = Stack()

        for i in arr[l + 1:r]:
            if i < x:
                ls.push(i)
            else:
                rs.push(i)

        m = l

        while not ls.isEmpty():
            arr[m] = ls.pop()
            m += 1

        arr[m] = x
        i = m
        m += 1

        while not rs.isEmpty():
            arr[m] = rs.pop()
            m += 1

        recur(l, i, arr)
        recur(i + 1, r, arr)

    k = int(input())
    arr = list(map(int, input().split()))

    recur(0, k, arr)

    print(*arr)


if __name__ == '__main__':
    main()