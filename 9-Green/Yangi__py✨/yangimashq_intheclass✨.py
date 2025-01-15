
"""ozim ucun mashq"""
#  1) otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta 
#     m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida 
#     konsolga chiqaring 

# 2) Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
#     Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# 3) Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z(atamani) kiriting 
#     (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

# 4) Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
#     Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

# 6) Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va 
#     qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
  

""" 1 mashq """
# otam = {
#     "ism":"Murodbek",
#     "yil":1984,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Otamning ismi {otam["ism"]} . Otam {otam["yil"]} da tugulgan. {otam["shahar"]} shahardada yashaydi . Manzil {otam["manzil"]} .")

# onam ={
#     "ism":"Nodira",
#     "yil":1990,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Onamning ismi {onam["ism"]} . Onam {onam["yil"]} da tugulgan. {onam["shahar"]} shahardada yashaydi . Manzil {onam["manzil"]} .")

# ukam ={
#     "ism":"Ozodbek",
#     "yil":2014,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Ukamning ismi {ukam["ism"]} . ukam {ukam["yil"]} da tugulgan. {ukam["shahar"]} shahardada yashaydi . Manzil {ukam["manzil"]} .")



# ukam1 ={
#     "ism":"Asadbek",
#     "yil":2017,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Ukamning ismi {ukam1["ism"]} . ukam {ukam1["yil"]} da tugulgan. {ukam1["shahar"]} shahardada yashaydi . Manzil {ukam1["manzil"]} .")

""" 2 mashq """
# taomlar ={
#     "ali":"manti",
#     "naima":"somsa",
#     "rahima":"norin",
#     "mubina":"ramyon",
# }
# print(f"Alining sevimli taomi {taomlar["ali"]}")
# print(f"naimaning sevimli taomi {taomlar['naima']}")
# print(f"rahimaning sevimli taomi {taomlar['rahima']}")
# print(f"mubinaning sevimli taomi {taomlar['mubina']}")

""" 3 mashq """
# python={
#     "if":"agar",
#     "else":"yana",
#     "float":"onlik son",
# }


""" mashq """
# phone0 = {
#         'model':'iphone15 pro',
#         'rang':'binafsha',
#         'yil':2023,
#         'narh':163000000,
#         'hotira':'256gb'
#         }

# phone1 = {
#        'model':'redmi 10 a',
#         'rang':'qora',
#         'yil':2019,
#         'narh':190800000,
#         'hotira':'128gb'
#         }

# phone2 = {
#        'model':'samsung a52',
#         'rang':'Titanium gray',
#         'yil':2023,
#         'narh':1379900000,
#         'hotira':'512gb'
#         }



# phones = [phone0,phone1,phone2]
# for p in phones:
#     print(f"{p['model'].title()}, "
#           f"{p['rang']} rang, "
#           f"{p['yil']}-yil, {p['narh']}$")

""" mashq """
# oilalar = {
# 	'oila1':{
# 		'ota':{
# 			'ism':"Murodjon",
#             'familya':"Mamathanov",
#             'yosh':'40',
#             'kasb':"Biznessman",
# 		},
# 		'ona':{
# 			'ism':'Nodira',
#             'familya':"Sharipova",
#             'yosh':'34',
#             'kasb':"uy bekasi",
# 		},},
# 	'oila2':{
# 		'ota':{
# 			'ism':"Murodjon",
#             'familya':"Mamathanov",
#             'yosh':'40',
#             'kasb':"Biznessman",
# 		},
# 		'ona':{
# 			'ism':'Nodira',
#             'familya':"Sharipova",
#             'yosh':'34',
#             'kasb':"uy bekasi",
# 		},
# 		}
# }


# for a,b in oilalar.items():
# 	print(a.upper())
# 	for parents,info in b.items():
# 		print(parents.upper())
# 		for key,value in info.items():
# 			print(f"{key} ----- {value}")





""" mashq """

