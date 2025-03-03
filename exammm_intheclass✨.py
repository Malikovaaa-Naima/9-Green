""" 2) Mashq"""
# r = int(input("Radius kiriting:")) 
# pi = 3.14
# s = pi*r**2
# print(f"Siz kiritgan aylana radiusi {r} bo'lib.Doira yuzi {s}")
""" 3) Mashq"""
# from math import sqrt
# a = int(input("To'g'ri burchakli uchburchakni katetlarini kiriting:"))
# b = int(input("To'g'ri burchakli uchburchakni katetlarini kiriting:"))
# c = sqrt(a**2+b**2)
# print(f"Siz kiritgan katetlar soni {a,b} , Gipetunizuya {c} ga teng. ")


""" MASHQ """
#1
# son = list(range(120,1200,2))
# print(son)
# print(sum(son))
# # print(son)
# print(max(son) - min(son))
# print(len(son))
# #2
# son2 = son [:20]
# son2 = son [520:]
# son2 = son [260:280]
# son2 = son [:]
# print(son2)   
# #3
# taom = ["palov","manti","somsa","mastava"]
# nonushta= []
# taom  =  nonushta[:]
# print(nonushta)       
# nonushta.clear()
# nonushta.append("qaymoq")
# nonushta.append("maloko")
# nonushta.append("non")
# nonushta.append("tuxum")
# nonushta.append("kalbasa")
# print(taom)
# print(nonushta)


""" Mashq"""
# family = []
# family.append(input("Otangizni ismini kiriting:"))
# family.append(input("Onangizni ismini kiriting:"))
# family.append(input("Ukangizni  ismini kiriting:"))
# family.append(input("Ukangizni  ismini kiriting:"))
# family.append(input("O'zingizni ismingizni kiriting:"))

# print(f"Sizning oilangizda {len(family)} ta inson bor.Ular {family[0]} va \
# {family[1]} {family[2]}.")
# print(family)

""" Mashq"""
# ball = int(input("Imtihon balingizni kiriting: "))
# if ball < 1 or ball <= 2:
#     print("Siz yomon baho oldiz 😢")
# elif ball == 3:
#     print(" qoniqarli 🤦‍♀️")
# elif ball == 4:
#     print(" yaxshi😁")
# elif ball == 5:
#     print(" Alo 🎉✨")
# else:
#     print("Siz notogri ball kiritdingiz:(")


""" mashq """
# sonlar = int(input("Ihtiyoriy son kiriting:"))
# if sonlar > 0:
#     print(f"{sonlar} -->  bu son musbat .")
# elif sonlar < 0:
#     print(f"{sonlar} --> bu son manfiy .")
# elif sonlar == 0:
#     print(f"{sonlar} --> bu son musbat ham emas manfiy ham emas .OK!😊😊😊")

""" mashq """
# son = input("Son kiriting:")
# if '.'in son: 
#     print("Bu son o'nlik son.✨")
# else:
#     print("Bu butun son.✨")


"""mashq"""
# son = int(input("Birinchi sonni kiriting:"))
# son1 = int(input("Ikkinchi sonni kiriting:"))
# if son > son1:
#     print(f"{son}  >  {son1}")
# elif son < son1:
#     print(f"{son}  <  {son1}")
# elif son == son1:
#     print(f"{son}  =  {son1}")

""" mashq"""
# son1 = float(input("Birinchi sonni kiriting:"))
# son2 = float(input("Ikkinchi sonni kiriting:"))
# son3 = float(input("Uchunchi sonni kiriting:"))

# sonlar = [son1,son2,son3]

# for son in sonlar:
#     if son > 0:
#         print(f"{son} ning kubi {son**3} ga teng✨✨✨.")
#     elif son == 0:
#         print(f"{son} musbat ham manfiy ham emas OK! ❗❗❗❗❌.")
#     else:
#         print(f"{son} musbat son emas😁😁😁😁.")

""" mashq """
# age = int(input("Nech yoshsz ? "))
# if age >= 1 and age <=7:
#     print("Sizga bepul")
# elif age >= 8 and age <=18:
#     print("Sizga 5 ming som")
# elif age >= 19 and age <=70:
#     print("Sizga 10 ming som")
# elif age >= 70 and age <=100:
#     print("Sizga BEPUL")
# elif age <0:
#     print(f"Bu musbat son emas.👌👌👌😒🤣🤣")
# else:
#     print("Siz noptugri son kiritingiuz.")



""" mashq """
# summa = 0
# j = int(input("How many person? :"))
# for n in range(j):
#     people = int(input("How old are you ? :"))
#     if people < 0 or people > 100:
#             print("Siz noto'g'ri  ball kiritdingiz.")
#     elif   people  <= 0 or people <= 7:
#                 print( "Siz uchun bepul ! Marhamat kiring!✨✨✨")
#     elif 8 <= people <= 18 :
#                 print("Siz uchun 20,000 so'm .OK !😂😂😂")
#                 summa = summa + 20_000
#     elif 19 <= people <= 69:
#                 print("Siz uchun 60,000 so'm . OK!🤣🤣🤣")
#                 summa = summa + 60_000
#     elif 70 <= people <= 100:
#                 print("Siz uchun bepul ! Marhamat kiring!✨✨✨")
#     else:
#                 print(f"{people} musbat son emas.👌👌👌😒🤣🤣")
# print(f"Sizlar uchun kirish narhi umumiy  {summa} so'm bo'ldi.❗❗💰💰. ")



""" mashq """
# parol =input("Parol kiriting:")
# if len(parol) >8:
#         parol1 = input("Qayta kiriting:")
#         if parol == parol1:
#                 print("Parol tasdiqlandi:🎉")
#         else:
#                 print("Parol tasdiqlanmadi:😂")
#                 print("Qaytadan urunib ko'ring:😢")
# else:
#         print("Parolingiz kamida 8 ta belgi bo'lishi kerak....😎👌")






