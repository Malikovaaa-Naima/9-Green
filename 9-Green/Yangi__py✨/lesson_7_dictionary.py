""" 
Thame:Dictionary(Lugatlar)
"""
# taomlar ={
#     'ali':'osh',
#     'vali':'manti',
#     'hasan':'lagmon',
#     'olim':'somsa',
#     'nodir':'kabob'
# }

"""
taomlar ={'ali':'osh'}
nomi = {'key':'value'}
"""
# print(taomlar)
# print(type(taomlar))


# print(taomlar['ali'])
# print(f"Olimning sevimli taomi {taomlar['olim']}")

# buyumlar ={
#     "ism":"Ali",
#     "yosh":23,
#     "student":True,
#     "oila":["ota","ona","aka"]
# }
# print(buyumlar)

green_9 ={
    'olimjanova':"Sarvinoz",
    'malikova':"Naima",
    'tohirova':"Rahima",
    'botirova':"Hadicha"
}

""" element qowiw"""
# green_9[input("Familya kiriting:").lower()] = input('ism kiriiting:')
# print(green_9)

# green_9.update({'mamadova':'Masrura'})
# print(green_9)

# green_9['fazliddinova'] = "Madina"
# print(green_9)

""" elementni qiymatini yangilaw """
# green_9.update({'mamadova':'Masrura'})
# print(green_9)

# green_9['fazliddinova'] = "Mubina"
# print(green_9)

""" elementni ochiriw"""
# del green_9["botirova"]

# green_9.pop("fazliddinova")

# green_9.popitem()

# print(green_9)

""" lugatni  tozalaw"""
# green_9.clear()
# print(green_9)

""" nusxa oliw"""
# math_student =green_9.copy()
# print(math_student)

# math_student_2 =dict(green_9)
# print(math_student_2)

"""get metodi """
# print(green_9['abdulahad'])
# print(green_9.get("abdulahad","Bunday ism yoq"))
# print(green_9.get(input("key kiriting:"),"bunday ism yoq"))

""" keys ,values,items ---  metodlari"""
# green_9 ={
#     'olimjanova':"Sarvinoz",
#     'malikova':"Naima",
#     'tohirova':"Rahima",
#     'botirova':"Hadicha"
# }

# print(green_9.keys())
# print(green_9.values())

# print(f"9 green sinfida quidagi oquvchilar bor:",end="")
# for familiya in green_9.keys():
#     print(familiya,end=" ")

# print(f"9 green sinfida quidagi oquvchilar bor:",end="")
# for ismlar in green_9.keys():
#     print(ismlar,end=" ")

""" items() - metodi """
# print(green_9.items())
# for key,value in green_9.items():
#     print(f"{key.title()} -----> {value.title()}")

""" ..... """
# eng_uz = {
#     "apple":"olma",
#     "bread":"non"
# }

# word = input("soz kiriting:").lower()
# for key ,value in eng_uz.items():
#     if word == key:
#         print(f"{key} ---- {value}")
#     elif word == value:
#         print(f"{value} ---- {key}")
# if word not in eng_uz.keys() and word not in eng_uz .values():
#     print("Bizda bu soz haqida malumot yoq....")






