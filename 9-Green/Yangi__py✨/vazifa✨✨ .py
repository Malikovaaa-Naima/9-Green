# """ vazifa """
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



# """ vazifa"""
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



# """ vazifa """
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

""" vazifa """
"""
2) yuqoridagi shaxs classidan bowqa turli voris klasslar yaratib 
koringlar (masalan o'qituvchi, sotuvchi , mijoz )
har bir klassga oziga hos xususiyat va metodlar yasang.

"""
class Mubina():
    def __init__(self, ism:str, familiya:str,sharif:str, yosh:int, t_yil:int,passport:str,millat:str):
      self.ism = ism
      self.familiya = familiya
      self.sharif = sharif
      self.yosh = yosh
      self.t_yil = t_yil
      self.passport = passport
      self.millat = millat

    def __str__(self):
        return f"{self.ism} {self.familiya} {self.sharif} "
    def get_info(self):
      """ shaxsni haqida to'liq malumot"""
      return f"ABOUT HER \nher name is: {self.ism}🎈, \nher surname: {self.familiya}🎇 \nYear: her age {self.yosh} , her year {self.t_yil}✨ \nPassport: {self.passport}🎋 \nNationality: {self.millat}💸"
    
    def get_age(self,h_yil):
      """ shaxsni yoshini topish"""
      return h_yil-self.t_yil

    def get_passport(self):
      """ shaxsni passportni olish"""
      return self.passport

    def get_millat(self):
      """ shaxsni millatni olish"""
      return self.millat

shaxs1 = Mubina("Mubina","Isaqjanova","Elyorbek qizi",18,2007,"AC21323424","o'zbek")

class Student(Mubina):
  def __init__(self, ism:str, familiya:str, sharif:str, yosh:int, t_yil:int, passport:str, millat:str,maktab,sinf,kasb,sertifikat):
      """ shaxs"""
      super().__init__(ism, familiya, sharif, yosh, t_yil, passport, millat)
      self.maktab1 = maktab
      self.sinf1 = sinf
      self.kasb1 = kasb
      self.sertifikat1 = sertifikat

  def maktab(self):
      return f"Her school: {self.maktab1}"

  def sinf(self):
    return f"Her class: {self.sinf1}"
  def set_sinf(self):
      if self.sinf1 < 11:
          self.sinf1 += 1
          return f"she is in {self.sinf1} class now"
      else:
          return "you finish the school , Goodbye👋"
  
  
  def kasb(self):
      return f"She is {self.kasb1}."

  def serificat(self):
      return f"Her certificate: {self.sertifikat1}"
    
    

odam = Student("Mubina","Isaqjanova","Elyorbek qizi",18,2007,"AC21323424","o'zbek",68,11," Arababic teacher","from arabic certificate B2")

print(odam.get_info())
print(odam.sinf())
print(odam.set_sinf())
print(odam.serificat())
print(odam.maktab())














