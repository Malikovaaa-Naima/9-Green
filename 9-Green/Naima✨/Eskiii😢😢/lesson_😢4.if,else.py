""" if ,else --> new theme"""
# n = 778
# j = 784
# if n > j:
#     print(f"{n} > {j} dan katta")
# else:
#     print(f"{n} < {j} dan kichik")

ismlar = ["Asadbek","Bobur","Javohir","Akbar","Aziz","Husan"]
for ism in ismlar:
    if ism == "Javohir":
        print(f"Salom {ism}  , sizga yangi habar bor ")
    else:#else - yoki ,boshqa barcha holatlarda 
        print(f"Salom {ism}")

""" New thame:--> !="""
for ism in ismlar:
    if ism != "Javohir": #teng bo'lmasa
        print(f"Salom {ism} , Javohir keladimi? ")
    else:
        print(f"Salom {ism}")

# """ elif """
# sonlar = list(range(1,101))
# """
# 1 - 20   2
# 21 - 40  3
# 41 - 60   4 
# 61  - 101  5
# """
# for son in sonlar:
#     if son < 21:
#         print(f"{son} - 2 --> {son**2}")
#     elif son < 41:
#         print(f"{son} - 3 --> {son**3}")
#     elif son < 61:
#         print(f"{son} - 4 --> {son**4}")
#     else:
#         print(f"{son} - 5 --> {son**5}")

""" or va and """
ball = int(input("Imtihon balingizni kiriting: "))
if ball < 0 or ball > 100:
    print("Siz noto'g'ri  ball kiritdingiz")
elif ball >= 85:
    print("Siz GRANT yutib oldingiz !")
elif ball >= 60:
    print("Siz imtihondan o'tdingiz")
else:
    print("Siz imtihondan o'ta olmadiz:(")

""" or va and """
ball = int(input("Imtihon balingizni kiriting: "))
if ball < 0 or ball > 100:
    print("Siz noto'g'ri  ball kiritdingiz")
elif ball >= 85 and ball <=100:
    print("Siz GRANT yutib oldingiz 👏👏👏!")
elif ball >= 60 and ball <85:
    print("Siz imtihondan o'tdingiz")
else:
#     print("Siz imtihondan o'ta olmadiz:( ")

 """ % vs """
sonlar = list(range(1 , 100))
print(sonlar)
for son in sonlar:
    if son%2==0:  #juft sonalar  
    #if son%2==1: #toq sonlar
        print(son)



""" in - ichida """
mevalar = [ "olma" , "shaftoli", "gilos" , "tarvuz"]
sevimli = input("Yoqtirgan mevani kiriting:")

if sevimli in mevalar:
        print("Sizning mevavangiz dokonimizda bor :)")
else:
        print("Sizning mevavangiz dokonimizda  Yo'q :(")





















































