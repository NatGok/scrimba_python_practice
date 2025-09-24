# ☕ Coffee Order Queue Challenge




# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 


# total_price = 0
# drink_count = 0
# available_drinks = ["latte", "americano", "espresso"]
# order = ""

# while True:
#     name=input("Welcome to the Coffee Shop! What's your name? ")
#     if name == "done":
#     break
# else:
#     order=input("input your drinks order")
#     if order not in available_drinks:
#         print("Sorry we don't have that drink, please choose from latte, americano, or espresso.")
#         continue
#     if order == "latte":
#         total_price += 3.50
#         drink_count += 1
#     elif order == "americano":
#         total_price += 3.00
#         drink_count += 1
#     elif order == "espresso":
#         total_price += 2.50
#         drink_count += 1


total_price = 0
drink_count = 0

while True:
    name = input("Enter customer name (or type 'done' to finish): ")
    
    if name == "done":
        break
        
    drink = input("Enter order for " + name + ": ")
    
    if drink == "latte":
        total_price += 3.50
        drink_count += 1
    elif drink == "americano":
        total_price += 3.00
        drink_count += 1
    elif drink == "espresso":
        total_price += 2.50
        drink_count += 1
    else:
        print(f"Sorry, {drink} is not on the menu.")
        continue
        
print("Order queue complete.")
print("Total drink ordered: ", drink_count)
print("Total price: $" + str(round(total_price, 2)))   