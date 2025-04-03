import random
import animal_functions
import crop_functions
import town_functions

def intro():
    print("You are starting a farm of your own, but you have no crew.")
    print("All you have are a few animals, crops, and $5000.")
    print("But you're a hard working person.")
    print("You have six months to make a profit and establish yourself as one of the greatest farms in existence.\n")

def breakdown(months, inventory):
    print(f"Month {months+1}")
    print(f"Your balance is ${inventory.get("balance")}")
    print("You have:")
    list(inventory)

def list(inventory):
    print("🐾____________________ANIMALS____________________🐾")
    print(f"Barn: {inventory.get("cows")} 🐄 cows | {inventory.get("chickens")} 🐔 chickens | {inventory.get("sheep")} 🐑 sheep")
    print(f"Yield: {inventory.get("milk")} 🥛 gallons of milk | {inventory.get("eggs")} 🥚 eggs | {inventory.get("fur")} 🧵 pounds of fur")
    print("🐾_______________________________________________🐾\n")
    print("🌾_____________________CROPS_____________________🌾")
    print(f"Acres: {inventory.get("veggie_acres")} 🥕 acres of vegetables | {inventory.get("fruit_acres")} 🍏 acres of fruit")
    print(f"Seeds: {inventory.get("veggie_seeds")} 🌱🥕 vegetable seeds | {inventory.get("fruit_seeds")} 🌱🍏 fruit seeds")
    print(f"Yield: {inventory.get("veggie_yield")} 🥕 crates of vegetables | {inventory.get("fruit_yield")} 🍏 crates of fruit")
    print("🌾_______________________________________________🌾\n")

def restock(stock):
    stock["store_cows"] += random.randint(1, 2)
    stock["store_chickens"] += random.randint(6, 24)
    stock["store_sheep"] += random.randint(1, 3)
    stock["store_veggie_seeds"] += random.randint(2, 4)
    stock["store_fruit_seeds"] += random.randint(1, 3)
    print("The store has restocked.\n")
    print("🏬____________________STORE____________________🏬")
    print(f"Animals: {stock.get("store_cows")} 🐄 cows | {stock.get("store_chickens")} 🐔 chickens | {stock.get("store_sheep")} 🐑 sheep")
    print(f"Seeds: {stock.get("store_veggie_seeds")} 🌱🥕 vegetable seeds | {stock.get("store_fruit_seeds")} 🌱🍏 fruit seeds")
    print("🏬_____________________________________________🏬\n")

def results(inventory):
    print("The game is over. In the end, you have:")
    list(inventory)
    print(f"You ended with ${inventory.get("balance")}")
    if inventory["balance"] >= 10000:
        print("Great job! You made a HUGE profit!")
    elif inventory["balance"] > 5000:
        print("Nice! You made profit.")
    elif inventory["balance"] <= 5000:
        print("Oof. You lost money. That's okay, farming is hard work.")
    elif inventory["balance"] <= 0:
        print("You're bankrupt. That's a lot of paperwork in the future.")

def menu():
    print("_______________MAIN MENU________________")
    print("1. Check on the animals.")
    print("2. Tend to the crops.")
    print("3. Go into town.")
    print("________________________________________\n")

def main():
    months = 0
    inventory = {
        "balance": 5000,
        "energy": 0,
        "cows": 3,
        "chickens": 24,
        "sheep": 6,
        "milk": 0,
        "eggs": 0,
        "fur": 0,
        "veggie_acres": 1,
        "fruit_acres": 1,
        "veggie_yield": 0,
        "fruit_yield": 0,
        "veggie_seeds": 1,
        "fruit_seeds": 1
        }
    stock = {
        "store_cows": 1,
        "store_chickens": 6,
        "store_sheep": 2,
        "store_veggie_seeds": 4,
        "store_fruit_seeds": 3
        }
    intro()

    while months != 1:
        inventory["energy"] = 4
        breakdown(months, inventory)
        restock(stock)
        while inventory["energy"] != 0:
            while True:
                print(f"You have {inventory.get("energy")} energy left.\n")
                menu()
                try:
                    menu_choice = int(input("What do you want to do today (1, 2, 3)? "))
                    if menu_choice in [1, 2, 3]:
                        break
                    else:
                        print("Invalid input. Please enter 1, 2, or 3.\n")
                except ValueError:
                    print("Invalid input. You must enter a number.\n")
            if menu_choice == 1:
                print("🐾 Heading to the animal barn. 🐾\n")
                animal_functions.animals(inventory)
            elif menu_choice == 2:
                print("🌾 Heading to the crop fields. 🌾\n")
                crop_functions.crops(inventory)
            elif menu_choice == 3:
                print("🏬 Heading into town. 🏬\n")
                town_functions.town(inventory, stock)
                # inventory["energy"] -= 1
        months += 1
    results(inventory)

if __name__ == "__main__":
    main()