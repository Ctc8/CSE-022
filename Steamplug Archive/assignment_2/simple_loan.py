loan_amount1 = float(input("Enter loan amount: "))
load_period1 = float(input("Enter load period (months): "))
loan_amount2 = loan_amount1/load_period1

print ("You owe $%.2f" % loan_amount2, "per month.")