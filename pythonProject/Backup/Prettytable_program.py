from prettytable import  PrettyTable


my_table = PrettyTable()
my_table.add_column("City_Name",["Bangalore", "Chennai", "Delhi"])
my_table.add_column("City_Name",["Bangalore", "Chennai", "Delhi"])
my_table.align = "l"
print(my_table)