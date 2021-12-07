# Day16 of my 100DaysOfCode Challenge

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("id", ["1", "2", "3"])
table.add_column("name", ["ABC", "DEf", "GHI"])
table.add_column("City", ["Delhi", "New York", "Paris"])

table.align = "r"

print(table)