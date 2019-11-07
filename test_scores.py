#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'end' to end input")
print("======================")

yn = "y"
while yn == "y":
	# initialize variables
	counter = 0
	score_total = 0
	test_score = ""

	while test_score != "end":
		test_score = input("Enter test score: ")
		if test_score == "end":
			break
		elif int(test_score) >= 0 and int(test_score) <= 100:
			score_total += int(test_score)
			counter += 1
		else:
			print("Test score must be from 0 through 100. Score discarded. Try again.")

	# calculate average score
	average_score = round(score_total / counter)
                
	# format and display the result
	print("======================")
	print("Total Score:", score_total,
      	"\nAverage Score:", average_score)
	print()
	yn = input("Enter another set of test scores (y/n)? ")
	test_score = 0
print("Bye")


