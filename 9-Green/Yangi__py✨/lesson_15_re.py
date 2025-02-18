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
def telefon_raqami_kirit():
    while True:
        kiritilgan = input("Telefon raqamingizni kiriting: ")
        # Telefon raqamini tekshirish uchun regex
        if re.match(r'^\+998\d{9}$', kiritilgan):  # +998 bilan boshlanadigan 9 raqam
            print(f"Telefon raqami to'g'ri: {kiritilgan} ✔")
        elif re.match(r'^\d{9}$', kiritilgan):  # 9 ta raqam
            print(f"Telefon raqami to'g'ri: {kiritilgan} ✔")
        elif re.match(r'^\(\d{2}\)\s\d{3}-\d{2}-\d{2}$', kiritilgan):  # (XX) XXX-XX-XX formatida
            print(f"Telefon raqami to'g'ri: {kiritilgan} ✔")
        else:
            print("Telefon raqami noto'g'ri formatda❌")

telefon_raqami_kirit()


















