""" 1) foydalanuvchi tugilgan kuni,oyi va yili sorab ,
unga tugulgan vaqtidan ayni vaqtgacha otgan
vaqtini soat va minutini aniqlikda hisob qaytaring.

Namuna: Siz tug'ulgan 15 yilu, 20 kun bo'ldi
"""

# import datetime

# def otgan_kunlar(yil:int,oy:int,kun:int):
#     """
#     bu funksiyani butun sinf bn qildik 🎇🎃
#     """

#     t_yil = yil
#     t_oy = oy
#     t_kun = kun
#     t_sana = datetime.date(yil,oy,kun)
#     bugun =datetime.date.today()


#     if (bugun-t_sana).days <=365:
#         return f"Siz tugulganizga {(bugun-t_sana).days} kun bo'ldi💫 "

#     elif bugun.month > t_oy:
#         yil = bugun.year - t_yil
#         kun = bugun - datetime.date(bugun.year,t_oy,t_kun)
#         return f"Siz tugulganizga {yil} - yilu , {kun.days} kun buldi💨 "

#     elif bugun.month == t_oy:
#         if bugun.day < t_kun:
#             yil = bugun.year - t_yil -1
#             kun = bugun - datetime.date(bugun.year-1,t_oy,t_kun)
#             return f"Siz tugulganizga {yil}-yilu , {kun.days} kun buldi 💥 "

#         elif bugun.day == t_kun:
#             yil = bugun.year - t_yil
#             return f"Siz bugun  {yil} yoshga to'ldingiz .Tabriklaymiz🎉🎊"

#         else:
#             yil = bugun.year - t_yil
#             kun = bugun - datetime.date(bugun.year,t_oy,t_kun)
#             return f"Siz tugulganizga {yil} - yilu , {kun.days} kun buldi🧶."

#     else:
#         yil = bugun.year - t_yil -1
#         kun = bugun - datetime.date(bugun.year-1,t_oy,t_kun)
#         return f"Siz tugulganizga {yil} - yilu , {kun.days} kun buldi💎."


# yil = int(input("Tug'ulgan yilingizni kiriting:"))
# oy = int(input("Tug'ulgan oyingizni kiriting:"))
# kun = int(input("Tug'ulgan kuningizni kiriting:"))

# user = otgan_kunlar(yil,oy,kun)

# print(user)




"""   2 mashq yoshni hisoblovchi 2 mashq 2 hil usulda"""
# t_yil = int(input("yilning kirit:"))
# t_oy = int(input("oyni kiriting:"))
# t_kun = int(input(" kunni kiriting:"))


# t_yil = 2009
# t_oy = 11
# t_kun = 23

# t_sana = datetime.date(t_yil,t_oy,t_kun)
# bugun = datetime.date.today()



# if bugun.month > t_oy:
#     yil = bugun.year - t_yil
#     kun = bugun - datetime.date(bugun.year,t_oy,t_kun)
#     print(f" siz tugulgan {yil} - yilu , {kun.days} kun buldi🎇")

# elif bugun.month == t_oy:
#     if bugun.day >= t_kun:
#         yil = bugun.year - t_yil -1
#         kun = bugun - datetime.date(bugun.year-1,t_oy,t_kun)
#         print(f"siz tugulganizga {yil}-yilu , {kun.days} kun buldi📞")
#     else:
#         yil = bugun.year - t_yil 
#         kun = bugun - datetime.date(bugun.year,t_oy,t_kun)
#         print(f"siz tugulganizga {yil}-yilu , kun buldi🎈.")

# else:
#     yil = bugun.year - t_yil -1
#     kun = bugun - datetime.date(bugun.year-1,t_oy,t_kun)
#     print(f"siz tugulganizga {yil}-yilu , {kun.days} kun buldi🎀")




""" 3 mashq """

import datetime


# bugun = datetime.date.today()
 
# oy = int(input("oy kiriting:"))
# kun = int(input("kun kiriting:"))

# sana1s = datetime.date(bugun.year,oy,kun)
# sana2 = datetime.date(bugun.year+1,oy,kun)


# if sana1 > bugun:
#     print(f"Sizning tug'ilgan kuningizga {(sana1-bugun).days} kun qoldi.")
# elif sana1 < bugun:
#     print(f"Sizning tug'ilgan kuningizga {(sana2-bugun).days} kun qoldi.")

# else:
#     print("Bugun sizning tug'ilgan kuningizni nishonlanmoqda🎉🎊🥳")



""" 4 mashq """
# bugun = datetime.date.today()
# kun = int(input("Necha kundan keyingi sanani bilmoqchisiz:"))
# sana = bugun + datetime.timedelta(days= kun)

# print(sana)
