# dostalar = {
# 	'sinfdoshlar':{
# 		'rahima':['hotdog','osh','norin'],
#         'muhammadyusuf':['gamburger','lavash','chizburger'],
#         'abdulahad':['kabob','somsa','norin']
# 	},
# 	"dostlar":{
# 		'mohlaroy':['qazi','somsa','norin'],
# 		'xadicha':['ramyon','kuksi','norin'],
# 		'oydina':['palov','jarkob','somsa']
# 	},
	
# }

# for n,m in dostalar.items():
# 	print(f"\n--------------{n.title()}-------------------")
# 	for ism,s in m.items():
# 		print(f"\n {ism.title()}", end=": ")
# 		for k in s:
# 			print(f"{k}",end=", ")




""" mashq """
""" 1 """
# while True:
#     paroll = input("Yangi parol kiriting:")
#     if len(paroll) >= 8 :
#         parol2 = input("Qayta kiriting:")
#         if  paroll == parol2:
#             print("Parol tasdiqlandi✔:")
#             break
#         else:
#             print("Parol tasdiqlanmadi.🤣🤣🤣")
#             print("Qaytaadan urinib ko'ring!")
#     else:
#         print("Parolingiz kamida 8 ta harfdan iborat bo'lishi kerak....")

""" 2 """
# parol = "naima"
# while True:
#     parol1 =input("Biror parol kiriting:")

#     if parol1 == parol:
#         print("Siz muvaqiyatli kirdingiz❣.")
#         break
#     elif parol:
#         print(f"{parol1} hato❌.")


""" mashq """
# while True:
#     savol =(input("yoshingizni yoki tugulgan yilingizni kiriting:(chiqish ucn \"exit\")"))
#     if savol =="exit":
#         break
#     elif savol.isdigit():
#         yosh_t=int(savol)
#         yil=2024 - yosh_t
#         print(f"sinning yoshingiz {yil}")
#     else:
#         print(f"faqat son kiritish mumkin emas:")

""" mashq """
# urunish = 0
# parol = "naima"
# while True:
#         savol =input("Parol kiriting:")
#         if savol == parol:
#             print("Siz parol muvaqqiyatli kirdi!✔😊🌹")
#             break
#         elif savol!= parol:
#               urunish += 1
#         if urunish>= 3:
#             while True:
#                 print("Siz parolni topa olmadingiz ! xixixixixixi🤣😂👌😜")

""" mashq """
# son =int(input("necha marta yuguriw kereak:"))     
# print("Biz yugurishni boshladik:")
# for s in list(range(son)):
#     print(f"{s+1} ---- aylana tugadi!")
# print("Biz yuguriwni tugaddik!")

# n =input("Otisak boladimi!")
# if n == "ha":
#     print("Rahmat!😍 .Bu kunlarni qanchadan beri kutgandim.🐱‍🏍😉💕👍")
# elif n == "yoq":
#     print("Yana qancha yuguriw kerak😒")

""" mashq """
# yow = int(input("Nech yoshsz ? "))
# if yow >= 1 and yow <=7:
#     print("Sizga bepul")
# elif yow >= 8 and yow <=18:
#     print("Sizga 100$ dollor")
# elif yow >= 19 and yow<=70:
#     print("Sizga 500$ dollor ")
# elif yow >= 70 and yow <=100:
#     print("Sizga BEPUL...xixxixixxii😉")
# elif yow <0:
#     print(f"Bu musbat son emas.👌👌👌😒🤣🤣")
# else:
#     print("Siz notugri son kiritingiz.")

""" mashq"""
# summa = 0
# j = int(input("How many person? :"))
# for n in range(j):
#     people = int(input("How old are you ? :"))
#     if people < 0 or people > 100:
#             print("You entered an incorrect score.")
#     elif   people  <= 0 or people <= 7:
#                 print( "Free for you! Please enter!✨✨✨")
#     elif 8 <= people <= 18 :
#                 print("20,000 soums for you. OK!😂😂😂")
#                 summa = summa + 20_000
#     elif 19 <= people <= 69:
#                 print("60,000 soums for you. OK!🤣🤣🤣")
#                 summa = summa + 60_000
#     elif 70 <= people <= 100:
#                 print("Free for you! Please enter!✨✨✨")
#     else:
#                 print(f"{people} is not a positive number.👌👌👌😒🤣🤣")
# print(f"The entry price for you was a total of {summa} soums.❗❗💰💰. ")

