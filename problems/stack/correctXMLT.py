from algocoding import Stack

TESTS = [
    # ----- Одиночные теги с длинными именами -----
    # 1. Пропущен '<' в начале открывающего тега
    ["<a><aa>", "<a></a>"],
    ["xab></ab>", "<ab></ab>"],
    # 2. Изменена первая буква имени открывающего тега
    ["<ac></ab>", "<ab></ab>"],
    # 3. Изменена последняя буква имени закрывающего тега
    ["<ab></ac>", "<ab></ab>"],
    # 4. Первый '>' заменён на '<' внутри открывающего тега
    ["<ab<</ab>", "<ab></ab>"],
    # 5. Последний '>' заменён на '<' (в конце строки)
    ["<ab></ab<", "<ab></ab>"],
    # 6. Символ '/' заменён на 'x' в закрывающем теге
    ["<ab><xab>", "<ab></ab>"],

    # ----- Другие имена -----
    ["<abc></abd>", "<abc></abc>"],      # замена 'd' на 'c' в закрывающем
    ["<abc><xabc>", "<abc></abc>"],      # '/' заменён на 'x'
    ["xabc></abc>", "<abc></abc>"],      # пропущен '<'

    # ----- Вложенные теги -----
    # 7. Изменена буква в имени внутреннего открывающего тега
    ["<root><chilc></child></root>", "<root><child></child></root>"],
    # 8. Изменена буква в имени внутреннего закрывающего тега
    ["<root><child></chilc></root>", "<root><child></child></root>"],
    # 9. Изменена буква в имени внешнего закрывающего тега
    ["<root><child></child></rood>", "<root><child></child></root>"],
    # 10. Пропущен '<' в начале внешнего открывающего
    ["xroot><child></child></root>", "<root><child></child></root>"],
    # 11. '>' заменён на '<' внутри внешнего открывающего
    ["<root<<child></child></root>", "<root><child></child></root>"],
    # 12. '/' заменён на 'x' во внутреннем закрывающем
    ["<root><child>x/child></root>", "<root><child></child></root>"],
]


def checkXML(s: str) -> bool:
  l = s[1:-1].split('><')
  # print(":  ", l)
  n = Stack()
  c = 0
  for i in l:
    if i[0] == "/":
      if c == 0:
        return False
      if n.peek() != i[1::]:
        return False
      else:
        c-=1
        n.pop()
    else:
      c+=1
      n.push(i)
  if c != 0:
    # print('3', n.show())
    return False

  
  return True


def correctXML(s: str) -> str:
  if s[0] != "<":
    return "<" + s[1::]
  if s[-1] != ">":
    return s[0:-1] + ">"

  
  k = set()

  for i in s:
    k.add(i)
  
  for i in range(len(s)):
    for j in list(k):
      if checkXML(s[0:i] + j + s[i+1::]):
        return s[0:i] + j + s[i+1::]

# def correctXML(s: str) -> str:
#   k = s.count("<")
#   if k != s.count(">"):
#     # print("<> mismatch")
    
#     if s[0] != "<":
#       return "<" + s[1::]
#     if s[-1] != ">":
#       return s[0:-1] + ">"
#     if (k - s.count(">"))**2 > 1:
#       s = s.replace(">>", "><")
#       s = s.replace("<<", "><")
#       return s
#     if 
#     for i in range(1,len(s)-1):
#       if (s[i] == ">") and (s[i+1] != "<"):
#         return s[0:i+1] + "<" + s[i+2::]
#       elif (s[i] == "<") and (s[i-1] != ">"):
#         return s[0:i-1] + ">" + s[i::]
#   else:
#     l = s[1:-1].split("><")
#     r = []
#     n = Stack([])
    
#     for i in l:
#       if i[0] == "/":
#         r.append("/"+n.pop())
#       else:
#         n.push(i)
#         r.append(i)
#     if k//2 != s.count("/"):
#       # print('/ error', n.show())
#       err = n.show()[1]
#       fix = n.show()[0]
#       window=len(err)

