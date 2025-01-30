"""        
thame: The name of the class 
"""
class Shaxs():
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
      return f"ABOUT ME \nmy name is: {self.ism}🎈, \nmy surname: {self.familiya}🎇 \nYear: my age {self.yosh} , my year {self.t_yil}✨ \nPassport: {self.passport}🎋 \nMillatim: {self.millat}💸"
    
    def get_age(self,h_yil):
      """ shaxsni yoshini topish"""
      return h_yil-self.t_yil

    def get_passport(self):
      """ shaxsni passportni olish"""
      return self.passport

    def get_millat(self):
      """ shaxsni millatni olish"""
      return self.millat

shaxs1 = Shaxs("Naima","Malikova","Murodovna",16,2009,"AC21323424","o'zbek")

class Student(Shaxs):
  def __init__(self, ism:str, familiya:str, sharif:str, yosh:int, t_yil:int, passport:str, millat:str,maktab,sinf,baholar):
      """ shaxs"""
      super().__init__(ism, familiya, sharif, yosh, t_yil, passport, millat)
      self.maktab1 = maktab
      self.sinf1 = sinf
      self.baholar1 = baholar
  def maktab(self):
      return f"My school: {self.maktab1}"

  def sinf(self):
    return f"My class: {self.sinf1}"
  def set_sinf(self):
      if self.sinf1 < 11:
          self.sinf1 += 1
          return f"I'm in {self.sinf1} class now"
      else:
          return "you finish the school , Goodbye👋"
  
  
  def baholar(self):
    n=sum(self.baholar1)
    return f"My score: {n}"



student1 = Student("Naima","Malikova","Murodovna",16,2009,"AC21323424","o'zbek","Boborahim Mashrab",11,[5,5,5,5])

# print(student1.get_age(2025))
print(student1.get_info())
print(student1.sinf())
print(student1.set_sinf())
print(student1.baholar())
print(student1.maktab())












