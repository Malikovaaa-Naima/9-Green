""" Tashqi Kutbuhonalar """
""" datetime()"""
import datetime

now = datetime.datetime.now()

# print(f"Year: {now.year}")
# print(f"Month: {now.month}")
# print(f"Weekday: {now.weekday()}")
# print(f"Day: {now.day}")
# print(f"Hour: {now.hour}")
# print(f"Minute: {now.minute}")
# print(f"Second: {now.second}")
# print(f"Microsecond: {now.microsecond}")


""" 

link -> https://docs.python.org/3/library/datetime.html
link -> https://www.w3schools.com/python/python_datetime.asp

"""
# print(now.date()) #sana
# print(now.strftime("%Y"))
# print(now.strftime("%B"))
# print(now.strftime("%A"))
# print(now.strftime("%C"))



""" sanadan sanini ayiriw"""
# bugun = datetime.datetime.today()
# ramozon = datetime.datetime(2025,3,1)
# print(ramozon-bugun)


""" vaqtdan vaqtni ayiriw"""
# bugun1=datetime.datetime.now()
# ramozon1= datetime.datetime(2025,3,1,00,00,1)

# print(bugun1)
# print(ramozon1)

# farq = ramozon1-bugun1
# print(farq)
# print(farq.days)
""" ....."""
t_sana = datetime.datetime(2009,11,23,3,0,0)
print(t_sana)

print(t_sana+datetime.timedelta(days=23,hours=2))