""" mashq """
# parol1 = input("Yangi parol kiriting:")
# if len(parol1) >= 8 :
#         parol2 = input("Qayta kiriting:")
#         if  parol1 == parol2:
#                 print("Parol tasdiqlandi:")
#         else:
#                 print("Parol tasdiqlanmadi.🤣🤣🤣")
#                 print("Qaytaadan urinib ko'ring!")
# else:
#         print("Parolingiz kamida 8 ta harfdan iborat bo'lishi kerak....")

""" mashq  """
# ombor = ["olma", "olcha", "gilos", "banan", "tarvuz", "malina", "qulubnay", "shaftoli"]
# print(f"Bizda quidagi mahsulotlar bor: ", end="")
# for mahsulot in ombor:
#     if mahsulot == ombor[-1]:
#         print(f"{mahsulot}", end=". ")
#     elif mahsulot == ombor[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(f"{mahsulot}", end=",")

# xarid = int(input("\nNechta mahsulot sotib olmoqchisiz: "))
# bor = []
# yoq = []
# for x in range(xarid):
#     maxsulot = input(f"{x+1}- mahsulotni kiriting: ").lower()
#     if maxsulot in ombor:
#         bor.append(maxsulot)
#     else:
#         yoq.append(maxsulot)

# print(f"Siz sotib olmoqchi bo'lgan quidagi {len(bor)} ta mahsulotlar bizning do'konda bor: ", end="")
# for mahsulot in bor:
#     if mahsulot == bor[-1]:
#         print(mahsulot, end=".")
#     elif mahsulot == bor[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(mahsulot, end=", ")
# print(f"\nSiz sotib olmoqchi bo'lgan quidagi {len(yoq)} ta mahsulotlar bizning do'konda yo'q: ", end="")
# for mahsulot in yoq:
#     if mahsulot == yoq[-1]:
#         print(mahsulot, end=".")
#     elif mahsulot == yoq[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(mahsulot, end=", ")





""" mashq """
# bor = ["pamada","ten","pudra","tush","penka","srap","qalam" ," atir"]
# print(f"Bizda quidagi mahsulotlar bor :" , end="")
# for h in bor:
#     if h == bor[-1]:
#         print(f"{h} " , end=" .")
#     elif h == bor[0]:
#         print(h.title(), end=", ")
#     else:
#         print(f"{h}", end=",")

# xarid = int(input("\nNechta mahsulot sotib olmoqchisiz: "))
# bor = []
# yoq = []
# for x in range(xarid):
#     m = input(f" nima sotib olmoqcisz : ").lower()
#     if m in bor:
#         bor.append(m)
#     else:
#         yoq.append(m)

# print(f"Siz sotib olmoqchi bo'lgan quidagi {len(bor)} ta mahsulotlar bizning do'konda bor: ", end="")
# for a in bor:
#     if a == bor[-1]:
#         print(a, end=".")
#     elif a == bor[0]:
#         print(a.title(), end=", ")
#     else:
#         print(a, end=", ")

# for n in yoq:
#     if n == yoq[-1]:
#         print(n, end=".")
#     elif n == yoq[0]:
#         print(n.title(), end=", ")
#     else:
#         print(n, end=", ")
# print(f"\nSiz sotib olmoqchi bo'lgan quidagi   mahsulotlar bizning do'konda yoq: ", end="")


""" mashq """
# kurs = ["english","russia","ICT","tarix","arab tili","ona tili","koreys tili"]
# print("Assalomu aleykum Hurmatli mijoz hush kelibsz!✨")
# print("Bizda quida kurslar mavjud:" ,end=" ")
# for n in kurs:
#     print(f" {n} ", end=" ")

# t = input("\n Qanaqa kursda oqimoqchisz:")
# narx = 0
# if t in kurs:
#     if t == "English":
#         narx = 700_000
#     elif t == "Russia":
#         narx = 500_000
#     elif t == "ICT":
#         narx = 600_000
#     elif t == "Tarix":
#         narx = 300_000
#     elif t == "Arab tili":
#         narx = 900_000
#     elif t == "Ona tili":
#         narx = 200_000
#     elif t == "Koreys tili":
#         narx = 800_000
#     print(f"{t} kursining narhi {narx} 🎉✨")

# else:
#     print(f"Bizda siz kiritgan kurs yoq !❌")
#     print(f"Boshqa filyalimizga boring .OK ✨")


""" 03. 05 . 24"""
""" 1 mashq """
# sonlar = []
# son1 = int(input("Birinchi sonni kiriting:"))
# son2 = int(input("Ikkinchi sonni kiriting:"))
# son3 = int(input("Uchunchi sonni kiriting:"))
# sonlar.append(son1)
# sonlar.append(son2)
# sonlar.append(son3)
# for son in sonlar:
#     if son < 0:
#         print(f"{son**5}")
#     else:
#         print(f"{son**4}")

""" 2 mashq """
# ism = input("Ismingizni kiriting:").lower()
# if ism == "muslima":
#     print(f"Salom Muslima.Davramizda hush ko'rdik.")
# elif ism =="zilola" or ism == "sevara":
#     print("Assalomu aleykum . Sizga qanday yordam beriwim mumkin.")
# elif ism =="anvar" or ism == "aziz":
#     print("Salom . Bugun qayerga boramiz.")
# else:
#     print("Qalaysan")

""" 3 mashq"""
# sinf = input("sinfingni kirit:")
# if sinf =="green":
#     yosh = int(input("Yoshingizni kiritng:"))
#     if yosh >= 14:
#         print("sinfga kirish mumkin.")
#     else:
#         print("Sinfga kirish mumkinmas.")



""" mashq """
# dostla ={
#     "dost1":"Munisa",
#     "dost2":"Mubina"
# }

# dostla["dost3"]="Rahima"
# dostla[input("Yangi key")]=input("Yangi ism:")
# dostla.update({"dost4":"Oydina"})
# dostla["dost3"]="Madina"
# dostla.update({"dost4":"Zulfiya"})



