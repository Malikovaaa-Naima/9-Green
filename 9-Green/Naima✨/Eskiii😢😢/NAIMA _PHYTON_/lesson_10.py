# """Int()-> natijani butun son qlb beradi"""

#yosh = int(input("yoshingizni kiriting:"))
#print(type(yosh))

#tyil = 2023 - yosh
#print(f"Men {tyil} da tugilgansz")

# tyil2 = int(input("Yilizni kiriting:"))
# yosh2 = 2023 - tyil2

# print(f"Sizning yoshiz {yosh2} da")


# """11 DARS"""
from  math  import sqrt
# son = int(input("biror son kiriting biz uni kavdrsi va ildizini aniqlab beramiz:"))
# print(f"siz kiritgan {son} soni, kvadrati {son**2} va ildizi {sqrt(son)} shu.")
# son1 = int(input("birorta son kiriting:")) 
# son2 =int(input("yana son kiriting:"))
# print(f"ayirma {son1 - son2}")
# print(f"qoshish {son1 +son2}")
# print(f"bolish {son1 / son2}")
# print(f"kopaytma {son1*son2}")
# print(f"ildiz {sqrt(son1 + son2)}")
# print(f"daraja {son1**son2}")
""" Sonni kvga va kubga ko'tarish """
number = int(input("Biror son kiriting: "))
kv = number**2
kub = number**3
print(f"Siz kiritgan {number} sonining kvadrati {kv} ga kubi esa {kub} ga teng")

""" Kvadratning perimetri va yuzi  """
kvadrat = int(input("Kvadratning tomonini kiriting: "))
yuza = kvadrat**2 # S=a**2
per = kvadrat*4 # P=a*4
print(f"Tomoni {kvadrat} ga teng bo'lgan kvadratning yuzi {yuza} ga,\
perimetri esa {per} ga teng bo'ladi. ")

a = int(input(" 1 chi son kiriting:"))
b = int(input(" 2 ci  son kiriting:"))
c = sqrt(a**2 + b**2)
print(f" Natija {c} ")

""" len() funksiyasi """
parol = input("Parol kiriting: ")
print(len(parol))
# print(f"Siz kiritgan parolning uzunligi {len(parol)} ga teng")

""" replace() """
x = "Sarvinoz Oydina Rahima Mohlaroy Naima Xadicha Oydina"

print(x.replace("Oydina", "Madina"))
print(x.replace(" ", ", "))