""" mashq"""
# otam = {
#     "ism":"Murodbek",
#     "yil":1984,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
#     "kasb":"buznissman"
# }

# print(f"Otamning ismi {otam['ism']} . Otam {otam['yil']} da tugulgan. {otam['shahar']} shahardada yashaydi . Manzil {otam['manzil']} . Kasblari {otam['kasb']}.")

# onam ={
#     "ism":"Nodira",
#     "yil":1990,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
#     "kasb":"uy bekasi"
# }

# print(f"Onamning ismi {onam['ism']} . Onam {onam['yil']} da tugulgan. {onam['shahar']} shahardada yashaydi . Manzil {onam['manzil']} . Kablari {onam['kasb']}")

# ukam ={
#     "ism":"Ozodbek",
#     "yil":2014,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Ukamning ismi {ukam['ism']} . ukam {ukam['yil']} da tugulgan. {ukam['shahar']} shahardada yashaydi . Manzil {ukam['manzil']} .")

# ukam1 ={
#     "ism":"Asadbek",
#     "yil":2017,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Ukamning ismi {ukam1['ism']} . ukam {ukam1['yil']} da tugulgan. {ukam1['shahar']} shahardada yashaydi . Manzil {ukam1['manzil']} .")

""" mashq"""
# lugat ={
#     "if":"agar",
#     "else":"aks holda",
#     "clear":"tozalamoq"
# }

# print(lugat.get(input("key kiriting:"),"bunday soz yoq"))

""" mashq"""
# dost ={
#     "ism":"Mubina",
#     "yil":2007,
#     "shahar":"Namangan",
#     "manzil":"Ahsikent",
# }

# print(f"Mening dostimni ismi {dost['ism']} . dostim {dost['yil']} da tugulgan. {dost['shahar']} shahardada yashaydi . Manzil {dost['manzil']} .")

""" mashq """
# davlatlar ={
#     "usa":"washington",
#     "turkey":"ankara",
#     "uzbekiston":"toshkent",
#     "fransiya":"parij",
#     "uk":"london",
# }
# davlatlar.update({'qatar':'doga'})
# print(davlatlar)

# davlatlar['koreya'] = "seul"
# print(davlatlar)

# del davlatlar["koreya"]

# davlatlar.pop("qatar")

# davlatlar.popitem()


# naima =davlatlar.copy()
# print(naima)

# naima2=dict(davlatlar)
# print(naima2)

""" mashq """#1
# davlatlar={
#     "korea":"soul",
#     "fransiya":"parij",
#     "USA":"Washington",
#     "Turkey":"Ankara",
#     "Uzbekiston":"Toshkent",
#     "Fransiya":"Parij",
#     "UK":"London",
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

""" mashq """#2
# davlatlar={
#     "korea":"soul",
#     "fransiya":"parij",
#     "USA":"Washington",
#     "Turkey":"Ankara",
#     "Uzbekiston":"Toshkent",
#     "Fransiya":"Parij",
#     "UK":"London",
# }

# for davlat in sorted(davlatlar.keys()):
#    print(davlat.title())

# for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt.title())

""" mashq"""
# green_9 ={
#     'olimjanova':"Sarvinoz",
#     'malikova':"Naima",
#     'tohirova':"Rahima",
#     'botirova':"Hadicha"
# }

# savol = input("biror ism yoki familiya kiriting::").lower()
# for f,i in green_9.items():
#     if savol ==f:
#         print(f"{f.title()} ----- {i.title()}")
#     elif savol ==i:
#         print(f"{i.title()} ------  {f.title()} ")

# if savol not in green_9.keys() and savol not in green_9.values():
#     print(f"Bizda bu {savol} haqida malumot  yoq:")

