from pandas import DataFrame as DF

def receive_data(names,roll,sec):
    dataBase = DF({"Names":names, "Roll No.":roll, "Section": sec})
    dataBase.to_excel("excel.xlsx")
    dataBase.to_csv("read.csv")
    return dataBase