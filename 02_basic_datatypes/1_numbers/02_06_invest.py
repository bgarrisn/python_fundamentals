'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
invest=int(input("How much are you investing: "))
interest=float(input("What is the interest rate in decimals: "))
years=int(input("How many years will you invest: "))

#futureval= int(invest)+(int(invest) * (int(interest)/100)* int(years))
#print(futureval)

#I am assuming this is not calculating compounding interest :-)


#futureval= invest*interest

#for every year, multiply future value by the interest,
# add back to base value, and then there is a new future value

for _ in range(years):
    compound=invest*interest
    invest=compound+invest
    print("the total is: " + str(invest))
