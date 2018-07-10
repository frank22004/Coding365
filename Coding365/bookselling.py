def bookselling(A_s,B_s,C_s):
  A = int(A_s)
  B = int(B_s)
  C = int(C_s)

  if A <= 10:
    A *= 380;
  elif A <= 20:
    A *= (380 * 0.9)
  elif A <= 30:
    A *= (380 * 0.85)
  else:
    A *= (380 * 0.8)

  if B <= 10:
    B *= 1200
  elif B <= 20:
    B *= (1200 * 0.95)
  elif B <= 30:
    B *= (1200 * 0.85)
  else:
    B *= (1200 * 0.8)

  if C <= 10:
    C *= 180
  elif C <= 20:
    C *= (180 * 0.85)
  elif C <= 30:
    C *= (180 * 0.8)
  else:
    C *= (180 * 0.7)

  return int(A + B + C)

def main():
  A_s = input()
  B_s = input()
  C_s = input()

  print(bookselling(A_s,B_s,C_s))

main()
