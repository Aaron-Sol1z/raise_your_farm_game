import random

def animal_menu(inventory):
    print("_______________ANIMAL MENU______________")
    print(f"1. Milk {inventory.get("cows")} cows.")
    print(f"2. Collect eggs from {inventory.get("chickens")} chickens.")
    print(f"3. Shear {inventory.get("sheep")} sheep for fur.")
    print("________________________________________")

def cows(inventory):
    milk_quantity = 0
    for x in range(1, inventory["cows"] + 1):
        milk_quantity += random.randint(3, 7)
        print(f"Cow # {x}: total milk: {milk_quantity}")
    print(f"You milked {milk_quantity} gallons of milk!")
    inventory["milk"] += milk_quantity
    print(f"You now currently have {inventory.get("milk")} gallons of milk!")
    deplete_energy(inventory)

def chickens(inventory):
    egg_quantity = 0
    for x in range(1, inventory["chickens"] + 1):
        egg_quantity += random.randint(0, 2)
        print(f"Chicken # {x}: total eggs: {egg_quantity}")
    print(f"You collected {egg_quantity} eggs!")
    inventory["eggs"] += egg_quantity
    print(f"You now currently have {inventory.get("eggs")} eggs!")
    deplete_energy(inventory)

def sheep(inventory):
    fur_quantity = 0
    for x in range(1, inventory["sheep"] + 1):
        fur_quantity += random.randint(2, 25)
        print(f"Sheep # {x}: total pounds of fur: {fur_quantity}")
    print(f"You collected {fur_quantity} pounds of fur!")
    inventory["fur"] += fur_quantity
    print(f"You now currently have {inventory.get("fur")} pounds of fur!")
    deplete_energy(inventory)

def deplete_energy(inventory):
    inventory["energy"] -= 1
    print("You spent one energy.")

def animals(inventory):
    print("Welcome to the animal barn.")
    while True:
        try:
            animal_menu(inventory)
            animal_choice = int(input("You're checking on the animals. Which animal do you want to tend to (1, 2, 3)? "))
            if animal_choice in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.\n")
        except ValueError:
            print("Invalid input. You must enter a number.\n")
    if animal_choice == 1:
        print("Going to the cow barn.\n")
        cows(inventory)
    elif animal_choice == 2:
        print("Going to the chicken coop.\n")
        chickens(inventory)
    elif animal_choice == 3:
        print("Going to the sheep pen.\n")
        sheep(inventory)
