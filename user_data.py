
import pandas as pd

id_list=[]
Name_list=[]
cp_list=[]
maths_list=[]
ece_list=[]
ee_list=[]
qp_list=[]
s_no=[]
while True:

    ID=(input("Enter student's ID: "))
    Name=input("Enter student's name: ")
    cp=int(input("Enter (FCCS0102) marks: "))
    maths=int(input("Enter (FCMT0101) marks: "))
    ece=int(input("Enter (FCEC0106) marks: "))
    ee=int(input("Enter (FCEE0106) marks: "))
    qp=int(input("Enter (FCPH0114) marks: "))
    id_list.append(ID)
    Name_list.append(Name)
    cp_list.append(cp)
    maths_list.append(maths)
    ece_list.append(ece)
    ee_list.append(ee)
    qp_list.append(qp)


    choice=input("Do you wish to continue(y/n): ")
    if(choice=="y"):
        pass
    elif(choice=="n"):
        break
    else:
        print("ERROR!")
        break

info={
    "Name":Name_list,"FCCS0102":cp_list,"FCEC0106":ece_list,"FCEE0106":ee_list,"FCMT0101":maths_list,
    "FCPH0114":qp_list
}

new_df=pd.DataFrame(info,index=id_list)
new_df.index.name="ID"
try:
    old_df=pd.read_csv("Data.csv",index_col="ID")
except FileNotFoundError:
    old_df=pd.DataFrame()

if not old_df.empty:
      new_df=pd.concat([new_df,old_df])

new_df.to_csv("Data.csv",index_label="ID")


