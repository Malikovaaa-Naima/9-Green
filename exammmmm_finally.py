# """ 9G 0001 """
# #1
# x,s,d,t = "olma","ol","naima","malikova"
# print(x,s,d,t)
# #2
# print("Ahmadning 'yuvvosh' mushugi meni ko'rsa ,doim yugurib keldi.")
# #3
# print(((93434+94903)-22344)+7363)
# #4
# ism ="naima"
# yosh = 15
# manzil ="Axsikent"
# maktab = "Boborahim Mashrab"
# sinf = " 9 GREEN"
# print(f" Ismim {ism},  {manzil}da yashayman , {maktab} da oqiyman, {sinf}sinfida oqiyman ")
# #5
# name ="NAIMA"
# surname ="MALIKOVA"
# fullname =f" {name} ,{surname}"
# print(fullname)
# #6
# gul  = "   BoyCHeCHak        "
# gul.lstrip()
# gul.strip()
# gul.title()
# gul.upper()
# gul.lower()

""" 9G 0002 """
# #1
# son1 =int(input("kirit"))
# son2 =int(input("kirit"))
# print(son1+son2)
# print(son1-son2)
# print(son1*son2)
# print(son1/son2)
# print(son1**2)
# print(son2**2)
# print(son1**3)
# print(son1**3)
# #2
# yil =2024
# yosh = int(input("yosh kirit:"))
# print(yil-yosh)

# #3
# matn1 = "bu mashq uchun berilgan matn"
# print(matn1.capitalize())

# matn2 ="aliSHer nAvoIy"
# print(matn2.lower())

# matn3= "boborahim mashrab"
# print(matn3.upper())

# matn4 = "aLIYEV vali"
# print(matn4.title())

# matn5 ="SolijoNOv JoniBEK"
# print(matn5.lower())

# matn6 ="    Assalomu aleykum"
# print(matn6.lstrip())

# matn7 ="Assalomu aleykum   "
# print(matn7.rstrip())

# matn8 ="    assalomu aleykum"
# print(matn8.strip())

# matn9 ="assalomu aleykum"
# print(matn9.title())

# matn10 ="BOBORAHIM MASHRAB"
# print(matn10.lower())
# #4
# print(round((231/4.7)*5))

# from math import sqrt 
# print((3**4+(sqrt(35345)))/8)

# import random
# print(random.randrange(20,80))

# r = input("radius kirit:")
# pi =3.14
# s =pi*r**2

# a =input("kava yuz kirit")
# s =a**2
# p=a*4
# #5
# uy_raqam =int(input("uy rqam kiriting:"))
# kocha =(input("kocha  kiriting:"))
# mahalla=(input("mahalal kiriting:"))
# tuman=(input("tuman  kiriting:"))
# viloyat =(input("viloyat  kiriting:"))
# print(f"{kocha} kocxhasi,{mahalla} mahallasi,{tuman}tumani,{viloyat}viloyatida yashaym,an.")

"""9G 0003 """
# #1
# import random
# so = int(input("son  kiriting:"))
# son = int(input("son  kiriting:"))
# print(random.randrange(so,son))

# #2
# kitobla =[]
# ism = input("ism kirit:")
# for s in range(5):
#     kitobla.append(input("kitob kirit:"))
# del kitobla[1]
# kitobla.insert(2,"dafg")
# kitobla.insert(3,"sdbvgf")

# #3
# fanlar =["matem","motam"]
# fanlar.append("nkjj")
# fanlar.insert(0,"svdbgf")
# fanlar["matem"]="aedgjh"
# fanlar["motam"]="afgfhgjh"
# del fanlar[0]
# fanlar.remove("afghfhhgjh")
# fanlar.pop()
# fan1 =  fanlar[:]
# fanlar.clear()

# #4
# family = []
# soni = int(input("nechtasila:"))
# for s in range(soni):
#     family.append(input("ism:"))
# print(family)

# #5
# cars =["bmw","mers","cobalt","nexxia"]
# print(len(cars))
# cars.sort()
# cars.sort(reverse=True)
# cars.reverse()
# print(cars)

""" 9G 0004 """
# #1
# son1 = int(input("so  krittng:"))
# son2 = int(input("so  krittng:"))
# son3 = int(input("so  krittng:"))

# print(max(son1,son2,son3))
# print(min(son1,son2,son3))
# print(sum(son1,son2,son3))

