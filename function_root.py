import math

def function():
    a_s = input()
    b_s = input()
    c_s = input()

    a = int(a_s)
    b = int(b_s)
    c = int(c_s)

    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)

    print(format(x1,".1f"))
    print(format(x2,".1f"))

def main():
    function()

main()
