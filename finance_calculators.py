import math
# Allows users to access different financial calculators: investment and bond.
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

# Enter either "investment" or "bond" from the menu above to proceed:
calculator = input("Enter either 'investment' or 'bond': ").lower()

# If user selects "investment", the program should ask them to enter the following:
# The amount of money they are depositing
# The interest rate
# The number of years they plan on investing
# The type of interest "simple" or "compound"
if calculator == "investment":
    deposit = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate: "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("""Enter the type of interest,
                           choose between 'simple' or 'compound': """)
# Convert intrest rate divided by 100
    r = interest_rate / 100
# Simple interest formula: A = P(1 + r*t)
    if interest_type == "simple":
        A = deposit * (1 + r * years)
        print("Total amount:", A)
# Compound interest formula: A = P(1 + r)^t
    elif interest_type == "compound":
        A = deposit * math.pow((1 + r), years)
        print("Total amount:", A)

# If user selects "bond", the program should ask them to enter the following:
# The present value of the house
# The interest rate
# The number of months they plan to take to repay the bond
if calculator == "bond":
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months you plan to take to repay the bond: "))
# Convert interest rate divided by 100 and then divided by 12
    i = (interest_rate / 100) / 12
# Bond repayment formula: repayment = (i * P)/(1 - (1 + i)^(-n))
    repayment = (i * house_value) / (1- math.pow((1 + i), -months))
    print("Your monthly repayment is:", repayment)

# If the user does not select either "investment" or "bond", the program should display "Error: Please Type Again".
else:
    print("Error: Please Type Again")
