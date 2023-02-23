pizzaType = " " 
pizzaTypelist = ["Pizza", "Pineapple", "Vegemite"] 
name = input("Enter your name:")

print("Hello, " + name)
# Standard input line 
print("Type your favourite colour:")
colour = input()
"""
werqwdqwdwerwer
qwdqd
qwdqwqdqw
dw
wdq
wdqwd
"""
print("Your favourite colour is " + colour)
# Changing position to see if order matters -> It does had to change vars and print 
print(f"Choose your pizza type: {pizzaTypelist}")

pizzaType = input()

while pizzaType not in pizzaTypelist:
    print("Gotta choose on the list man...")
    pizzaType = input()
    print("test")

#Choose from options only - gotta make into loop or something 

while True:
    pQuan = input("How many pizzas u want? ")

    try:
        pQuan = int(pQuan)

        if pQuan <0:
            print("give NUMBERS")
            continue

        break

    except ValueError:
        print("NOT A NUMBER")
        
print("you want to order", pQuan, "pizzas")

#FUCKMANN
