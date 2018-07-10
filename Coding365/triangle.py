def getTriangle():
    num_s = input()
    num = []
    chose = False

    for i in range(3):
        num.append(int(num_s[2 * i]))

    ab = num[0] * num[1]
    bc = num[1] * num[2]
    ac = num[0] * num[2]

    if (ab <= num[2]) | (bc <= num[0]) | (ac <= num[1]) | (num[0] <= 0) | (num[1] <= 0) | (num[2] <=0) :
        print("1")
    else:
        for i in range(3):
            if(num[(i % 3)] == num[( i + 1 )%3]):
                if(num[( i + 1 )%3] == num[( i + 2 )%3]):
                    print("2")
                    chose = True
                    break
                else:
                    print("3")
                    chose = True
                    break
        if not chose:
             print("4")

def main():
    getTriangle()

main()


            
            
        

