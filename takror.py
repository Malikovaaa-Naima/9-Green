""" --------------------------------  Takrorlash -----------------------------"""
# def full_name(name:str,surname:str) -> str:
#     """ ....... """
#     full = f"{name} {surname}"
#     return full

# abror = full_name("Abror","Ahmedov")
# print(abror)

""" yosh top"""
# def yosh_top(ism:str,t_yil:int,h_yil=2024) -> str:
#     """ ........ """
#     """ 1 usul """
#     natija = f"{ism.title()}ning yoshi {h_yil-t_yil}da."
#     return natija

#     # """ 2 usul """
#     # return f"{ism.title()}ning yoshi {h_yil-t_yil}da."

# lola = yosh_top("Lola",2006)
# naima = yosh_top("Lola",2009,h_yil=2024)
# n = yosh_top("naima",2006,h_yil=2030)

# print(lola)
# print(naima)
# print(n)

""" eng katta sonni topish:"""
# def the_biggest(*sonlar:int) -> int:
#     """ .... """
#     x = sorted(sonlar)
#     return x[-1]
    
# numbers = the_biggest(2,43,213,-0,23243,67868786,21)
# print(numbers)

""" eng katta sonni topish:"""
# def the_biggest2(*sonlar:int) -> int:
#     """ .... """
#     maxium = 0
#     for number in sonlar:
#         if number > maxium:
#             maxium = number

#     return maxium
    
# numbers = the_biggest2(2,43,213,-0,23243,67868786,21)
# print(numbers)

""" eng kichik sonni topish:"""
# def the_smallest(*sonlar):
#     """ .... """
#     n = sorted(sonlar)
#     return n[0]

# number = the_smallest(2,43,213,-0,23243,67868786,21)
# print(number)


""" mashq """
# def the_len(*sonlar):
#     """ .... """
#     max = 0
#     for son in sonlar:
#          max+=1
#     return max

# number = the_len(2,43,213,-0,23243,67868786,21)
# print(number)

""" MASHQ """
# def range_the(start, stop):
#     return list(range(start, stop))
    

# n = range_the(5, 10)
# print(n)


""" MASHQ """
# def rng(son1:int,son2:int) -> int:
#     """ ..  """
#     sons = [son1]
#     return sons

""" mashq """
# def harf(letter:str)  -> int:
#     """  """
#     unli = ["a","i","o","u","e"]
#     if letter in unli:
#         return f" this letter is {letter} vowel"
#     else:
#         return f" this letter is  {letter} consanant"

# print(harf(input("enter some letter?")))



""" mashq """
# def my_orta(*numbers:int)->int:
#     """ """
#     summa = 0
#     count = 0

#     for s in numbers:
#         summa += s
#         count += 1
    
#     return summa/count

# print(my_orta(4,32,4,567,-4))
# print(my_orta(4,32,))

""" mashq """
from random import randrange
comp = randrange(1,10)
print("Kopmuter bir son oyladi 1,10 gacha ,siz taxmin qilib koring.")
savol = int(input("1,10 GACHA SON KIRITTING:"))
if savol >= 1 and savol <= 11:
    if comp == savol:
        print(f"Tebriklaymiz bildingiz!✔😁⭐")
    else:
        print(f"Xatolik!😂😊😒🤣 {comp} oyludi.")
else:
    print("Xatolik! Sizning kiritgan son 1-10 gacha bo'lishgacha kelibsiz.")


 

