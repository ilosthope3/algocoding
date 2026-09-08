from algocoding import Stack

TESTS = [
    # Single tag pairs
    ["xa></a>", "<a></a>"],       # missing '<'
    ["<b></a>", "<a></a>"],       # opening name changed
    ["<a<</a>", "<a></a>"],       # first '>' replaced by '<'
    ["<a></b>", "<a></a>"],       # closing name changed
    ["<a></a<", "<a></a>"],       # last '>' replaced by '<'
    ["<a><xa>", "<a></a>"],       # '/' replaced by 'x'
    ["<a>>/a>", "<a></a>"],       # inner '<' replaced by '>'

    # Another tag pair
    ["xb></b>", "<b></b>"],
    ["<c></b>", "<b></b>"],
    ["<b></c>", "<b></b>"],
    ["<b></b<", "<b></b>"],

    # Nested tags
    ["<a><c></b></a>", "<a><b></b></a>"],   # inner opening name changed
    ["<a><b></c></a>", "<a><b></b></a>"],   # inner closing name changed
    ["<a><b></b></c>", "<a><b></b></a>"],   # outer closing name changed
    ["<a><b></b></a", "<a><b></b></a>"],    # missing final '>'
    ["<a><b></b></a>", "<a><b></b></a>"],   # already valid (no change) – not needed
]

MAP = {
  "<":")",
  "[":"]",
  }




  
def correctXML(s: str) -> str:
  # i = 0
  # <a>
  # while i<len(s):
  #   if s[i+2] == ">": #an op brace
  #     if (s[i+1] < 'a') or ( s[i+1]>'z'):
  #       pass #error that a strange symbol is placed instead of a letter
  #   elif s[i+]
  if s[0] != "<":
    return "<" + s[1::]
  if s[-1] != ">":
    return s[0:-1] + ">"
  s = s[1:-1]
  r = [] 
  l = s.split("><") # a /a b /b
  n = Stack()
  # print(": ", l)
  for i in l:
    # print(f"----{i}")
    if (len(i) == 1):
      n.push(i)
      r.append("><"+i)

    elif len(i) == 2:
      if i[0] != "/":
        # print("! ", "></"+i[1])
        r.append("></"+i[1])
        
      elif n.peek() == i[1]:
        n.pop()
        r.append("><"+i)
      else:
        #error of type a /B wrong b 
        r.append("></"+n.pop())
    else:
      # print("! ", i[0] + "><"+i[3::])
      r.append(i[0] + "><"+i[3::]) #error of type a__/a wrong char in connector 
  r.append(">")
  rs = "".join(r)
  if rs[0] == ">":
    return rs[1::]
  return "<" + rs
if __name__ == "__main__":
  for test in TESTS:
    print(f"{test[1]}   <--   {test[0]}")
    print(correctXML(test[0]))
    print()
