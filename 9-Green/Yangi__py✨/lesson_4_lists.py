""" Ro'yhat elementlari o'zgartirish"""
# darslar = ["python"]
# print(darslar)
# darslar[0]="Telegaram bot"
""" bir ro'yhatni ikkinchisiga qo'shish extend()"""
# subject = ["Matematika","Rus tili","Ingliz tili","Arab tili","Koreys tili"]
# fan = ["Matematika","Koreys tili "]
# subject.extend(fan)
# print(subject)
# print(fan)

""" New theme:"""
# """ .append() - ro'yhatga elemnt qoshadigan royhat"""
# fanlar = ["Matematika","Rus tili","Ingliz tili","Arab tili","Koreys tili"]
# fanlar.append("Jismoniy tarbiya")
# fanlar.append("Koreys tili")
# fanlar.append("Informatika")
# fanlar.append("Ona tili")
# print(fanlar)

""" New theme"""
# """insert() - royhattagi elementti istalgan yeriga qoshib beriladi"""
# fanlar.insert(1,"Algebra")
# fanlar.insert(23,"QWERTY")
# print(fanlar)

""" New theme"""
# """ . remove() -> elementlarni o'chirish:"""
# fanlar.remove("Matematika")                                                                                                                                                                                                                                          
# fanlar.remove("Rus tili")
# print(fanlar)

""" New theme"""
""" . del() -> royhatdan elementni indexini bo'yicha o'chiradi."""
# del fanlar[0]
# del(fanlar[1])
# print(fanlar)


""" .pop() - > royhatdan elementni sugiurib oluvchi metod"""
""" Agar pop() ga index bermasah u royhat oxiridagi indexni aftomatika oladi"""
# sinfdowlar = ["Ulugbek","Rahima","Guljahon","Sarvinoz","Gulwoda"]
# sinfdowlar.pop(1)
# sinfdowlar.pop(1) 
# print(sinfdowlar)

""""""

""" New theme """
""" list() -> royhat shaklantiriw ucun funksiya """
# country = list() # royhat yaratiw
# davlatlar = []   #bow royhat
# print(country)
# print(davlatlar)

""" New theme """
""" .clear() royhatni  tozalaw elementlardan"""
# fruits = ["apple","banana","cherry"]
# print(fruits)
# fruits.clear()
# print(fruits)

""" range() -> sonli oraliq shakilantiriw ucun funksiya """
# sonlar1 = list(range(1, 10000000))
# sonlar2 = list(range(1,100))
# print(sonlar1)
# print(sonlar2)


""" royhatdan nusxa olish"""
# sonlar = list(range(1,30))
# print(sonlar)
# sonlar2 = sonlar [10:20]
# sonlar2 = sonlar [:]
# sonlar2 = sonlar [:20]
# sonlar2 = sonlar [10:]
# print(sonlar2)        


""" New theme """
""" .sort ()"""
# name = [ "Olim","Ali","Momin","Malika","Kamola"]
# print(name)
# name.sort()#togri tartiblash
# print(name)
# name.sort(reverse=True)#teskari tartibda tartiblash
# print(name)

""" .sorted() -> royhatni bir marta alifbo boyicha tartiblab beradi"""
# print(name)
# print(sorted(name))#togri tartibda
# print(sorted(name,reverse=True))#teskari tartibda

""" .reserve() -> royhatni bowi va  oxirini aylantirib konsulga chiqaruvchi 
# funksiya ."""
# country = [ "uzbek","russian","albanian"]
# print(country)
# country.reverse() # royhatni bowi va  oxirini aylantirib konsulga chiqaramiz
# print(country)

""" range()"""
# number = list(range(1,21))
# print(number)

""" max() , min() , sum() funksiyalar"""
# print(max(number))# eng katta soni topib beradi
# print(min(number))# eng kichik soni topib beradi
# print(sum(number))# yig'indini  topib beradi





























