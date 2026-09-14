import sys


def main(s):
  

  d = {2 : '2'}
  lvl = 2
  for i in s:
    if i == "(":
      d[lvl] = d.get(lvl, '') + f"{lvl+1}"
      lvl += 1
      d[lvl] = d.get(lvl, '') + f"{lvl}"
    elif i == ")":
      d[lvl] = d.get(lvl, '') + f"{lvl}"
      lvl -= 1
      d[lvl] = d.get(lvl, '') + f"{lvl+1}"
    else:
      d[lvl] = d.get(lvl, '') + i

  d[2] += '2'
  def calc(s):
    s = s.replace("!0", "1")
    s = s.replace("!1", "0")
    s = s.replace("0&0", "0")
    s = s.replace("0&1", "0")
    s = s.replace("1&0", "0")
    s = s.replace("1&1", "1")

    for i, c in enumerate(s):
      if c=="|":
        if s[i-1]+s[i+1] == "00":
          s = s[:i+1] + "0"+s[i+2::]
        else:
          s = s[:i+1] + "1"+s[i+2::]
      elif c=="|":
        if s[i-1]+s[i+1] in ("11","00"):
          s = s[:i+1] + "0"+s[i+2::]
        else:
          s = s[:i+1] + "1"+s[i+2::]
    return s[-1]

  prev = []
  for key,v in reversed(d.items()):
    for i in range(len(prev)):
      v = v.replace(f"{key+1}{key+1}", prev[i],1)

    prev=[calc(exp) for exp in v[1:-1].split(f"{key}{key}")]

  print(prev[0])


if __name__ == '__main__':
  s = "1|(0&0^1)"
  main(s)