# #2
# sonlae = [213,34,5465,34,0,-54]
# sonlae.sort()
# sonlae.sort(reverse=True)
# sonlae.reverse()

# #3
# mavelar = ["olma","orik","olcha","tarvuz","malina"]
# for meva in mavelar:
#     if meva == "olma" or meva =="malina":
#         print(meva.upper())
#     else:
#         print(meva.title())

# #4
# son = int(input(" necta meva nomini kiritimoqchisz:"))
# mevalar = []
# for s in range(son):
#     meva = input("meva kiriting:")
#     mevalar.append(meva)
# print(mevalar)

# # 5
# son = int(input("Birinchi sonni kiriting:"))
# son1 = int(input("Ikkinchi sonni kiriting:"))
# if son > son1:
#     print(f"{son}  >  {son1}")
# elif son < son1:
#     print(f"{son}  <  {son1}")
# elif son == son1:
#     print(f"{son}  =  {son1}")

""" 9G0005 """
# #1
# from math import sqrt
# sonlar = list(range(3,873,2))
# for s in sonlar:
#     print(sqrt(s))

# #2
# ism = input("Ismingizni kiriting:").lower()
# if ism == "muslima":
#     print(f"Salom Muslima.Davramizda hush ko'rdik.")
# elif ism =="zilola" or ism == "sevara":
#     print("Assalomu aleykum . Sizga qanday yordam beriwim mumkin.")
# elif ism =="anvar" or ism == "aziz":
#     print("Salom . Bugun qayerga boramiz.")
# else:
#     print("Qalaysan")

# #3
# from math import sqrt
# sonlar = list(range(102,2020))
# for s in sonlar:
#     if  s < 1000:
#         print(s**3)    
#     elif s > 1500:
#         print(s-4)
#     if s % 7 == 0 :
#         print(sqrt(s))

# #4
# sonlar = list(range(-332,-2,3))
# for s in sonlar:
#     print(f" {s**5} va {s**7}")
#     print(s-4)
#     print(len(sonlar))
# sonlar.sort()
# print(sonlar)

# #5
# a = int(input("son kiriting:"))
# b = int(input("son kiriting"))

# if a > b:
#     print(f"{a} > {b}")
# elif a < b:
#     print(f"{a} < {b}")
# else:
#     print(f"{a} = {b}")

""" 9G0006"""
# #1
# sonlar = list(range(201,400,2))
# print(f" {sonlar}")

# sonlar = list(range(300,500,2))
# print(f" {sonlar}")

# #2
# country = ["Africa","Mexica","Rassiya","Chili","Uzbekistan","Koreya","Qatar","USA","Madakaskar","Qozogiston"]
# print(country)
# print(len(country))
# print(sorted(country))
# print(sorted(country,reverse=True))
# print(country)
# country.reverse()
# print(country)
# country.sort()
# country.sort(reverse=True)

# #3
# names = ["naima", "mubina"," mansura","al Availability"]
# s = input("ism kiritinh:")
# if s in names:
#     print("Bunday ism mavjud")
# else:
#     print("Hush kebsiz.")

# #4
# ombor_oquv = ["datar","ruchka","qalam","kitob","marker","lineka"]
# print(f"Bizda quidagi mahsulotlar bor: ", end="")
# for mahsulot in ombor_oquv:
#     if mahsulot == ombor_oquv[-1]:
#         print(f"{mahsulot}", end=". ")
#     elif mahsulot == ombor_oquv[0]:
#         print(mahsulot.title(), end=", ")
#     else:
#         print(f"{mahsulot}", end=",")

# xarid = int(input("\nNechta mahsulot sotib olmoqchisiz: "))
# bor = []
# yoq = []
# for x in range(xarid):
#     maxsulot = input(f"{x+1}- mahsulotni kiriting: ").lower()
#     if maxsulot in ombor_oquv:
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


""" 9G014CH2 """
# #1
# from math import sqrt
# for i in range(1,501):
#     if i <200:
#         print(f" {i} --->  daraja {i**2}")
#     elif i > 300:
#         print(f" {i} --->  ildiz {sqrt(i)}")

# #2
# freind =[ ]
# while True:
#     ism = input("ism kiriting: ciqish uchun exit yoki quit deng:")
#     if ism == "exit" or ism == "quit":
#         break
#     else:
#         freind.append(ism)
# print(freind)




