# dostla[input("Yangi key")]=input("Yangi ism:")
# dostla[input("Yangi key")]=input("Yangi ism:")

# print(dostla)


"""mashq"""
# otam = {
#     "ism":"Murodbek",
#     "yil":1984,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Otamning ismi {otam["ism"]} . Otam {otam["yil"]} da tugulgan. {otam["shahar"]} shahardada yashaydi . Manzil {otam["manzil"]} .")


# onam = {
#     "ism":"Nodira",
#     "yil":1990,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }
# print(f"Onamning ismi {onam["ism"]} . Onam {onam["yil"]} da tugulgan. {onam["shahar"]} shahardada yashaydi . Manzil {onam["manzil"]} .")

# ukalarim = {
#     "ism":"Ozodbek va Asadbek",
#     "yil":2014,
#     "yil1":2017,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"ukalarim ismi {ukalarim["ism"]} . ukalarim {ukalarim["yil"]}, {ukalarim["yil1"]} da tugulgan. {ukalarim["shahar"]} shahardada yashaydi . Manzil {ukalarim["manzil"]} .")

""" 2 mashq"""
# oila = {
#     'ota': 'kfc',
#     'ona':'shahli',
#     'uka':'manti',
#     'uka2':'fast food',
    
# }

# print(f"otamning sevimli taomi {oila['ota']}")

# print(f"otamning sevimli taomi {oila['ona']}")

# print(f"otamning sevimli taomi {oila['uka']}")

# print(f"otamning sevimli taomi {oila['uka1']}")


""" mashq """
# python ={
#     "if":"Agar",
#     "else":"aks holda",
#     "and":"va",
#     "or":"yoki",
#     "float":"onlik son",
#     "int":"butun son",
#     "string":"matn",
#     "input":"sorash",
#     "append":"qoshish",
#     "dict":"lugat",
# }

# print(f"ifning manosi --> {python['if']}  ")
# print(f"elsening manosi --> {python['else']}  ")
# print(f"andning manosi --> {python['and']}  ")
# print(f"orning manosi --> {python['or']}  ")
# print(f"floatning manosi --> {python['float']}  ")
# print(f"intning manosi --> {python['int']}  ")
# print(f"stringning manosi --> {python['string']}  ")
# print(f"inputning manosi --> {python['input']}  ")
# print(f"append ning manosi --> {python['append']}  ")
# print(f"dictning manosi --> {python['dict']}  ")


""" mashq"""
# sonlar = []
# for x in range(5):
#     sonlar.append(int(input(f"{x+1} --> son kiriting:")))

# from math import sqrt
# for son in sonlar:
#     if son > 0:
#         print(f"{son} ning ildizi {sqrt(son)} ga teng.")
#         print(f"{son} ning 4 darajasi {son**4} ga teng.")
#         print(f"{son} ning o'zidan 2 ta katta son {son+2} ga teng.")


""" mashq """
# students= {
#     "student1":"Naima",
#     "student2":"Noila",
#     "student3":"Nozima",
#     "student4":"Nargiza",
#     "student5":"Nodira",
# }

# #1
# students["student2"] = "Ummugulsum"
# students["student2"] = "Gulsuma"
# #2
# students[input('Yangi key:')] = input("Yangi ism:")
# students[input('Yangi key:')] = input("Yangi ism:")
# students[input('Yangi key:')] = input("Yangi ism:")
# #3
# del students ["student5"]
# #4
# students.update({"student6":"Sarvinoz"})
# students.update({"student7":"Sevara"})
# #5
# students.pop("student2")
# #6
# pupil = students.copy()
# pupil1 = dict(students)
# #7
# students.clear()
# #8
# pupil.popitem()

# print(students)
# print(pupil)
# print(pupil1)

""" mashq  """
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

""" mashq """
# talaba = {
#     'ism':'Naima',
#     'familiya':'Malikova',
#     'yosh':15,
#     'fan':'matematika,ICT',
#     'sinf': 8 
# }
# print(talaba.items())

# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n") 

 
""" mashq """  
# mahsulotlar = { 
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
# }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")


""" mashq """  
# kutubhona = { 
#     'yolvoramn hiyonat qilma':600000,
#     'otkan kunlar':200000,
#     'quyonlar saltanati':400000,
#     'afv et allahim':45000,
#     'alkimyogar':300000
# }


# kitoblar = ["yolvoramn hiyonat qilma","afv et allahim","alkimyogar"]
# for kitob in kutubhona:
#     if kitob in kitoblar:
#         print(f"{kitob.title()} {kutubhona[kitob]} so'm")
# for buyum in kitoblar:
#     if buyum not in kutubhona:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")


""" kerakli """
# import datetime as dt
# hozir = dt.datetime.now()
# print(hozir)
# sanani ajratib olish
# print(hozir.date())

# vaqtni ajratib olish
# print(hozir.time())
# print(hozir.today())

# soatni ajratib olish
# print(hozir.hour)

# minutni ajratib olish
# print(hozir.minute)

# sekundni ajratib olish
# print(hozir.second)
""" kerakli"""


""" mashq """
# lugat ={
    # "approximately":"taxminan",
    # "endepentdent":"ozodlik",
    # "beautiful":"chiroyli",
    # "ugly":"hunuk",
    # "difucult":"qiyin",
    # "easy":"oson"
# }

# print(f"approximatelyning manosi --> {lugat["approximately"]}  ")
# print(f"endepentdentning manosi --> {lugat["approximately"]}  ")
# print(f"beautifulning manosi --> {lugat["endepentdent"]}  ")
# print(f"uglyning manosi --> {lugat["beautiful"]}  ")
# print(f"difucultning manosi -->{lugat["ugly"]}  ")
# print(f"easyning manosi --> {lugat["easy"]}  ")

