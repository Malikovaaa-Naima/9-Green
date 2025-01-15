""" vazifa """
summa = 0
j = int(input("How many person? :"))
for n in range(j):
    people = int(input("How old are you ? :"))
    if people < 0 or people > 100:
            print("Siz noto'g'ri  ball kiritdingiz.")
    elif   people  <= 0 or people <= 7:
                print( "Siz uchun bepul ! Marhamat kiring!✨✨✨")
    elif 8 <= people <= 18 :
                print("Siz uchun 20,000 so'm .OK !😂😂😂")
                summa = summa + 20_000
    elif 19 <= people <= 69:
                print("Siz uchun 60,000 so'm . OK!🤣🤣🤣")
                summa = summa + 60_000
    elif 70 <= people <= 100:
                print("Siz uchun bepul ! Marhamat kiring!✨✨✨")
    else:
                print(f"{people} musbat son emas.👌👌👌😒🤣🤣")
print(f"Sizlar uchun kirish narhi umumiy  {summa} so'm bo'ldi.❗❗💰💰. ")



""" vazifa"""
parol1 = input("Yangi parol kiriting:")
if len(parol1) >= 8 :
        parol2 = input("Qayta kiriting:")
        if  parol1 == parol2:
                print("Parol tasdiqlandi:")
        else:
                print("Parol tasdiqlanmadi.🤣🤣🤣")
                print("Qaytaadan urinib ko'ring!")
else:
        print("Parolingiz kamida 8 ta harfdan iborat bo'lishi kerak....")



""" vazifa """
ombor = ["olma", "olcha", "gilos", "banan", "tarvuz", "malina", "qulubnay", "shaftoli"]
print(f"Bizda quidagi mahsulotlar bor: ", end="")
for mahsulot in ombor:
    if mahsulot == ombor[-1]:
        print(f"{mahsulot}", end=". ")
    elif mahsulot == ombor[0]:
        print(mahsulot.title(), end=", ")
    else:
        print(f"{mahsulot}", end=",")

xarid = int(input("\nNechta mahsulot sotib olmoqchisiz: "))
bor = []
yoq = []
for x in range(xarid):
    maxsulot = input(f"{x+1}- mahsulotni kiriting: ").lower()
    if maxsulot in ombor:
        bor.append(maxsulot)
    else:
        yoq.append(maxsulot)

print(f"Siz sotib olmoqchi bo'lgan quidagi {len(bor)} ta mahsulotlar bizning do'konda bor: ", end="")
for mahsulot in bor:
    if mahsulot == bor[-1]:
        print(mahsulot, end=".")
    elif mahsulot == bor[0]:
        print(mahsulot.title(), end=", ")
    else:
        print(mahsulot, end=", ")


print(f"\nSiz sotib olmoqchi bo'lgan quidagi {len(yoq)} ta mahsulotlar bizning do'konda yo'q: ", end="")
for mahsulot in yoq:
    if mahsulot == yoq[-1]:
        print(mahsulot, end=".")
    elif mahsulot == yoq[0]:
        print(mahsulot.title(), end=", ")
    else:
        print(mahsulot, end=", ")



