# Day7 of my 100DaysOfCode Challenge

# Problem

# Arpasland has surrounded by attackers. A truck enters the city. 
# The driver claims the load is food and medicine from Iranians. 
# Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. 
# He knows that a Tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. 
# Determine if the Tag of the truck is valid or not.

# We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

# Input Format
# The first line contains a string of length 9. The format is "DDtagDDD-DD", where D stands for a digit (non zero) and tag is an uppercase english letter.

# Output Format
# Print "valid" (without quotes) if the Tag is valid, print "invalid" otherwise (without quotes)

tag = input("Enter the Tag: ")
if len(tag) != 9:
	print("invalid")
else:
	vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
	output = 0
	if((int(tag[0]) + int(tag[1])) % 2 == 1):
		output = 1
	if( tag[2] in vowels):
		output = 1
	if((int(tag[3]) + int(tag[4])) % 2 == 1):
		output = 1
	if((int(tag[4]) + int(tag[5])) % 2 == 1):
		output = 1
	if((int(tag[7]) + int(tag[8])) % 2 == 1):
		output = 1
	if(output == 0):
		print("valid")
	else:
		print("invalid")
