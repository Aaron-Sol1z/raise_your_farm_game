def town_menu():
    print("_______________TOWN MENU________________")
    print(f"1. Buy animals")
    print(f"2. Buy seeds")
    print(f"3. Sell total yield")
    print("________________________________________")

def buy_animals(inventory, stock):
    if stock["store_cows"] == 0 and stock["store_chickens"] == 0 and stock["store_sheep"] == 0:
        print("Sorry. There are no animals left in stock. Check back next week.\n")
    else:
        if stock["store_cows"] == 0:
            print("There are no cows in stock.\n")
        else:
            print("Browsing cows.")
            checkout("cows", inventory, stock, "store_cows", "cows")
        if stock["store_chickens"] == 0:
            print("There are no chickens in stock.\n")
        else:
            print("Browsing chickens.")
            checkout("chickens", inventory, stock, "store_chickens", "chickens")
        if stock["store_sheep"] == 0:
            print("There are no sheep in stock.\n")
        else:
            print("Browsing sheep.")
            checkout("sheep", inventory, stock, "store_sheep", "sheep")
        deplete_energy(inventory)

def buy_seeds(inventory, stock):
    if stock["store_veggie_seeds"] == 0 and stock["store_fruit_seeds"] == 0:
        print("Sorry. There are no bags of seed left in stock. Check back next week.\n")
    else:
        if stock["store_veggie_seeds"] == 0:
            print("There are no bags of vegetable seeds in stock.")
        else:
            checkout("bags of vegetable seeds", inventory, stock, "store_veggie_seeds", "veggie_seeds")
        if stock["store_fruit_seeds"] == 0:
            print("There are no bags of fruit seeds in stock.")
        else:
            checkout("bags of fruit seeds", inventory, stock, "store_fruit_seeds", "fruit_seeds")
        deplete_energy(inventory)

def checkout(item_name, inventory, stock, stock_key, inventory_key):
    checkout = 0
    if item_name == "bags of vegetable seeds":
        indiv_cost = 100
    elif item_name == "bags of fruit seeds":
        indiv_cost = 150
    elif item_name == "cows":
        indiv_cost = 900
    elif item_name == "chickens":
        indiv_cost = 15
    elif item_name == "sheep":
        indiv_cost = 300
    while True:
        try:
            print(f"{item_name} = ${indiv_cost}")
            print(f"Current balance: ${inventory.get("balance")}.")
            print(f"{stock.get(stock_key)} {item_name} in stock.")
            buy_choice = int(input("Enter the amount you want to buy. "))
            if buy_choice in range(0, stock[stock_key] + 1):
                inventory[inventory_key] += buy_choice
                stock[stock_key] -= buy_choice
                checkout = buy_choice * indiv_cost
                print(f"You bought {buy_choice} {item_name} for ${checkout}.\n")
                inventory["balance"] -= checkout
                break
            elif buy_choice > stock[stock_key]:
                print(f"The store doesn't have {buy_choice} of these in stock.\n")
            elif buy_choice < 0:
                print("You cannot enter a negative number.\n")
        except ValueError:
            print("Invalid choice. You must enter a number.\n")

def sell(inventory):
    print("________________RECEIPT_________________")
    earnings = 0
    balance = inventory["balance"]
    #milk
    milk_sell = inventory["milk"] * 4
    earnings += milk_sell
    print(f"{inventory.get("milk")} milk ------ ${milk_sell}.")
    inventory["milk"] = 0
    # eggs
    eggs_dozen = inventory["eggs"] // 12
    eggs_remainder = inventory["eggs"] - (eggs_dozen * 12)
    eggs_dozen_sell = eggs_dozen * 7
    eggs_remainder_sell = eggs_remainder * 0.5
    earnings += eggs_dozen_sell + eggs_remainder_sell
    print(f"{eggs_dozen} dozen eggs ------ ${eggs_dozen_sell}.")
    print(f"{eggs_remainder} individual eggs ------ ${eggs_remainder_sell}.")
    inventory["eggs"] = 0
    # fur
    fur_sell = inventory["fur"] * 8
    earnings += fur_sell
    print(f"{inventory.get("fur")} pounds of fur ------ ${fur_sell}.")
    inventory["fur"] = 0
    # vegetable crates
    veggie_sell = inventory["veggie_yield"] * 50
    earnings += veggie_sell
    print(f"{inventory.get("veggie_yield")} crates of vegetables ------ ${veggie_sell}.")
    inventory["vegetables_yield"] = 0
    # fruit crates
    fruit_sell = inventory.get("fruit_yield") * 80
    earnings += fruit_sell
    print(f"{inventory.get("fruit_yield")} crates of fruit ------ ${fruit_sell}.")
    inventory["fruit_yield"] = 0
    print(f"You sold everything and earned ${earnings}.\n")
    # balance += earnings
    # inventory["balance"] = balance
    inventory["balance"] += earnings
    deplete_energy(inventory)

def deplete_energy(inventory):
    inventory["energy"] -= 1
    print("You spent one energy.")

def town(inventory, stock):
    print("Welcome to the town.")
    while True:
        try:
            town_menu()
            shop_choice = int(input("You're in the local store. What would you like to do (1, 2, 3)? "))
            if shop_choice in [1, 2, 3]:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    if shop_choice == 1:
        print("Buying animals.\n")
        buy_animals(inventory, stock)
    elif shop_choice == 2:
        print("Buying seeds.\n")
        buy_seeds(inventory, stock)
    elif shop_choice == 3:
        print("Selling yield.\n")
        sell(inventory)