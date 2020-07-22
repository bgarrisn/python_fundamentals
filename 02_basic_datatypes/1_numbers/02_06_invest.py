'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
invest=input("How much are you investing: ")
interest=input("What is the interest rate in percentage: ")
years=input("How many years will you invest: ")

futureval= int(invest)+(int(invest) * (int(interest)/100)* int(years))
print(futureval)

#I am assuming this is not calculating compounding interest :-)