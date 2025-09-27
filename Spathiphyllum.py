#customer guesses the computer's favourite plant
#the computer responds based on the user's input


customer_choice=input("Can you guess the computers favourite plant? ")
if customer_choice == "spathiphyllum":
    print("Not quite I need a capital S in the name of the plant Spathiphyllum")
elif customer_choice == "Spathiphyllum": 
    print("Yes - Spathiphyllum is the best plant ever!")
else: 
    print("Spathiphyllum! Not " + customer_choice + "!")