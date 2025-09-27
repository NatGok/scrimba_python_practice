#customer guesses the computer's favourite plant
#the computer responds based on the user's input


customer_choice=input("Can you guess the computers favourite plant? ")
if customer_choice == "spathiphyllum":
    print("Not quite I need a capital S in the name of the plant Spathiphyllum")
elif customer_choice == "Spathiphyllum": 
    print("Yes - Spathiphyllum is the best plant ever!")
else: 
    print("Spathiphyllum! Not " + customer_choice + "!")
#exercise 2
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Write the rest of your code here.
else:
    tax =((14839.02-income)*.032)+14839.02

if tax < 0.0:
	tax = 0.0
     
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 #exercise3 leap year or common year or pre georgian calendar
year = int(input("Enter a year: "))
if year < 1582:
    print("This year is before the Gregorian calendar.")
elif year % 4 == 0 and (year % 100 != 0):
    print("This is a leap year.")
else year % 400 != 0:
		print("Common year")
    print("This is a common year.")