"""mashq"""
# soz = input("soz kiriting:").lower()
# lugat ={
#     "approximately":"taxminan",
#     "endepentdent":"ozodlik",
#     "beautiful":"chiroyli",
#     "ugly":"hunuk",
#     "difucult":"qiyin",
#     "easy":"oson"
# }

# if soz in lugat:
#     print(f"{soz.title()} ning manosi ---> {lugat[soz]}✨")
# else:
#     print(f"Siz kiritgan {soz} bizning lugatda mavjud emas.🎉")



""" mashq """
# python ={
#     "if":"if shart qoyish uchun",
#     "else":"aks holda",
#     "and":"va",
#     "or":"yoki",
#     "float":"onlik son",
#     "int":"butun son",
#     "string":"matn",
#     "input":" biror narsani sorash",
#     "append":"biror narsani qoshish",
#     "dict":"lugat",
# }

# for n , j  in sorted(python.items()):
#     print(f"Ozgaruvchi: {n}")
#     print(f"Manosi: {j} \n")

""" mashq """
# davlatlar ={
#     "usa":"washington",
#     "turkey":"ankara",
#     "uzbekiston":"toshkent",
#     "fransiya":"parij",
#     "uk":"london",
# }

# savol = input("biror davlat yoki poytaxt nomini kiriting:").lower()
# for davlat,poytaxt in davlatlar.items():
#     if savol ==davlat:
#         print(f"{davlat.title()} ning poytaxti {poytaxt.title()} shaxri.")
#     elif savol ==poytaxt:
#         print(f"{poytaxt.title()} shaxri {davlat.title()} ning poytaxti.")

# if savol not in davlatlar.keys() and savol not in davlatlar.values():
#     print(f"Bizda bu {savol} haqida malumot  yoq:")


""" sovga """
# oyin = {
#     "tosh":"✊",
#     "qaychi":"✌",
#     "qogoz":"🤚",
# }
# i = input("Tosh/qaychi/qogaz kiriting:").lower()
# for m , n in oyin.items():
#     if i in m:
#         print(n)

""" mashq """
# dost={
#     "dost1":{
#         "m":{
#             "ism":"Mubina",
#             "familya":"Isaqjanova",
#             "yosh":18,
#             "kasb":"student"
#         }
#     }        
#         }
# for d in dost.values():
#     j = d["m"]
#     print(f"Mubina haqida malumot --> {j.values()}")

""" sovga """
# import random
# foydalanuvchi_harakati = input("Tanlovni kiriting (tosh, qog'oz, qaychi): ")
# mumkinbolgan_harakatlar = ["tosh", "qog'oz", "qaychi"]
# kompyuter_harakati = random.choice(mumkinbolgan_harakatlar)
# print(f"\nSiz tanladingiz {foydalanuvchi_harakati}, kompyuter tanladi {kompyuter_harakati}.\n")

# if foydalanuvchi_harakati == kompyuter_harakati:
#     print(f"Ikkala o'yinchi ham tanlandi {foydalanuvchi_harakati}. Bu galstuk!")
# elif foydalanuvchi_harakati == "tosh":
#     if kompyuter_harakati == "qaychi":
#         print("Tosh qaychini sindiradi! Siz yutdingiz!✨✌")
#     else:
#         print("Qog'oz toshni qoplaydi! Yutqazdingiz.😢")
# elif foydalanuvchi_harakati== "qogoz":
#     if kompyuter_harakati== "tosh":
#         print("Qog'oz toshni qoplaydi! Siz yutdingiz!✨✌")
#     else:
#         print("Qaychi qog'ozni kesadi! Yutqazdingiz.😢")
# elif foydalanuvchi_harakati == "qaychi":
#     if kompyuter_harakati == "qogoz":
#         print("Qaychi qog'ozni kesadi! Siz yutdingiz!😂😢")
#     else:
#         print("Tosh qaychini sindiradi! Yutqazdingiz.😒😒")


""" mashq  """
# ombor = ["olma", "olcha", "gilos", "banan", "tarvuz", "malina", "qulubnay", "shaftoli"]
# print(f"Bizda quidagi mahsulotlar bor: ", end="")
# for mahsulot in ombor:
#     if mahsulot == ombor[-1]:
#         print(f"{mahsulot}", end=". ")
#     elif mahsulot == ombor[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(f"{mahsulot}", end=",")

# xarid = int(input("\nNechta mahsulot sotib olmoqchisiz: "))
# bor = []
# yoq = []
# for x in range(xarid):
#     maxsulot = input(f"{x+1}- mahsulotni kiriting: ").lower()
#     if maxsulot in ombor:
#         bor.append(maxsulot)
#     else:
#         yoq.append(maxsulot)

# print(f"Siz sotib olmoqchi bo'lgan quidagi {len(bor)} ta mahsulotlar bizning do'konda bor: ", end="")
# for mahsulot in bor:
#     if mahsulot == bor[-1]:
#         print(mahsulot, end=".")
#     elif mahsulot == bor[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(mahsulot, end=", ")
# print(f"\nSiz sotib olmoqchi bo'lgan quidagi {len(yoq)} ta mahsulotlar bizning do'konda yo'q: ", end="")
# for mahsulot in yoq:
#     if mahsulot == yoq[-1]:
#         print(mahsulot, end=".")
#     elif mahsulot == yoq[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(mahsulot, end=", ")


""" mashq """
# sonlar = int(input("Ihtiyoriy son kiriting:"))
# if sonlar > 0:
#     print(f"{sonlar}  -->  {sonlar+1} .")
# elif sonlar < 0:
#     print(f"{sonlar} --> bu son manfiy .")
# elif sonlar == 0:
#     print(f"{sonlar} --> bu son musbat ham emas manfiy ham emas .OK!")

