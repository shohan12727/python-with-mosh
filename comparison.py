temperature = 37 

if temperature < 40 :
    print("it's normal day")
else:
    print("it's a hot day summer")

name = input("enter your name ")
if len(name) == 3 :
    print("you are on right track")
else:
    print("you are not in a right track")


name = input ("enter your name: ")

if len(name) < 3 :
    print("your name must have three character")
elif len(name) > 50 :
    print("your name should not extend 50 character")
else:
    print("everything looks good.")
