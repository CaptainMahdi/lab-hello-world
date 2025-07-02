print("Hello from Mahdi's Code!")
print("---------------------")

name = input("Enter your name: ").lower()

if name == "mahdi":
    print("Hello Boss!")
else:
    print("Hello " + name + "!")
    
age = int(input("How old are you? "))
if 100 >age >= 18:
    print("You are an adult.")
elif age > 100:
    print("!!WOW " + name.upper() + " UR OLD!!")
elif age < 18:
    print("You are a minor.")
    
print("---------------------")

favlang = input("Whats your favorite coding language? ")

if favlang == "none":
    print("Thats alright " + name + ", codings not for everyone!")
else:
    print("Cool "+ name + ", " + favlang + " is a great language!")
print("---------------------")

if name == "mahdi" and age == 14:
    print("Identity confirmed. Welcome back Mahdi!")
else:
    print("You are all signed up, enjoy!")