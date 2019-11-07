#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # initialize variables
    monthly_investment = 0
    yearly_interest_rate = 0
    years = 0
    monthly_interest_amount = 0

    while monthly_investment < 1:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0:
            break
        else:
            print("Entry must be greater than 0. Please try again.") 
    
    while yearly_interest_rate <= 0 or yearly_interest_rate > 15:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 15") 

    while years < 1 or years > 50:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 50")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = 12

    
    future_value = 0
    # calculate the future value
    # display the result
    print()
    years_count = 0
    for i in range(years):
        for i in range(months):
            future_value += monthly_investment
            monthly_interest_amount = future_value * monthly_interest_rate
            future_value += monthly_interest_amount
        years_count += 1
        print("year = ", years_count, "Future Value = "+ str(round(future_value, 2)))


    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
