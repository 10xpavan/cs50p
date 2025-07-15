#defining functions
def hello(to):
    print("hello,", to)

    
name = input("whats your name? ")
hello(name)

def hello(to="world"):
    print("hello,", to)


hello()
name = input("whats your name? ")
hello(name)