#       for j in range(0,len(s)-window):
#         if s[j:j+window] == err:
#           if checkXML(s[0:j] + "/" + fix + s[j+window::]):
#             return s[0:j] + "/" + fix + s[j+window::]
#     else:
#       # print('tag rename error')
#       return '<' +"><".join(r)+">"
      

# def correctXML(s: str)-> str:
#   if s[0] != "<":
#     return "<" + s[1::]
#   if s[-1] != ">":
#     return s[0:-1] + ">"

#   l = s[1:-1].split("><")
#   n = Stack()
#   forwardPass = []
#   backwardPass = []
#   l = s[1:-1].split('><')
#   err = -1
#   n = Stack()

#   for index, i in enumerate(l):
#     if i[0] == "/":
#       if n.peek() != i[1::]:
#         n.pop()
#         print("foudn idk", i)
#         forwardPass.append(0)
#       else:
#         n.pop()
#         forwardPass.append(0)
#     else:
#       n.push(i)
#       forwardPass.append(1)

#   for index, i in enumerate(l[::-1]):
#     if i[0] != "/":
#       if n.peek()[1::] != i:
#         n.pop()
#         print("issue at", i)
#         backwardPass.append(0)
#       else:
#         n.pop()
#         backwardPass.append(0)
#     else:
#       n.push(i)
#       backwardPass.append(1)


#   for i, item in enumerate(l):
#     print(f"{item}\t{forwardPass[i]}\t{backwardPass[i]}\t{backwardPass[i]*forwardPass[i]}")

import string

def is_valid_xml(s: str) -> bool:
    """Return True if s is a valid sequence of XML tags (no text)."""
    stack = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '<':
            if i + 1 < n and s[i + 1] == '/':
                # closing tag: </name>
                j = i + 2
                while j < n and s[j] != '>':
                    j += 1
                if j == n:
                    return False
                tag = s[i+2:j]
                if not tag or not tag.islower():
                    return False
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i = j + 1
            else:
                # opening tag: <name>
                j = i + 1
                while j < n and s[j] != '>':
                    j += 1
                if j == n:
                    return False
                tag = s[i+1:j]
                if not tag or not tag.islower():
                    return False
                stack.append(tag)
                i = j + 1
        else:
            # any character outside a tag is invalid
            return False
    return len(stack) == 0

def fix_xml(s: str) -> str:
    """Brute‑force: try replacing each character with every lowercase letter.
       Returns the first valid XML found (guaranteed to exist per problem)."""
    allowed = string.ascii_lowercase
    for i in range(len(s)):
        for c in allowed:
            if s[i] == c:
                continue
            candidate = s[:i] + c + s[i+1:]
            if is_valid_xml(candidate):
                return candidate
    return s  # fallback (should never happen)

if __name__ == "__main__":
  # print("<root><chilc></child></root>".split("><"))
  # for test in TESTS:
  # s = "<abc><bac><ca><ab><c><b><a><bc><ac></ac></bc></a></b></c><ac><b></b></ac></ab><bc><a></a></bc></ca></bac></abc>"
  s = "<ab><bc><c><ac></bc></ab>"
  # print(checkXML(s))
  c = 0
  t = 0
  err = 0
  for i in range(len(s)):
    for k in "<>/abcx":
      try:
        test = [s[0:i] + k + s[i+1::], s]
        res = fix_xml(test[0])
        if res!= test[1]:
          print(test[0])
          print(res)
          print(test[1])
          print()
        else:
          c+=1
      except:
        err += 1
      t+=1   
      # print(f"{test[1]}   <--   {test[0]}")
      # print(correctXML(test[0]), correctXML(test[0])==test[1])
      # print()

  print(c, " / ", t, '   ', err)

  correctXML(s)





