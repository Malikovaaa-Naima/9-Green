"""
NewThames:funksiya...
"""
# print("Hello world")

# def salom_ber():
#     print("Assalomu aleykum!")

# salom_ber()


# def yosh_top():
#     ism =input("ism kiriting:")
#     t_yil =int(input(f"{ism.title()} -- tugulgan yilingizni kiriting:"))

#     print(f"{ism.title()} --> siznin yoshingiz --> {2024-t_yil}da.")


# yosh_top()






""" docstring"""

# def yosh_top(t_yil): # parametr
#     """ tug'ilgan yilini qabul qilib olin yoshini hisablaydigan funksiya 
    
#     t_yil --> int
#     """

#     print(f" sizning yoshingiz {2024-t_yil} da")

# yosh_top(2012)
# yosh_top(2003)

# x= int(input("t yil kirit: "))
# yosh_top(x)


""" doc...."""
# print(print.__doc__)# double under score --> dunder metodi
# print(max.__doc__)

""" parametr key_word bn birga yoziw..."""
# def yosh_top(ism,t_yil):
#     print(f"salom {ism},siz {t_yil}da tugulgansizzz. ")

# yosh_top("Ali",t_yil=2012)

""" standart qiymat """
# def yosh_top(ism,t_yil=2000):
#     print(f"salom {ism},siz {t_yil}da tugulgansizzz. ")

# yosh_top("Ali",t_yil=2012)
    
""" Funksiyadan qiymat qaytariw"""
# def yosh_top(t_yil):
#     """ Tugulgan yilni qabul qilib olib yoshni qaytaradigan funksiya"""
#     yosh =2024-t_yil
#     return yosh

# naimaning_yoshi=yosh_top
# print(f"Naimaning yoshi {naimaning_yoshi} da.")


""" ......."""
# def yosh_top(t_yil:int,ism:str,oila:list) -> int: # t_yil - parametr
# def yosh_top(t_yil:int) -> int:
    # """ Tugulgan yilni qabul qilib olib yoshni qaytaradigan funksiya"""
#     yosh =2024-t_yil
#     return yosh #return ---> qaytariw

# naimaning_yoshi=yosh_top
# print(f"Naimaning yoshi {naimaning_yoshi} da.")


""" funksiya ichida --- dictionary"""
# def person(name:str,surname:str,age:int,email:str,phone:int):
#     person = {
#     "name": name,
#     "surname":surname,
#     "age":age,
#     "email":email,
#     "phone":phone
#     }
#     return person

# naima = person("Naima","Malikova",15,"naimamalikova75@gmail.com",336162521)
# print(naima)

""" info haqida tuwunca """
# def info(name:str,age:int,sinf="9 green",) -> str: # sinf = "9 green" -- > standart qiymat
#     """ """
#     return f"{name.title()} your age {age} , your class{sinf}"
# student1 =info(sinf="10 green ",age=16,name="Abbos ")# keyword bilab parametr beriw


""" *arg usuli"""
def my_sum(*sonlar): # *arg

    summa = 0
    for son in sonlar:
        summa = summa+son
    return summa

# print(my_sum(4,32,4,567,-4))
# print(my_sum(4,32,))
# print(my_sum())















  