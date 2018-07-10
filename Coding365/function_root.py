import math

def function():
    a_s = input()
    b_s = input()
    c_s = input()

    a = int(a_s)
    b = int(b_s)
    c = int(c_s)

    t = b**2 - 4*a*c
    if t >= 0:
      x1 = (-b + math.sqrt(t)) / (2 * a)
      x2 = (-b - math.sqrt(t)) / (2 * a)
      print(format(x1,".1f"))
      print(format(x2,".1f"))
    else:
      real = format(-b / 2*a,".1f")
      img = format(math.sqrt(abs(t)) / 2 * a,".1f")

      x1 = real+"+"+img+"i"
      x2 = real+"-"+img+"i"

      print(x1)
      print(x2)

def main():
    function()

main()
