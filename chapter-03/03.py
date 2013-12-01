# Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(word):
	word_length = len(word)
	space_number = 70 - word_length
	print space_number * " " + word

right_justify('David Zhu')