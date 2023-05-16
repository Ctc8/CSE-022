current_balance = int(input("Enter your current bank balance: "))
expenses = int(input("Projected monthly operational expenses: "))
income = int(input("Projected monthly income from operations: "))

gross_burn_rate = expenses
net_burn_rate = (expenses - income)
runway = (current_balance/net_burn_rate)

print("Gross burn rate: $%d " % gross_burn_rate)
print("Net burn rate: $%d " % net_burn_rate)
print("Projected runway: %d months" % runway)

# 1. Gross burn rate: The amount of money needed to sustain the business (expenses)
# 2. Net burn rate: Difference between the gross burn rate and the monthly income generated (Negative NBR is good) (cash/losses)
# 3. Calculate startup runway by amount of money we have now / net burn rate

