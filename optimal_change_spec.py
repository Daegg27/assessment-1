from optimal_change import optimal_change


print("1:",optimal_change(0.42, 1) == "The optimal change for an item that costs $0.42 with an amount paid of $1 is 2 quarters, 1 nickel, and 3 pennies.")
print("2:",optimal_change(23.41, 64.12) == "The optimal change for an item that costs $23.41 with an amount paid of $64.12 is 2 $20 bills, 2 quarters, 2 dimes, and 1 penny.")
print("3:",optimal_change(43.41, 51.41) == "The optimal change for an item that costs $43.41 with an amount paid of $51.41 is 1 $5 bill, and 3 $1 bills.")
print("4:",optimal_change(31.53, 42.21) == "The optimal change for an item that costs $31.53 with an amount paid of $42.21 is 1 $10 bill, 2 quarters, 1 dime, 1 nickel, and 3 pennies.")
print("5:",optimal_change(10.94, 11) == "The optimal change for an item that costs $10.94 with an amount paid of $11 is 1 nickel, and 1 penny.")
print("6:",optimal_change(86.72, 93.21) == "The optimal change for an item that costs $86.72 with an amount paid of $93.21 is 1 $5 bill, 1 $1 bill, 1 bill, 2 dimes, and 4 pennies.")



print("7:",optimal_change(12, 10) == "You do not have enough money!")
print("8:",optimal_change(12, 12) == "You are all set!")
