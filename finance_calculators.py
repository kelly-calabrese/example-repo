# Finance calculator for investment or bond scenarios

import math

# allow the user to choose either investment or bond
# start by explaining the choices
print("Investment - to calculate the amount of interest you'll earn on your investment. \nBond       - to calculate the amount you'll have to pay on a home loan.")
calc_choice = input("\nEnter either \"investment\" or \"bond\" from the menu above to proceed: ")

#allow any capitalization of "investment" or "bond" by standardizing. Give error message for invalid inputs.
calc_choice = calc_choice.lower()

while calc_choice != "investment" and calc_choice != "bond":
    print("Error: Invalid input.")
    calc_choice = input("Choose either \"investment\" or \"bond\" from the menu above to proceed: ")


# What to do depending on Calc_Choice: collect appropriate inputs and calculate results

if calc_choice == "investment": 

    #collect inputs for investment formulae
    principal_amt = float(input("Amount of money deposited: "))
    while principal_amt <= 0:
        principal_amt = float(input("Enter a positive value for deposit to proceed: "))
    
    pct_int_rate = float(input("Numeric value of yearly percent interest: "))
    while pct_int_rate <= 0:
        pct_int_rate = float(input("Enter a positive value for yearly percent interest to proceed: "))
    
    plan_years = float(input("Number of years planned for investment: "))
    while plan_years <= 0:
        plan_years = float(input("Enter a positive number of years planned to proceed: "))
    
    interest = input("Enter either \"simple\" or \"compound\" interest type: ")
    interest = interest.lower()
    while interest != "simple" and interest != "compound":
        print("Error: Invalid input.")
        interest = input("Choose either \"simple\" or \"compound\" to proceed: ")
    
    # interest formulae variables
    r = pct_int_rate/100 
    t = plan_years 
    
    # Interest formulae
    total_simple = round(principal_amt * (1 + r * t), 2) 
    total_compound = round(principal_amt * math.pow((1 + r), t), 2) 


else :

    # collect inputs for bond formula
    present_value = float(input("The present value of the house: "))
    while present_value <= 0:
        present_value = float(input("Enter a positive number for present value to proceed: "))
    
    pct_int_rate = float(input("Numeric value of yearly percent interest: "))
    while pct_int_rate <= 0:
        pct_int_rate = float(input("Enter a positive number for yearly percent interest to proceed: "))
    
    plan_months = float(input("Number of months planned to repay the bond: "))
    while plan_months <= 0:
        plan_months = float(input("Enter a positive number of planned months to proceed: "))

    # Bond repayment formula variables
    r = pct_int_rate/100
    i = r/12
    n = int(plan_months)
    
    # Bond repayment formula
    repayment = round((i * present_value)/(1 - (1 + i) ** (-n)),2)


# Print requested output
if calc_choice == "investment" and interest == "simple":
    print(f"Total amount after {plan_years} years with principal amount of {principal_amt} at {pct_int_rate}% yearly simple interest is:\n{total_simple}")
elif calc_choice == "investment" and interest == "compound":
    print(f"Total amount after {plan_years} years with principal amount of {principal_amt} at {pct_int_rate}% yearly compound interest is:\n{total_compound}")
else :
    print(f"The monthly payment for a home loan of {present_value} over {plan_months} months with a yearly interest rate of {pct_int_rate}% is: \n{repayment}")

