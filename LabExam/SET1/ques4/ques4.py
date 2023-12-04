from pandas import DataFrame as DF
import pandas as pd

names = ["Gaurang", "Sagnik", "Aditya", "Khateeb"]
reg = [1,10,5,4]
marks = [20,2,23,4]

di = {
    "names": names,
    "reg": reg,
    "marks": marks
}

dataset1 = DF(di)
dataset1.to_csv('Unsorted.csv')

for i in range(len(di["reg"])):
    for j in range(len(di["reg"])-i-1):
        if(di["reg"][j]> di["reg"][j+1]):
            di["reg"][j], di["reg"][j+1] = di["reg"][j+1], di["reg"][j]
            di["names"][j], di["names"][j+1] = di["names"][j+1], di["names"][j]
            di["marks"][j], di["marks"][j+1] = di["marks"][j+1], di["marks"][j]

dataset2 = DF(di)
dataset2.to_csv('Sorted.csv')
pd.concat([dataset1,dataset2], ignore_index=True).to_excel('merged.xlsx')