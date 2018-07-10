import math

def sumproductdiffquo():
    num1_s = input()
    num2_s = input()

    num1 = float(num1_s)
    num2 = float(num2_s)

    sum = num1 + num2
    product = num1 * num2
    diff = math.fabs(num1 - num2)
    if num2 == 0:
        quo = 0
    else:
        #無條件捨去法，乘100取整數，再除100回去
        quo = num1 / num2
        quo = quo*100
        quo_floor = math.floor(quo)

    sum_s = "Sum:"+str(format(sum,".2f"))
    diff_s = "Difference:"+str(format(diff,".2f"))
    prod_s = "Product:"+str(format(product,".2f"))
    quo_s = "Quotient:"+str(format(quo_floor/100,".2f"))

    print(sum_s)
    print(diff_s)
    print(prod_s)
    print(quo_s)

def main():
    sumproductdiffquo()

main()