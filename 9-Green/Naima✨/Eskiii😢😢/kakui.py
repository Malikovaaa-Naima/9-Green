def kalkulator():
    print("Kalkulatorga xush kelibsiz!")
    print("Amallar:")
    print("1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")

    tanlov = input("Amalni tanlang (1/2/3/4): ")

    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))

    if tanlov == '1':
        natija = a + b
        print(f"{a} + {b} = {natija}")
    elif tanlov == '2':
        natija = a - b
        print(f"{a} - {b} = {natija}")
    elif tanlov == '3':
        natija = a * b
        print(f"{a} * {b} = {natija}")
    elif tanlov == '4':
        if b != 0:
            natija = a / b
            print(f"{a} / {b} = {natija}")
        else:
            print("0 ga bo'lish mumkin emas!")
    else:
        print("Noto'g'ri tanlov!")

kalkulator()
