
# def div42by (number):
#     try:
#         return 42 / number
#     except ZeroDivisionError:
#         print("Error: you tried to divide by zero.")
#
#
# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

print("How many cats do you have?")
numcats = input()
if int(numcats) >= 4:
    print("That is a lot of cats")
else:
    print("That is not very many cats")