""" mashq"""
# sonlar =[]
# son1 = float(input("Birinchi sonni kiriting:"))
# son2 = float(input("Ikkinchi sonni kiriting:"))
# son3 = float(input("Uchunchi sonni kiriting:"))
# sonlar.append(son1)
# sonlar.append(son2)
# sonlar.append(son3)
# if sonlar > 0:
#     print(f"{sonlar} -->  bu son musbat .")
# elif sonlar < 0:
#     print(f"{sonlar} --> bu son manfiy .")
# elif sonlar == 0:
#     print(f"{sonlar} --> bu son musbat ham emas manfiy ham emas .OK!😊😊😊")

""" mashq """
# son = int(input("Birinchi sonni kiriting:"))
# son1 = int(input("Ikkinchi sonni kiriting:"))
# if son > son1:
#     print(f"{son}  >  {son1}")
# elif son < son1:
#     print(f"{son}  <  {son1}")
# elif son == son1:
#     print(f"{son}  =  {son1}")

""" mashq """
# mahsulotlar ={  # bu esa dict yaratganmiz.
#     "non":50000,
#     "tuz":20000,
#     "qaymoq":300000,
#     "gosht":100000,
#     "qulupnay":25000,
#     "pitsa":150000,
#     "kalbasa":50000
# }

# savat =[] # foydalanuvchi olmopqcxhi bolgan buyyum
# umumiy_narx = 0 #summani hisoblab beruvchi ozgaruvchi 
# bor =[]#dokonimizda bor narsa uchun
# yoq =[] # dokonimizda yoq narsa uchun


""" dokonimizda bor mahsulotlarni for tsikli bn chiqaramiz. """
# print("Bizning dokonimizda quidagi mahsulatlar bor:")
# for a, b in mahsulotlar.items():
#     print(f"{a} ---> {b}")


"""karoci odamda necta mahsulot olitganini sorittu ky for tsikli bn nima olmoqchiligini aylantirib beruttu."""
# s = int(input("Nechta mahsulot sotib olmoqchisiz:"))
# for m in range(s):
#     savat.append(input("Nima sotib olmoqchisz:").lower())


""" bunda esa bizda bor narsalani yozganmiz ky narxni hisoblab berganmiz."""
# for maxsulot,narx in mahsulotlar.items():
#     if maxsulot in savat:
#         umumiy_narx += narx
#         bor.append(maxsulot)


""" beyda yoq narsalar bor. """
# for maxsulot in savat:
#     if maxsulot not in mahsulotlar:
#         yoq.append(maxsulot)


""" beyda len bn olcittu ky summani hisobluttu. """
# print(f"Bizda siz kiritgan {len(bor)} ta mahsulot bor : Bular ---> " ,end="")
# for e in bor:
#     print(e,end=" ,")
# print(f"\n Umumiy narx  ---> {umumiy_narx}")


""" beyda yoq narsalar holos. """
# print(f"Bizda siz kiritgan {len(yoq)} ta mahsulot yoq : Bular ---> " ,end="")
# for j in yoq:
#     print(j,end=",")
    

""" mashq """
# davlatlar={
    # "uzb":"toshkent",
    # "korea":"soul",
    # "fransiya":"parij",
    # "USA":"Washington",
    # "Turkey":"Ankara",
    # "Uzbekiston":"Toshkent",
    # "Fransiya":"Parij",
    # "UK":"London",
# }
# for davlat,poytaxt in davlatlar.items():
#     print(f" Davlat  ---> {davlat}")
#     print(f" Poytaxt  ---> {poytaxt}\n")

# savol = input("biror davlat yoki poytaxt nomini kiriting:").lower()
# for davlat,poytaxt in davlatlar.items():
#     if savol ==davlat:
#         print(f"{davlat.title()} ning poytaxti {poytaxt.title()} shaxri.")
#     elif savol ==poytaxt:
#         print(f"{poytaxt.title()} shaxri {davlat.title()} ning poytaxti.")

# if savol not in davlatlar.keys() and savol not in davlatlar.values():
#     print(f"Bizda bu {savol} haqida malumot  yoq:")


""" mashq """
# davlatlar={
#     "uzb":"toshkent",
#     "korea":"soul",
#     "fransiya":"parij",
#     "USA":"Washington",
#     "Turkey":"Ankara",
#     "Uzbekiston":"Toshkent",
#     "Fransiya":"Parij",
#     "UK":"London",
# }

# for n , j  in sorted(davlatlar.items()):
#     print(f"Davlatlar: {n.title()}")
#     print(f"Poytaxt: {j.title()} \n")

# print("Davlatlar✨: ")
# for k in sorted(davlatlar.keys()):
#     print(k.title())


# print("\nPoytaxt✨: ")
# for v in sorted(davlatlar.values()):
#     print(v.title())

"""mashq"""
# Wi3SRPKh*j6-qwj
"""mashq"""

""" 5 test """
# #1
# a = int(input("son kiriting:"))
# b = int(input("son kiriting:"))
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print((a+b)/2)
# print(a**2)
# print(a**3)
# print(b**2)
# print(b**3)
# #2
# from math import sqrt
# import random
# print(round((231/4.7)*5))
# print(sqrt(35345+3**4)/8)
# print(random.randrange(20,80))
# r = int(input("aylanani radiusuni kiringt:"))
# pi = 5
# print(f"{pi*r**2}")
# a = int(input("son kiriting:"))
# print(f"{a**2}")
# print(f"{a*4}")
# #3
# ismlar = ["Asadbek","Ozodbek" , "Zafarbek" , "Zohirbek"]
# print(f"salom qalesan {ismlar[0]}")
# print(f"nima qilyapsan? {ismlar[1]}")
# print(f"qaydasan ? {ismlar[2]}")
# print(f"nima gaplar  {ismlar[3]}")

# """ 6 test"""
# #1
# viloyat ="Namangan"
# ozgaruvchi =32.456
# maktab_32 ="qala tumanidagi 32-maktab"
# fistname_lastname_age = "jonh","shoe",45
# #2
# x =432.45
# print(type(x))
# y =654
# print(type(y))
# z ="hsighs"
# print(type(z))
# son =45435
# print(type(son))
# son2=67586
# print(type(son2))
# #3
# from math import sqrt
# print(sqrt(234))
# print(sqrt(543))
# print(round(23.432))
# print(round(453.6765))
# print(4**4)

