from optimal_change import optimal_change

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", (optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."))
print("3:", optimal_change(42.39, 100)== "The optimal change for an item that costs $42.39 with an amount paid of $100 is 1 $50 bill,   1 $5 bill, 2 $1 bills, 2 quarters, 1 dime,  1 penny.")
print("4:", optimal_change(72.43, 80) == "The optimal change for an item that costs $72.43 with an amount paid of $80 is    1 $5 bill, 2 $1 bills, 2 quarters,  1 nickle, 2 pennies.")
print("5:", optimal_change(7.54, 5.00) == "Sorry! You don't have enough money!")