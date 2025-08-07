import random

coin = random.choice(["heads", "tails"])
print(coin)

x = random.randint(1, 9)
print(x)

a = ["jack", "money", "power", "wealth"]
random.shuffle(a)
for card in a:
    print(card)