# """ 8 test """
# #1
# uy_raqam =int(input("uy rqam kiriting:"))
# kocha =(input("kocha  kiriting:"))
# mahalla=(input("mahalal kiriting:"))
# tuman=(input("tuman  kiriting:"))
# viloyat =(input("viloyat  kiriting:"))
# print(f"{kocha} kocxhasi,{mahalla} mahallasi,{tuman}tumani,{viloyat}viloyatida yashaym,an.")
# #2
# d = "matn"
# t = "ghr"
# hb = "htgrh"
# gh= "jjothiih"
# dh= "jjothiihy"
# ht= "jjothiith"
# hrhtr= "jjothiiht"
# print(f"{d.capitalize()},{t.title()},{hb.lstrip()},{gh.rstrip()},{dh.strip()},{ht.lower()},{hrhtr.upper()}")

# """ 9 tast"""
# #1
# number = []
# number.append(float(input("Son kiriting")))
# number.append(float(input("Son kiriting")))
# number.append(float(input("Son kiriting")))
# number.append(float(input("Son kiriting")))

# number.remove(12)
# number.remove(7)
# number.insert(3,(input("Son kiriting")))
# number.insert(2,(input("Son kiriting")))
# number.insert(0,(input("Son kiriting")))
# number.insert(-1,(input("Son kiriting")))
# number1 = number[:]
# number.reverse()
# number1.reverse()
# print(number)
# print(number1)
# #2
# son = int(input("xoxlagan soningizni kiriting:"))
# son1 = int(input("xoxlagan soningizni kiriting:"))
# sonlar = list(range(son, son1))
# print(len,{sonlar})
# sonlar.sort()
# sonlar.sort(reverse=True)
# print(sonlar)
# #3
# n = list(range(-2024,2024, 2))

# g =list(range(123,87384, 2))

# h =list(range(352,20010118, 11))
# print(sum(h))
# #4
# davlatlar = ["Tokiyo" ,"Toshkent","Sofiya","AQSH","Xorazm","Samarqand"]
# davlatlar.sort()
# davlatlar.sort(reverse=True)
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))

# davlatlar.insert(0,input("Hohlagan shaharizni kiriting"))
# davlatlar.insert(5,input("Hohlagan shaharizni kiriting"))
# davlatlar.insert(3,input("Hohlagan shaharizni kiriting"))
# davlatlar.reverse()
# uzb =[]
# uzb.append(davlatlar.pop("Toshkent"))
# uzb.append(davlatlar.pop("Xorazm"))
# uzb.sort()
# print(davlatlar)
# print(uzb)

# """ 10 test"""
# #1
# sonlar =list(range(101,1000,2))
# print(sonlar)
# sonlar2 =list(range(21,200,2))
# print(sonlar2)
# sonlar3 =list(range(100,500,5))
# print(sonlar3)

# #2
# mevalar = ["banan","kivi","gilos","olcha","olma",]
# print(mevalar)
# mevalar.append("apelsin")
# mevalar.append("mango")
# mevalar.append("uzum")
# mevalar.insert(-1,"avcco")
# mevalar.insert(-4,"anjir")
# mevalar.insert(3,"sirus")
# mevalar[-1]
# #3
# family = []
# family.append(input("Otangizni ismini kiriting:"))
# family.append(input("Onangizni ismini kiriting:"))
# family.append(input("Ukangizni  ismini kiriting:"))
# family.append(input("Ukangizni  ismini kiriting:"))
# family.append(input("O'zingizni ismingizni kiriting:"))
# family.sort()
# family.sort(reverse=True)
# print(family)
# family.clear()
# #4
# numbers = [1,-2, 12, 232, -45,-34,-68,100 ,234, -4325]
# musbat =[]
# numbers.pop(1) 
# numbers.pop(12) 
# numbers.pop(232) 
# print(numbers)
# print(musbat)

""" 11 test """
# #1
# for s in range(200,800):
#     print(f"{s**3} --- {s**5}")
# #2
# student =["naima","naima","mubina","munisa","madina","zulfiya"]
# print(f"salom qalesan {student[0]}")
# print(f"nima qilyapsan? {student[1]}")
# print(f"qaydasan ? {student[2]}")
# print(f"nima gaplar  {student[3]}")
# #3
# mevalar =[]
# for m in range(5):
#     mevalar.append(input("meva kiritting:"))
# mevalar.sort()
# mevalar.sort(reverse=True)
# print(len(mevalar))
# mevalar.reverse()
# #4
# boys = ["Olim" ,"Anvar" ,"Umar"]
# adjective = ["bilimdon" ,"kuchli","aqlli"]
# for adj in adjective:
#     for boy in boys:
#         print(f"{boy} is very {adj} boy")

""" 12 test"""
#1
# mevalar =["olma","gilos","olcha","sabs","karam"]
# for meva in mevalar:
#     if meva == "sabs" or meva =="karam":
#         print(meva.upper())
#     else:
#         print(meva.title())

#2
from math import sqrt
# n =list(range(205,2024))
# print(n)
# for s in n:
#     if s < 1001:
#         print(s**3)
#     elif s  > 1500:
#         print(s-3)
# for i in n:
#     if i %25 == 0:
#         print(sqrt(i))
#3
# ball = int(input("Imtihon bahoyingizni kiriting:"))
# if  0 < ball   <= 20:
#     print("juda yomon")
# elif 21 < ball  < 35:
#     print("qoniqarli")
# elif 36 < ball  < 81:
#     print("yaxshi")
# elif  80 < ball  < 45:
#     print("juda yaxwi")
# elif 46 < ball  < 49:
#     print("Alo")
# elif ball == 50:
#     print("Excellent")
# else:
#     print("Iltimos 0 dan 100 gacha oraliqdagi son kiriting!")

