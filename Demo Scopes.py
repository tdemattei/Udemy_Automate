
# spam = 42   # Global Variable
#
# def eggs():
#     spam = 42   # Local Variable
#
# print("some code here")
# print("some more code here")

def spam():
    global eggs
    eggs = "hello"
    print(eggs)





eggs = 42
spam()
print(eggs)


