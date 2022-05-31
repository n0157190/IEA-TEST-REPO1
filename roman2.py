import roman

while True:
    try:
        number=int(input("Please enter a number: "))
        print(roman.toRoman(number))
    except Exception:
        print("Out of range")
    continue