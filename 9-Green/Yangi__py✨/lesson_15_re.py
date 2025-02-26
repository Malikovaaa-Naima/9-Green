"""
RegEx - Regular expression to match

"""
import re

# word1 = "python"
# word2 = "hello"
# word3 = "world"

# print(re.match("^p....n", word1))
# print(re.match("^h....l", word2))
# print(re.match("^w....d", word3))


"""  .............   """

# ism = input("ism kirit:")

# if re.match("^N",ism):
#     print(f"salom {ism} ,Ismingiz N harfdan boshlanadi.")
# else:
#     print(f"salom {ism}")

""" ............. """
# def telefon_raqami_kirit():
#     while True:
#         kiritilgan = input("Telefon raqamingizni kiriting: ")
#         # Telefon raqamini tekshirish uchun regex
#         if re.match(r'^\+998\d{9}$', kiritilgan):  # +998 bilan boshlanadigan 9 raqam
#             print(f"Telefon raqami to'g'ri: {kiritilgan} ✔")
#         elif re.match(r'^\d{9}$', kiritilgan):  # 9 ta raqam
#             print(f"Telefon raqami to'g'ri: {kiritilgan} ✔")
#         elif re.match(r'^\(\d{2}\)\s\d{3}-\d{2}-\d{2}$', kiritilgan):  # (XX) XXX-XX-XX formatida
#             print(f"Telefon raqami to'g'ri: {kiritilgan} ✔")
#         else:
#             print("Telefon raqami noto'g'ri formatda❌")

# telefon_raqami_kirit()

"""

^[+]998[\s][0-9]{2}[\s][0-9]{3}[-][0-9]{2}[-][0-9]{2}

^[+]998[\s][0-9]{2}[\s][0-9]{3}[\s][0-9]{2}[\s][0-9]{2}$

"""


"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp

"""

# shablon = "^[+]998[\s][0-9]{2}[\s][0-9]{3}[\s][0-9]{2}[\s][0-9]{2}$"
# tel = input("tel kiting:")

# if re.match(shablon,tel):
#     print("Telefon raqami to'g'ri")
# else:
#     print("Telefon raqami noto'g'ri")


# matn = """
#     assalomu aleykum naima@gmail.com
#     salomu aleykum malikova@gmail.com
#     albatta +998917602521

# """
# email_andoza ="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.findall(email_andoza,matn)
# print(email)


"""
regex funksiyalati 

findall() --- > barcha mosliklarni oz ichiga olgan royhatni qaytaradi
search() --- > agar strning istalgan joyida moslik mavjud bolsa,match obektni qaytaradi

"""








