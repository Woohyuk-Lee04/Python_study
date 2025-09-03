"""customer = {
    "name" : "John Smith",
    "age" : 30,
    "is_verified" : True
}

print(customer["name"])
customer["name"] = "Jack Smith"
print(customer.get("name"))
print(customer.get("birthdate", "Jan 1 1980"))"""

Numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
}

phone = input("Phone : ")
output = ""
for numb in phone:
    output += Numbers.get(numb) + " "
print(output)


Emojis = {
    ":)" : "😊",
    ":(" : "😭"
}

sen = input("> ")
words = sen.split(' ')
output = ""
for word in words:
    output += Emojis.get(word, word) + " "
print(output)