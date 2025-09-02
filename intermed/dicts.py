mydict = {"name": "Max", "age": 28, "city": "new york"}
print(mydict)

mydict2 = dict(name="mary", age=27, city="boston")
print(mydict2)

mydict_cpy = mydict.copy()

mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

mydict.update(mydict2)
print(mydict)


#you use () in tupes, and [] in list oaky. and dictuinaryies use {} even sents use {} but without key and value
#sets always are unordered, whatever you save there, tehy stay unordereed aka arbitary