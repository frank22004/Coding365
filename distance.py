#算出a,b,c三條線在x軸上所涵蓋的長度
def main():
    largest = 0
    smallest = 0
    a = 0
    
    for i in range(6):
        a = input()
        a = int(a)
        
        if a > largest:
            largest = a
        elif a < smallest:
            smallest = a
    
    print(int(largest+abs(smallest)))

main()