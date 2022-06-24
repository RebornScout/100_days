
print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
diners = input("How many people to split the bill? ")
to_pay = round((float(bill))/ int(diners) * ((int(tip)/100)+1), 2)
print("The amount you need to pay is:", to_pay)