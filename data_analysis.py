import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv("Data.csv",index_col="ID")
class Individual:
    def __init__(self,id):
        self.id=id
    def valid(self):
        if self.id in df.index:
            return True
        else:
            return False
    def sub_marks(self):
        total=df.loc[self.id,"FCCS0102"]+df.loc[self.id, "FCEC0106"]+df.loc[self.id, "FCEE0106"]+df.loc[self.id, "FCMT0101"]+df.loc[self.id, "FCPH0114"]
        print(f"FCCS0102:{df.loc[self.id,"FCCS0102"]}")
        print(f"FCEC0106:{df.loc[self.id, "FCEC0106"]}")
        print(f"FCEE0106:{df.loc[self.id, "FCEE0106"]}")
        print(f"FCMT0101:{df.loc[self.id, "FCMT0101"]}")
        print(f"FCPH0114:{df.loc[self.id, "FCPH0114"]}")
        print(f"Average is : {total/5}")
    def grading_fun(self,marks):
        if(marks>90):
            return ("A")
        elif(marks>80 and marks<90):
            return ("B")
        elif(marks>70 and marks<80):
            return ("C")
        else:
            return ("D")
    def grade(self):
        print(f"FCCS0102:{self.grading_fun(df.loc[self.id, "FCCS0102"])}")
        print(f"FCEC0106:{self.grading_fun(df.loc[self.id, "FCEC0106"])}")
        print(f"FCEE0106:{self.grading_fun(df.loc[self.id, "FCEE0106"])}")
        print(f"FCMT0101:{self.grading_fun(df.loc[self.id, "FCMT0101"])}")
        print(f"FCPH0114:{self.grading_fun(df.loc[self.id, "FCPH0114"])}")
    def bar(self):
        subjects=np.array(["FCCS0102","FCEC0106","FCEE0106","FCMT0101","FCPH0114"])
        marks=np.array([df.loc[self.id, "FCCS0102"],df.loc[self.id, "FCEC0106"],df.loc[self.id, "FCEE0106"],df.loc[self.id, "FCMT0101"],df.loc[self.id, "FCPH0114"]])
        plt.bar(subjects,marks)
        plt.title("BAR GRAPH",fontsize=20,fontweight="bold")
        plt.ylabel("MARKS",fontsize=20,fontweight="bold")
        plt.xlabel("SUBJECTS",fontsize=20,fontweight="bold")
        plt.show()



class Section:
    def class_avg(self):
        print(f"CLASS AVERAGE: {df["FCCS0102"].mean()/5+df["FCEC0106"].mean()/5+df["FCEE0106"].mean()/5+df["FCMT0101"].mean()/5+df["FCPH0114"].mean()/5}")
    def subject_avg(self):
        print(f"FCCS0102: {df["FCCS0102"].mean()}")
        print(f"FCEC0106: {df["FCEC0106"].mean()}")
        print(f"FCEE0106: {df["FCEE0106"].mean()}")
        print(f"FCMT0101: {df["FCMT0101"].mean()}")
        print(f"FCPH0114: {df["FCPH0114"].mean()}")
    def highest_lowest(self):
        print(f"FCCS0102: Highest: {df["FCCS0102"].max()}, Lowest: {df["FCCS0102"].min()}")
        print(f"FCEC0106: Highest: {df["FCEC0106"].max()}, Lowest: {df["FCEC0106"].min()}")
        print(f"FCEE0106: Highest: {df["FCEE0106"].max()}, Lowest: {df["FCEE0106"].min()}")
        print(f"FCMT0101: Highest: {df["FCMT0101"].max()}, Lowest: {df["FCMT0101"].min()}")
        print(f"FCPH0114: Highest: {df["FCPH0114"].max()}, Lowest: {df["FCPH0114"].min()}")
    def table(self):
        print(df.to_string())
class Compare:
    def __init__(self,id1,id2):
        self.id1=id1
        self.id2=id2
    def graph(self):
        x1 = np.array(["FCCS0102", "FCEC0106", "FCEE0106", "FCMT0101", "FCPH0114"])
        y1=np.array([df.loc[self.id1, "FCCS0102"],df.loc[self.id1, "FCEC0106"],df.loc[self.id1, "FCEE0106"],df.loc[self.id1, "FCMT0101"],df.loc[self.id1, "FCPH0114"]])
        y2=np.array([df.loc[self.id2, "FCCS0102"],df.loc[self.id2, "FCEC0106"],df.loc[self.id2, "FCEE0106"],df.loc[self.id2, "FCMT0101"],df.loc[self.id2, "FCPH0114"]])
        plt.plot(x1,y1,marker=".",markersize=10,markerfacecolor="blue",label=f"{self.id1}")
        plt.plot(x1,y2,marker=".",markersize=10,markerfacecolor="green",label=f"{self.id2}")
        plt.legend()
        plt.show()






