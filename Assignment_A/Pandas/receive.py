import python as pt
import pandas as pd

# names = [ x for x in input("Enter names seperated by spaces: ").split()]
# roll = [int(x) for x in input("Enter roll no seperated by spaces: ").split()]
# sec = [x for x in input("Enter sec seperated by spaces: ").split()]
# database = pt.receive_data(names,roll,sec)

DataSet1 = pd.read_csv('read.csv')
print(DataSet1[['Names','Section']])

print(DataSet1.iloc[[1]])