""" 13 test """
#1
# ismlar =["olim","ali","guli","kamron","karim"]
# for ism in ismlar:
#     if ism == "karim" or ism == "kamron":
#         print(f"Salom {ism}  , ahvollaring yaxwimi")
#     else: 
#         print(f"Salom {ism}")
# #2
# for son in range(201,500,2):
#     if son  < 200 and son  > 300 :
#         print(son**4)
#     elif son  < 350 and son  > 400 :
#         print(sqrt(son))
#     elif son  < 420 and son  > 480 :
#         print(round(son/3.5),3)
#     else:
#         print(son**6)

# #3
# ball = int(input("Imtihon bahoyingizni kiriting:"))
# if  -1 < ball   < 41:
#     print("juda yomon")
# elif 40 < ball  < 61:
#     print("qoniqarli")
# elif 60 < ball  < 81:
#     print("yaxshi")
# elif  80 < ball  < 91:
#     print("juda yaxwi")
# elif 90 < ball  < 100:
#     print("Alo")
# elif ball == 100:
#     print("Excellent")
# else:
#     print("Iltimos 0 dan 100 gacha oraliqdagi son kiriting!")

""" 14 test """
# #1
# sonlar =list(range(3,322,2))
# for son in sonlar:
#     print(f"{son**5} ----- {son**7}")
#     print(f"{son-4} ---- {son+3}")
#     print(sqrt(son))
# print(len(sonlar))
# sonlar.sort()
# sonlar.sort(reverse=True)
# #2
# summa =0
# sonlar = [2,6,9,0,-9,7,8.5,7,6,-3,78]
# for son in sonlar:
#     summa = summa+son
# print(summa) 
# print(len(sonlar))
# print(max(sonlar))
# print(min(sonlar))
#3
# ombor = ["olma", "olcha", "gilos", "banan", "tarvuz", "malina", "qulubnay", "shaftoli"]
# xarid = int(input("\nNechta mahsulot sotib olmoqchisiz: "))
# bor = []
# yoq = []
# for x in range(xarid):
#     maxsulot = input(f"{x+1}- mahsulotni kiriting: ").lower()
#     if maxsulot in ombor:
#         bor.append(maxsulot)
#     else:
#         yoq.append(maxsulot)
# print(f"siz sotib olmoqchi bolgan mahsulotlar nomi:{ombor}")
# #4
# son = int(input("necta meva sotivb olmoqchisz:"))
# mevalar=[]
# sabzivotlar=[]
# for s in range(son):
#     mevalar.append(input(f"{s+1} meva nomini kiriting:"))
# sabzivotlar.append(mevalar)
# print(mevalar)

""" 15 test """
# #1
# son1 = int(input("1- son kiriting:"))
# son2 = int(input("2- son kiriting:"))
# son3 = int(input("3- son kiriting:"))

# sonlar =[son1,son2,son3,]
# print(min(sonlar))
# print(sum(sonlar))
# for son in sonlar:
#     if son > 0:
#         print(sonlar**3)

# #2
# son = int(input("Birinchi sonni kiriting:"))
# son1 = int(input("Ikkinchi sonni kiriting:"))
# if son > son1:
#     print(f"{son}  >  {son1}")
# elif son < son1:
#     print(f"{son}  <  {son1}")
# elif son == son1:
#     print(f"{son}  =  {son1}")

# #3
# ism = input("Ismingizni kiriting:")
# yosh =int(input(f"Salom {ism}. yoshingizni kiriting:"))
# if   yosh  >= 1 and yosh <= 6:
#     print( "Siz Bog'cha yoshidasiz! ✨✨✨")
# elif 7 <= yosh <= 17 :
#     print("Siz maktab o'quvchisiz.OK !😂😂😂")
#     if yosh == 7:
#         print("Siz 1-sinfda o'qiysiz😉")
#     elif yosh == 8:
#        print("Siz 2-sinfda o'qiysiz😢")
#     elif yosh == 9:
#       print("Siz 3-sinfda o'qiysiz😊")
#     elif yosh == 10:
#        print("Siz 4-sinfda o'qiysiz🎉")
#     elif yosh == 11:
#        print("Siz 5-sinfda o'qiysiz🤷")
#     elif yosh == 12:
#         print("Siz 6-sinfda o'qiysiz✌")
#     elif yosh == 13:
#        print("Siz 7-sinfda o'qiysiz.🤦‍♀️")
#     elif yosh == 14:
#         print("Siz 8-sinfda o'qiysiz❤💖.")
#     elif yosh == 15:
#         print("Siz 9-sinfda o'qiysiz💰.")
#     elif yosh == 16:
#         print("Siz 10-sinfda o'qiysiz💕.")
#     elif yosh == 17:
#         print("Siz 11-sinfda o'qiysiz💪.")
# elif 18 <= yosh <= 30:
#     print("Siz universitet talabasisiz. OK!🤣🤣🤣")
           
# elif 31 <= yosh <= 100:
#     print("Siz maktab o'quvchisi emassiz✨✨✨")
# else:
#     print("Siz noto'g'ri  son kiritdingiz😢😢.")

""" 16 test"""

#1
# son1 = int(input("1- son kiriting:"))
# son2 = int(input("2- son kiriting:"))
# son3 = int(input("3- son kiriting:"))

# sonlar =[son1,son2,son3,]
# print(min(sonlar))
# print(sum(sonlar))
# for son in sonlar:
#     if son > 0:
#         print(sonlar**3)

#2
# son = int(input("Birinchi sonni kiriting:"))
# son1 = int(input("Ikkinchi sonni kiriting:"))
# if son > son1:
#     print(f"{son}  >  {son1}")
# elif son < son1:
#     print(f"{son}  <  {son1}")
# elif son == son1:
#     print(f"{son}  =  {son1}")
#3
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

