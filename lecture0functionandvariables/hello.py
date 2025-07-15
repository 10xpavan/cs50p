print("hello world") 
name = input("now tell me your name? ").strip().capitalize()  #you can do like this also, hehe
print("your name is ", end="")
print(name)

#remove whitespace from str(string) and capitalize
#name = name.strip().capitalize()

#split user's name into first name and last name
first, last = name.split(" ")

#capitalize users name
# name = name.capitalize() or oyu can also use name.title()

#say hello to user
print(f"hello, {name}")