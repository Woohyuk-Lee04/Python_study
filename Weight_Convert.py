weight = int(input("Weight : "))

convert = input("(L)bs or (K)g : ")

if convert.upper() == "L":
    print(f"You are {weight * 0.45} Kg")
else:
    print(f"You are {weight / 0.45} Lbs")