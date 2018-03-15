import csv

dataset = csv.reader(open('..\Dataset\JAMP_DATA0722figshaer.csv', newline=''), delimiter=' ', quotechar='|')
for row in dataset :
    print(', '.join(row))
