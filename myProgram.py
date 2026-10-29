
def decision_helper():
    print("Welcome to Life Decision Helper!")

    item = input("What do you want to buy? ")
    price = float(input("How much is it? "))
    budget = float(input("What is your budget? "))
    importance = int(input("How important is it from 1 to 10? "))
    need = input("Do you really need it? (yes/no): ").lower()

    print("Your Decision:")
    print(f"Item: {item}")

    if price > budget:
        print("You don't have enough money for this purchase.")
    elif need == "yes":
        print("You should buy it because you need it.")
    elif importance >= 8:
        print("Go ahead and buy it!")
    elif importance >= 5:
        print("Maybe wait and think about it.")
    else:
        print("You should save your money.")

    if price <= budget:
        remaining = budget - price
        print(f"You will have ${remaining:.2f} left.")
    else:
        print("Try saving more money first.")

decision_helper()