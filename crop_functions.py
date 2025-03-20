import random

def crop_menu(inventory):
    print("_______________CROP MENU________________")
    print(f"1. Harvest {inventory.get("veggie_acres")} vegetable acres.")
    print(f"2. Harvest {inventory.get("fruit_acres")} fruit acres.")
    print(f"3. Plant {inventory.get("veggie_seeds")} vegetables and {inventory.get("fruit_seeds")} fruit.")
    print("________________________________________")

def crop_compute(acre_quantity):
    crop_quantity = 0
    for x in range(1, acre_quantity + 1):
        crop_quantity += random.randint(1, 5)
    return crop_quantity

def harvest(crop_choice, inventory):
    if crop_choice == 1:
        acre_quantity = inventory["veggie_acres"]
    elif crop_choice == 2:
        acre_quantity = inventory["fruit_acres"]
    if acre_quantity == 0:
        print("There is nothing left to harvest. Consider planting more seeds.\n")
    else:
        current_crop_harvest = crop_compute(acre_quantity)
        print(f"You harvested {current_crop_harvest} crates of food!")
        if crop_choice == 1:
            inventory["veggie_yield"] += current_crop_harvest
            inventory["veggie_acres"] = 0
            print(f"You now have a total of {inventory.get("veggie_yield")} crates of vegetables!\n")
        elif crop_choice == 2:
            inventory["fruit_yield"] += current_crop_harvest
            inventory["fruit_acres"] = 0
            print(f"You now have a total of {inventory.get("fruit_yield")} crates of fruit!\n")
        deplete_energy(inventory)

def seeds(inventory):
    if inventory["veggie_seeds"] == 0 and inventory["fruit_seeds"] == 0:
        print("You have no seeds to plant. Consider buying more from the town.\n")
    else:
        if inventory["veggie_seeds"] == 0:
            print("You have no vegetable seeds to plant.\n")
        else:
            inventory["veggie_acres"] += inventory["veggie_seeds"]
            inventory["veggie_seeds"] = 0
        
        if inventory["fruit_seeds"] == 0:
            print("You have no fruit seeds to plant.\n")
        else:
            inventory["fruit_acres"] += inventory["fruit_seeds"]
            inventory["fruit_seeds"] = 0
        print("Your seeds have been planted.")
        print(f"You currently have {inventory.get("veggie_acres")} acres of vegetables and {inventory.get("fruit_acres")} acres of fruit.\n")
        deplete_energy(inventory)

def deplete_energy(inventory):
    inventory["energy"] -= 1
    print("You spent one energy.")

def crops(inventory):
    print("Welcome to the crop fields.")
    while True:
        try:
            crop_menu(inventory)
            crop_choice = int(input("You're checking on your crops. What would you like to do (1, 2, or 3)? "))
            if crop_choice in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    if crop_choice == 1:
        print("Going to harvest vegetables.\n")
        harvest(crop_choice, inventory)
    elif crop_choice == 2:
        print("Going to harvest fruit.\n")
        harvest(crop_choice, inventory)
    elif crop_choice == 3:
        print("Planting all seeds.\n")
        seeds(inventory)
