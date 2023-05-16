p = float(input("Enter loan amount: "))
n = float(input("Enter load period (months): "))
r = float(input("Enter annual interest rate (percentage): "))
m = (r/100) / 12
cost = ((p * m * ((1+m) ** n)) / (((1+m) ** n) - 1)) 
print("You owe $%.2f" % cost + " per month.")




'''
P * r * (1+r)^N
---------------
(1+r)^N - 1
'''