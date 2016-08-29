import csv
item_list_file = open("items.csv", "r")
item_list_reader = csv.reader(item_list_file)
for row in item_list_reader:
    print(row)