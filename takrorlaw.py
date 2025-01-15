# """ ----  9b001 ---- """
# #1
# ism = "naima"
# familiya ="malikova"
# yosh =15
# kitoblar = ["jjdhb","dfsh"]
# kasb ="oqituvchi"
# print(type(ism))
# print(type(familiya))
# print(type(kitoblar))
# print(type(yosh))
# print(type(kasb))

# #2
# from math import sqrt
# print(round(sqrt(4364+1233),2))

# #3
# son = int(input("son kiritying:"))
# son1 = int(input("son kiritying:"))
# print((son**son1)/23)

# #4
# s = float(input("son kirting:"))
# print(type(s))

# # 5
# kitoblar = []
# for s in range(5):
#     kitoblar.append(input("kitob nomini kiriting:"))

# print(kitoblar)

# #6
# ismlar =["ali","uhgy","fsgdb"]
# ismlar.insert(0,"fdshg")
# ismlar.insert(-1,"grthjn")
# ismlar["ali"]="dsafg"
# ismlar["ali"]="aedgjh"

# """ ---- 9B002 -----"""
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

# """ ---- 9B004 ----"""
# #1
# sonlar =[45,-96,0,63.2,1257,-6752,42,3,542]
# sonlar.sort()
# sonlar.sort(reverse=True)
# sonlar.reverse()
# #2
# mevalar =["olma","orik","shaftoli","apelsin","malina","xurmo"]
# for m in mevalar:
#     if m == "malina" or m =="olma":
#         print(m.lower())
#     else:
#         print(m.title())
# #3
# books={
#     "jih":"fsad",
#     "sfgdh":"adfsgjh"
# }
# books.update({'dghj':'fbgh'})
# books['jih'] = "Madina"
# print(books)

# books.update({'dghj':'fbgh'})
# books['jih'] = "Madina"
# print(books)

# del books["botirova"]
# books.pop("fazliddinova")
# books.popitem()

# books.clear()

# #4
# son = list(range(102,2020))
# for s in son:
#     if s >1000:
#         print(s**3)
#     elif s <1500:
#         print(s-4)
#     if s %7==0: 
#         print(sqrt(s))

# #5
# ball = int(input("Imtihon balingizni kiriting: "))
# orin = int(input("nechanci orinni oldingz."))
# if ball < 0 or ball > 100:
#     print("Siz noto'g'ri  ball kiritdingiz")
# elif ball >= 85:
#     if orin ==1:
#         print("Siz  1 orinni GRANT yutib oldingiz  !")
#     elif orin==2:
#         print("Siz  2 orinni GRANT yutib oldingiz  !")
#     elif orin ==3:
#         print("Siz  3 orinni GRANT yutib oldingiz  !")
#     elif orin == 4:
#         print("Siz  4 orinni GRANT yutib oldingiz  !")
# elif ball >= 60:
#     print("Siz imtihondan o'tdingiz")
# else:
#     print("Siz imtihondan o'ta olmadiz:(")


# """ ----- 9B005 -----"""
# #1
# lugat ={
#     "easy":"oson",
#     "or":"yoki",
#     "and":"va"
# }

# print(lugat.get(input("biror soz kiriting:"),"bunday soz mavjud emas:"))

# #2
# ovqat ={
#     "manti":15000,
#     "somasa":12000,
#     "osh ":15000,
#     "lagmon":45000
# }
# for k in ovqat.keys():
#     print(f"Bizda shu taomlar bor {k.title()}")
# for ovqat,narx in ovqat.items():
#     print(f"{ovqat} ----- {narx}")

# #3
# ism = input("Ismingizni kiriting:")
# yosh =int(input(f"Salom {ism}. yoshingizni kiriting:"))
# if   yosh  >= 1 and yosh <= 6:
#     print( "Siz Bog'cha yoshidasiz! ")
# elif 7 <= yosh <= 17 :
#     print("Siz maktab o'quvchisiz.OK !")
#     if yosh == 7:
#         print("Siz 1-sinfda o'qiysiz")
#     elif yosh == 8:
#        print("Siz 2-sinfda o'qiysiz")
#     elif yosh == 9:
#       print("Siz 3-sinfda o'qiysiz")
#     elif yosh == 10:
#        print("Siz 4-sinfda o'qiysiz")
#     elif yosh == 11:
#        print("Siz 5-sinfda o'qiysiz")
#     elif yosh == 12:
#         print("Siz 6-sinfda o'qiysiz")
#     elif yosh == 13:
#        print("Siz 7-sinfda o'qiysiz.")
#     elif yosh == 14:
#         print("Siz 8-sinfda o'qiysiz.")
#     elif yosh == 15:
#         print("Siz 9-sinfda o'qiysiz.")
#     elif yosh == 16:
#         print("Siz 10-sinfda o'qiysiz.")
#     elif yosh == 17:
#         print("Siz 11-sinfda o'qiysiz.")
# elif 18 <= yosh <= 30:
#     print("Siz universitet talabasisiz. OK!")
           
# elif 31 <= yosh <= 100:
#     print("Siz maktab o'quvchisi emassiz")
# else:
#     print("Siz noto'g'ri  son kiritdingiz.")

# #4
# green ={
#     'olimjanova':"Sarvinoz",
#     'malikova':"Naima",
#     'tohirova':"Rahima",
#     'botirova':"Hadicha"
# }


# savol = input("biror ism yoki familiya kiriting::").lower()
# for f,i in green.items():
#     if savol ==f:
#         print(f"{f.title()} ----- {i.title()}")
#     elif savol ==i:
#         print(f"{i.title()} ------  {f.title()} ")

# if savol not in green.keys() and savol not in green.values():
#     print(f"Bizda bu {savol} haqida malumot  yoq:")


# """ ----- 9b007 ---- """
# #1
# dost ={
#     "ism":"Mubina",
#     "yil":2007,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Mening dostimni ismi {dost['ism']} . dostim {dost['yil']} da tugulgan. {dost['shahar']} shahardada yashaydi . Manzil {dost['manzil']} .")

# """ ---- 9G001 ---- """
# #1
# m,n,f,c="naima","malikova","14","naima"
# print(m)
# print(n)
# print(f)
# print(c)
# #2
# print("Ahmadning yuvvosh mushugi meni kirsa doim yugurib keldi.")

# #3
# print(((93434+94903)-22344)+7363)

# #4
# ism = "naima"
# familiya ="malikova"
# yosh =15
# kasb ="oqituvchi"
# print(f"mening ismim {ism} ,familyam {familiya},{yosh}damn,")


# """  ----- 9G002 -----"""
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

""" mashq """
