""" mashq """
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



""" mashq """
# import random
# ismlar =["naima","hadicha","sarvinoz","rahima","mohlaroy","oydina","mubina","muhammadyusuf","abdulahad","zinnur"]
# shartlar=["tozalov","100 marta otirib turish","snikers olb berish","prisedanya","matemdan vazifa qiliw","salfetka olb keliw"]


# print(ismlar[random.randrange(0, len(ismlar))])
# print("--------")
# print(shartlar[random.randrange(0, len(shartlar))])

# for m in range(3):
#     print("⭐ ⭐ ⭐")
#     for n in range(3):
#         print("⭐")
#         for m in range(3):
#             print("⭐ ⭐ ⭐")


""" mashqlar """
# yil = 2024
# while True:
#     yosh =int(input("yosh kiriting:"))
#     s = yil-yosh
#     print(f"sizning {s} shu yildasz:")

#     savol = input("chiqishni hohlsysimi(exit/quit):").lower()
#     if savol=="quit" or savol =="exit":
#         print("Dastur tugadi❗❕")
#         break


""" ---- mashqlar ----"""
"""
Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va 
chipta narhini chiqarsin.


Foydalanuvchi exit yoki quit deb yozganda dastur 
to'xtasin (ikkita shartni ham tekshiring).  
"""
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
# x =0
# parol1="www"
# while True:
#     if len(parol1) >= 3 :
#             x += 1
#             parol2 = input("parol kiriting:")
#             if  parol1 == parol2:
#                     print("Parol tasdiqlandi✔ .Hush kelibsz!")
#                     break
#             if x>=3:
#                 while True:
#                     print("Parol tasdiqlanmadi.🤣🤣🤣")
#                     print("Qaytaadan urinib ko'ring!")
  

# """ 1 --> mashq """
# print(len.__doc__)
# print(max.__doc__)
# print(sum.__doc__)
# print(range.__doc__)
# print(list.__doc__)
# """ 2 --> mashq """
# def ball():
#     ball = int(input("Imtihon bahoyingizni kiriting:"))
#     if  0 < ball   < 50:
#         print("Qoniqarsiz😒")
#     elif 51 < ball  < 70:
#         print("qoniqarli😉")
#     elif 71 < ball  < 90:
#         print("yaxshi😁")
#     elif  91 < ball  < 101:
#         print("alo⭐")
#     else:
#         print("Iltimos 0 dan 100 gacha oraliqdagi son kiriting!")

# # ball()
# """ 3 --> mashq """
# def t_burchak(p,s):
#     print(f"Tomonlari {p} va {s} tortburchakning yuzi {p*s} ga perimetri esa {2*(p+s)} ga teng")

# t_burchak(4,5)
# """ 4 --> mashq """ 
# son=[23,-1,2,545,78]
# def tartib(qiymat):
#     qiymat.sort()
#     print(qiymat)
# tartib(son)


# """ 1 --> mashq """

# def family(mother:str,father:str,brother:str,brorher1:str,me:str):
#     family1 = {
#     "mother": mother,
#     "father":father,
#     "brother":brother,
#     "brother1":brorher1,
#     "me":me
#     }
#     return family1

# naima = family("Nodira","Murodbek","Asadbek","Ozodbek","Naima")
# # print(naima)

# for s,n  in  naima.items():
#     print(f" ------ {s} ------")
#     print(f"        {n}      ")


# """ birost mashq """
# def baholash (ismlar):
#     baholash={}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"talaba {ism.title()}ning bahosini kiriting:")
#         baholash[ism]=baho
#     return baholash

# talabalar =["ali","vali","hasan"]
# baholash =baholash(talabalar)
# print(baholash)

# """ mashq """
# royhat_mowin =["m004qa","f778aa","009ans","505zzz"]
# def mowin():
#     print(royhat_mowin)



# """ mashq """
# def sonl(son:int):
#     """ """
#     return list(range(0,son,2))
# s = sonl(100)
# print(s)

""" mashq """








