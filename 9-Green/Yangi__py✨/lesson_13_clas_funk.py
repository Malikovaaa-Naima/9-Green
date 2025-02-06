# class Shaxs():
#     def __init__(self, ism:str, familiya:str,sharif:str, yosh:int, t_yil:int,passport:str,millat:str):
#       self.ism = ism
#       self.familiya = familiya
#       self.sharif = sharif
#       self.yosh = yosh
#       self.t_yil = t_yil
#       self.passport = passport
#       self.millat = millat

#     def __str__(self):
#         return f"{self.ism} {self.familiya} {self.sharif} "
#     def get_info(self):
#       """ shaxsni haqida to'liq malumot"""
#       return f"ABOUT ME \nmy name is: {self.ism}🎈, \nmy surname: {self.familiya}🎇 \nYear: my age {self.yosh} , my year {self.t_yil}✨ \nPassport: {self.passport}🎋 \nMillatim: {self.millat}💸"
    
#     def get_age(self,h_yil):
#       """ shaxsni yoshini topish"""
#       return h_yil-self.t_yil

#     def get_passport(self):
#       """ shaxsni passportni olish"""
#       return self.passport

#     def get_millat(self):
#       """ shaxsni millatni olish"""
#       return self.millat

# shaxs1 = Shaxs("Naima","Malikova","Murodovna",16,2009,"AC21323424","o'zbek")

# class Student(Shaxs):
#   def __init__(self, ism:str, familiya:str, sharif:str, yosh:int, t_yil:int, passport:str, millat:str,maktab,sinf,baholar):
#       """ shaxs"""
#       super().__init__(ism, familiya, sharif, yosh, t_yil, passport, millat)
#       self.maktab1 = maktab
#       self.sinf1 = sinf
#       self.baholar1 = baholar

      
#   def __str__(self):
#         return f"ismim-{self.ism} familyam-{self.familiya} sharifim-{self.sharif} "

#   def get_age(self,h_yil):
#       """ shaxsni yoshini topish"""
#       return f"{self.ism} {self.t_yil-self.t_yil}"

#   def get_passport(self):
#       """ shaxsni passportni olish"""
#       return f"{self.passport} pasportim"

#   def get_millat(self):
#       """ shaxsni millatni olish"""
#       return f"{self.millat} pasportim"

#   def maktab(self):
#       return f"My school: {self.maktab1}"

#   def baholar(self):
#     n=sum(self.baholar1)
#     return f"My score: {n}"



# student1 = Student("Naima","Malikova","Murodovna",16,2009,"AC21323424","o'zbek","Boborahim Mashrab",11,[5,5,5,5])

# # print(student1.get_age(2025))
# print(student1.get_info())
# print(student1.baholar())
# print(student1.maktab())



"""  
      texnika
  telefon    noutbook

"""
class Texnika():
    def __init__(self, model, yil, narxi,rang,kompaniya,muddat):
      self.model = model
      self.yil = yil
      self.narxi = narxi
      self.rang = rang
      self.kompaniya = kompaniya
      self.muddat = muddat

    def __str__(self):
        return f"{self.model} {self.yil} {self.narxi} {self.rang} {self.kompaniya} {self.muddat}"
    def get_info(self):
        """... """
        return f"\nTexnika model: {self.model}🎆, \nYil: {self.yil}🎇, \nNarxi: {self.narxi}💸, \nRang: {self.rang}🧶, \nKompaniya: {self.kompaniya}🎗, \nMuddat: {self.muddat}🎎"

    def get_narxi(self):
        return self.narxi
    def get_rang(self):
        return self.rang
    def get_kompaniya(self):
        return self.kompaniya
    def get_muddat(self):
        return self.muddat

class Telefon(Texnika):
    def __init__(self, model, yil, narxi, rang, kompaniya, muddat, razmer,telefon):
        super().__init__(model, yil, narxi, rang, kompaniya, muddat)
        self.razmer = razmer
        self.telefon = telefon

    def __str__(self):
        return f" Razmer: {self.razmer}, Telefon: {self.telefon}"
    def get_narxi(self):
        return f"{self.telefon} --->  {self.narxi}💸"
    def get_rang(self):
        return f"Rang: {self.rang}"
    def get_kompaniya(self):
        return f"Kompaniya: {self.kompaniya}"
    def get_muddat(self):
        return f"Muddat: {self.muddat} yil."
    def get_info(self):
        return f"\nTexnika model: {self.model}🎀, \nYil: {self.yil}🎄, \nNarxi: {self.narxi}$, \nRang: {self.rang}🎍, \nKompaniya: {self.kompaniya}🎇, \nMuddat: {self.muddat}🎈, \nRazmer: {self.razmer}✨, \nTelefon: {self.telefon}🎃"
    
class Noutbok(Texnika):
    def __init__(self, model, yil, narxi, rang, kompaniya, muddat, hotira):
        super().__init__(model, yil, narxi, rang, kompaniya, muddat)
        self.hotira = hotira
    def __str__(self):
        return f"Hotira: {self.hotira}"
    def get_narxi(self):
        return f"{self.narxi}🎗"
    def get_rang(self):
        return f"Rang: {self.rang}👓"
    def get_kompaniya(self):
        return f"Kompaniya: {self.kompaniya}🎡"
    def get_muddat(self):
        return f"Muddat: {self.muddat}yil"
    def get_info(self):
        return f"\nTexnika model: {self.model}🎀, \nYil: {self.yil}🎄, \nNarxi: {self.narxi}$, \nRang: {self.rang}🎍, \nKompaniya: {self.kompaniya}🎇, \nMuddat: {self.muddat}🎈, \nHotira: {self.hotira}📚"

        
h = Texnika("iphone 16",2024, 23_0000000,"och purple","apple","5 yil")
n = Telefon("Samsung Galaxy S22",2022, 15_0000000,"och blue","samsung",6.7,"6 yil", "+998912345678")
m = Noutbok("Noutbok",2022, 15_0000000,"qora","hp"," 3 yil","512GB")
print(h.get_info())
print(n.get_info())
print(m.get_info())













                                                         












