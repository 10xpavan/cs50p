def main():
    number = getnum()
    meow(number)


def getnum():
    while True:
        n = int(input("what is n "))
        if n > 0:
            break
    return n
    
    
    
def meow(n):
    for _ in range(n):
        print("meow")


main()