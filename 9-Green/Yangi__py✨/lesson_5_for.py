# """ 
# Thame: for operatori
# """

# """ 
#     for tsikli ketma -ketlikni takrorlash uchun ishlatiladi.
#     For tsili yordamida biz ro'yhatdagi har bi element ucun
#     bir martadan ,qandaydur kodni bajarishingiz mumkin.

# """

# """ for operatori"""
# ismlar = ["Ali","Bobur","Ravshan","Olim","Hasan","Husan"]
# print(f"Salom, {ismlar[1]} ,Ahvolaring yaxshimi ?")
# for ism in ismlar:
#     print(f"Salom, {ism} ,Ahvolaring yaxshimi ?")
# print("Men do'sting Naima")

# """________________________________________________________"""

# mehmonlar = ["Ali","Bobur","Ravshan","Olim","Hasan","Husan"]
# for ism in mehmonlar:
#     print(f"Salom,{ism} sizni 10-aprel hayit bayramiga taklif qilamn.")
# print("Men do'sting Naima")

# """________________________________________________________"""

# ism = "Azizbek"
# for i in ism:
#     print(i)


"""  Oila azolari"""
oila = int(input("Oila ozalaringizni kiriting:"))
oila1 = []
for n in range(oila):
    ism1 = input(f"{n+1} - ismni kiriting:")
    oila1.append(ism1)
print(f"Sizning oilangizda {len(oila1)} ta inson bor: Ular:" ,end=" ")
for ism in oila1:
    print(f"{ism.title()}" , end=", ")


















