
def hello(name):    # define a function
    print("Hello!", name)
    return "Bye"


hello("Tom")     # Call function several times
hello("Peter")
hello("Bill")
a = hello("Sam")
print(a)

def plus_one(number):   # define a function
    return number + 1   # tell function to return a value

new_number = plus_one(10)    # Run Fuction and pass it a argument
print(new_number)   # Print value returned by plus_one function

print("Hello", end=" ")     # replaces return at end of print statement with another character
print("World")

print("one", "two", "three", sep=" - ")     # replaces space as separator value







