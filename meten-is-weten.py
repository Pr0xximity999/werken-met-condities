a = int(input("Geef me een heel getal: "))
b = int(input("Geef me nog een heel getal: "))

if a > b:
    max = a
    print(f"a is het grootste getal: {max}")
elif a < b:
    min = a
    print(f"a is het kleinste getal: {min}")
else:
    print("a en b zijn even groot")
