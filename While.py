"""i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")"""

code = 9

i = 3
while i > 0:
    num = int(input("Guess : "))
    if num == code:
        print("You won!")
        break
    i -= 13
else:
    print("Failed")
    
