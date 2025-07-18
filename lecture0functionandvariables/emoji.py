def emojimap(to):
    to = to.replace(":)", "😊")
    to = to.replace(":(", "😔")
    return to

nam = input("heyy, enter something")
result = emojimap(nam)
print(result)