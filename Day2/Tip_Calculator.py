# Day2 of my 100DaysOfCode Challenge

# Program to calculate TIP

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_given = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_person = int(input("How many people to split the bill? "))

total_bill_with_tip = (percentage_given / 100 ) * bill + bill
share_of_each_person = total_bill_with_tip / number_of_person
print(f"Each Person should pay: ${round(share_of_each_person)}")