"""
MakeChange.py
This Program receives an input dollar amount, then makes change for that amount based on the given price of an item

Barry Cheeney
20220214 v2.0
"""
Payment = 0.0
Cost = 0.0
Change = 0.0

def figure_change(Change):
    Ten = Change // 1000
    Five = (Change % 1000) // 500
    Dollar = (Change % 1000 % 500) // 100
    Quarter = (Change % 1000 % 500 % 100) // 25
    Dime = (Change % 1000 % 500 % 100 % 25) // 10
    Nickle = (Change % 1000 % 500 % 100 % 25 % 10) // 5
    Penny = Change % 5
    
    print ("The Customer's Change Payment is:")
    print (round(Ten),"Tens")
    print (round(Five),"Fives")
    print (round(Dollar),"Dollars")
    print (round(Quarter),"Quarters")
    print (round(Dime),"Dimes")
    print (round(Nickle),"Nickles")
    print (round(Penny),"Pennies")
    print ("")

while True:
    try:
        Payment = float(input("Please Enter Payment Amount:"))
    except ValueError:
        print("Payment must be input in decimal notation such as 1.00 or 32.45")
        continue
    else:
        break

if(Payment > 100.00):
    print ("Payment exceeds sales limit, please contact manager.")
    while True:
        try:
            Payment = float(input("Please Enter Payment Amount:"))
        except ValueError:
            print("Payment must be input in decimal notation such as 1.00 or 32.45")
            continue
        else:
            break    
if(Payment < 0.0):
    print ("This location is not authorized to give refunds, please contact manager.")
    while True:
        try:
            Payment = float(input("Please Enter Payment Amount:"))
        except ValueError:
            print("Payment must be input in decimal notation such as 1.00 or 32.45")
            continue
        else:
            break

while True:
    try:
        Cost = float(input("Please enter the cost of the item:"))
    except ValueError:
        print("Cost must be input in decimal notation such as 1.00 or 32.45")
        continue
    else:
        break
if(Cost > 100.00):
    print ("Cost exceeds sales limit, please contact manager.")
    while True:
        try:
            Cost = float(input("Please Enter Cost Amount:"))
        except ValueError:
            print("Cost must be input in decimal notation such as 1.00 or 32.45")
            continue
        else:
            break    
if(Cost < 0.0):
    print ("This location is not authorized to give refunds, please contact manager.")
    while True:
        try:
            Cost = float(input("Please Enter Cost Amount:"))
        except ValueError:
            print("Cost must be input in decimal notation such as 1.00 or 32.45")
            continue
        else:
            break

Payment = Payment * 100
Cost = Cost * 100
Change = Payment - Cost

print("Customer's Change is    $", round(Change / 100, 2))
print("")
figure_change(Change)