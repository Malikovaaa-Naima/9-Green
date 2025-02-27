"""https://www.tutorialsteacher.com/python/error-types-in-python"""

""" try - except"""
# try:
#     son = int(input("son kiriting:"))
#     print(f"{son} ning kvadrati {son**2} ga teng.")
# except:
#     print("Xatolik!")

# print("dasturning davomi.")
# print("dasturning davomi.")
# print("dasturning davomi.")

"""..... """
# try:
#     x = int(input(" son kiriting:"))
#     y = int(input(" son kiriting:"))
#     print(x/y)
# except ZeroDivisionError:
#     print("Xatolik!  0 ga bolib bolmaydi")
# except NameError:
#     print("Xatolik!  Bunday bir variable yo'q")
# except:
#     print("Xatolik!")

""" 1 mashq """
def cal(son1, son2,icon):
    """ hozir men calcu yasayman."""

    try:
        if icon == '+':
            return son1 + son2
        elif icon == '-':
            return son1 - son2
        elif icon == '*':
            return son1 * son2
        elif icon == '/':
            return son1 / son2
        else:
            return "Error! Bunday bir operator yo'q."
    except ZeroDivisionError:
        return "Error! 0 ga bolib bolmaydi."
    except TypeError:
        return "Error!"
    except KeyError as e:
        return f"Error! {str(e)}"
    






