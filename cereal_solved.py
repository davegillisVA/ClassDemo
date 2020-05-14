import os
import csv
import pprint as pp## Added DFG
import pandas as pd## Added DFG

cereal_csv = os.path.join("Resources", "cereal.csv")
print(cereal_csv)##A dded DFG
cereal = pd.DataFrame(pd.read_csv(cereal_csv))## Added DFG
print(cereal) ## Added DFG
selectedCereal = cereal.loc[cereal['fiber'] >= 5]## Added DFG
print("Selected Stuff")## Added DFG
pp.pprint(selectedCereal)## Added DFG
# Open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    temp = next(csvreader)
    print(temp)
    fiberlist = [row for row in csvreader if (float(row[7]) >= 5)]
    pp.pprint(fiberlist)

    # Read the header row first (skip this part if there is no header)
    #csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    # for row in csvreader:
    #
    #     # Convert row to float and compare to grams of fiber
    #     if float(row[7]) >= 5:
    #         print("from csv reader")
    #         print(row[7])

    #new_list = [expression(i) for i in old_list if filter(i)]

    #fiberlist = [row[7] for row in csvreader if (float(row[7]) >= 5)]
    #print(fiberlist)
# pp.pprint(row)##Added DFG
# good.append(row) ##Added DFG
# print(good) ## Added DFG