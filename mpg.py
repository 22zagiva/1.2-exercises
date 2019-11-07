#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

yn = "y"
while yn == "y":

	# get input from the user
	miles_driven= float(input("Enter miles driven:\t\t"))
	gallons_used = float(input("Enter gallons of gas used:\t"))
	miles_gallon_cost = float(input("Enter cost per gallon:\t\t"))

	# calculate miles per gallon
	mpg = miles_driven / gallons_used 
	mpg = round(mpg, 1)
	tgc = gallons_used * miles_gallon_cost
	tgc = round(tgc, 1)
	cpm = miles_gallon_cost * gallons_used / miles_driven
	cpm = round(cpm, 1)

	# format and display the result
	print()
	print("Miles Per Gallon:\t\t" + str(mpg))
	print("Total Gas Cost:\t\t\t" + str(tgc))
	print("Cost Per Mile:\t\t\t" + str(cpm))
	print()
	yn = input("Get entries for another trip (y/n)? ")
	print()
print("bye!")