""" 17 test"""
# #2
# k= int(input("Bugun nechta kitob  ko'rmoqchisz:"))
# kitob = []
# for q in range(k):
#     kintob = input(f"{q+1} --> kino nomini kiriting:")
#     kitob.append(kintob)
# print(f"Bugun siz {len(kitob)} ta kino ko'rdiz. ")
# for s in kitob:
#     print(s)
# #1
# j =list(range(102,2020))
# for s in j:
#     if s < 1000:
#         print(s**7)
#     elif s > 1500:
#         print(s-4)  
# for i in j:
#     if i %19 == 0:
#         print(sqrt(i))

""" 18 mashq"""
#1
# lugat ={
#     "approximately":"taxminan",
#     "endepentdent":"ozodlik",
#     "beautiful":"chiroyli",
#     "ugly":"hunuk",
#     "difucult":"qiyin",
#     "easy":"oson"
# }
# savol = input("biror soz yoki manosi kiriting:").lower()
# for d,p in lugat.items():
#     if savol ==d:
#         print(f"{d.title()} -----  {p.title()}.")
#     elif savol ==p:
#         print(f"{p.title()} ----- {d.title()} .")

# if savol not in lugat.keys() and savol not in lugat.values():
#     print(f"Bizda bu {savol} haqida malumot  yoq:")


#2
# taomlar = {
#     'ali': 'osh',
#     'vali':'lagmon',
#     'ali':'osh',
#     'husan':'mastava',
#     'olim':'somsa',
#     'nodir':'kabob'
# }
# print(f"Alining sevimli taomi {taomlar['ali']}")

#3
# mahsulotlar ={ 
#     "non":50000,
#     "tuz":20000,
#     "qaymoq":300000,
#     "gosht":100000,
#     "qulupnay":25000,
#     "pitsa":150000,
#     "kalbasa":50000
# }
# for n , j in mahsulotlar.items():
#     print(f"\n {n} ----{j}")
# for d,g in mahsulotlar.values():
#     print(g)

""" 19 test """
#1
# son = int(input("Birinchi sonni kiriting:"))
# son1 = int(input("Ikkinchi sonni kiriting:"))
# if son > son1:
#     print(f"{son}  >  {son1}")
# elif son < son1:
#     print(f"{son}  <  {son1}")
# elif son == son1:
#     print(f"{son}  =  {son1}")
# #2
# sonlar = int(input("Ihtiyoriy son kiriting:"))
# if sonlar == 0:
#     print(f"{sonlar} --> bu son juft ham emas toq ham emas .OK!😊😊😊")
# elif sonlar%2==0:
#     print(f"{sonlar} -->  bu son juft .")
# elif sonlar%2 == 1:
#     print(f"{sonlar} --> bu son toq .")
#3
# toamlar={
#   "non":50000,
#     "tuz":20000,
#     "qaymoq":300000,
#     "gosht":100000,
#     "qulupnay":25000,
#     "pitsa":150000,
#     "kalbasa":50000
# }
# toamlar["toam4"]="manti"
# toamlar[input("Yangi key")]=input("Yangi value:")
# toamlar.update({"toam5":"norin"})
# print(toamlar)

"""  mashq """
# ball = int(input("Imtihon balingizni kiriting: "))
# orin = int(input("nechanci orinni oldingz."))
# if ball < 0 or ball > 100:
#     print("Siz noto'g'ri  ball kiritdingiz")
# elif ball >= 85:
#     elif orin ==1:
#         print("Siz GRANT yutib oldingiz  !")
# elif ball >= 60:
#     print("Siz imtihondan o'tdingiz")
# else:
#     print("Siz imtihondan o'ta olmadiz:(")



""" mashq"""

""" 1 mashq """
# son = list(range(22,926,2))
# print(son)
# for s in son:
#     print(f"{s} ---- {s**7}")

""" 2 mashq """
# ismlar =[]
# ismlar.append("nozima")
# ismlar.append("naima")
# ismlar.append("noila")

# ismlar.remove("noila")
# ismlar.remove("naima")
# del ismlar[0]

# ismlar.insert(0,"mubina")
# ismlar.insert(-1,"oydina")
# ismlar.insert(6,"hadicha")

# ismlar1 =[]
# ismlar.pop(0)
# ismlar.pop(-3)
# ismlar.pop(0)

# ismlar2=[]
# ismlar =ismlar2[:]
# print(ismlar)
# print(ismlar1)
# print(ismlar2)

"""3 mashq"""
#1
# users =["alisher","aziza","yasina","umar"]
# login=(input("yangi login tanglang:"))
# if login in users:
#     print(f"bu login band bowqa yangi login tanglang:")
#     users.append(login)
#     print(users)
# else:
#     print("xush kelibsz:")
#2
# sonlar = int(input("Ihtiyoriy son kiriting:"))
# if sonlar == 0:
#     print(f"{sonlar} --> bu son juft ham emas toq ham emas ")
# elif sonlar%2==0:
#     print(f"{sonlar} -->  bu son juft .")
# elif sonlar%2 == 1:
#     print(f"{sonlar} --> bu son toq .")

""" 4 mashq"""
# lugat ={
#     "easy":"oson",
#     "egg":"tuhum",
#     "ugly":"hunuk",
#     "word":"soz",
#     "and":"va",
#     "or":"yoki",
#     "slow":"sekin",
# }
# savol =input("biror ingliz tilida yoki ozbek tilida soz kiriting:")
# for eng,uzb in lugat.items():
#     if savol == eng:
#         print(f"{eng.title()} ----- {uzb.title()}")
#     elif savol == uzb:
#         print(f"{uzb.title()} ----- {eng.title()}")
# if savol not in lugat.keys() and savol not in lugat.values():
#     print(f"Siz kiritga bu {savol.title()} soz bizning lugatda yoq.")


# https://github.com/UlugbekXatamjonov/python-darslari.git 





















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































