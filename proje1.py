
import numpy as np
import pandas as pd

df = pd.read_csv('Hafta_02/persona.csv')

#sORU1
df.head()
df.tail()
df.shape
df.describe().T
df.colums
df.reset_index()
df.isnull().sum()
#Soru2

df["SOURCE"].value_counts()

df["SOURCE"].nunique()
#soru3
df["PRICE"].nunique()

#soru4

df["PRICE"].value_counts()
#soru5


df["COUNTRY"].value_counts()

#SORU6
df[['PRICE','COUNTRY']].groupby("COUNTRY").sum()
df.groupby("COUNTRY").PRICE.sum()
#df.groupby(["COUNTRY"]).agg({"PRICE":["sum","mean"]})
#soru7

df["SOURCE"].value_counts()
df[["SOURCE","COUNTRY"]].groupby("SOURCE").count()
#soru8

df[["PRICE","COUNTRY"]].groupby("COUNTRY").mean()

#soru9
df[["PRICE","SOURCE"]].groupby("SOURCE").mean()
#SORU10

df[["SOURCE","COUNTRY","PRICE"]].groupby(["COUNTRY","SOURCE"]).mean()

#GOREV 2

df[["SOURCE","COUNTRY","SEX","AGE","PRICE"]].groupby(["SOURCE","COUNTRY","SEX","AGE"]).mean()

#GOREV3
agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).mean().sort_values(by ="PRICE", ascending = False)

#GOREV4
agg_df = agg_df.reset_index()
AGE_CAT=[]
#GOREV5- 1.yol
for row in agg_df["AGE"]:
    if row in range(0,19) :
        AGE_CAT.append("0_18")
    elif row in range(19,24):
        AGE_CAT.append("19_23")
    elif row in range(24,31):
        AGE_CAT.append("24_30")
    elif row in range(31,41):
        AGE_CAT.append("31_40")
    elif row in range(41,71):
        AGE_CAT.append("41_70")
agg_df["AGE_CAT"]=AGE_CAT
 #2. yol

agg_df.loc[(agg_df['AGE'] <= 18 ), 'AGE_CAT'] = '0_18'
agg_df.loc[(agg_df['AGE'] <= 23) & (agg_df['AGE'] >= 19), 'AGE_CAT'] = '19_23'
agg_df.loc[(agg_df['AGE'] <= 30) & (agg_df['AGE'] >= 23), 'AGE_CAT'] = '24_30'
agg_df.loc[(agg_df['AGE'] <= 40) & (agg_df['AGE'] >= 31), 'AGE_CAT'] = '31_40'
agg_df.loc[(agg_df['AGE'] <= 70) & (agg_df['AGE'] >= 41), 'AGE_CAT'] = '41_70'
#3.yol
agg_df["AGE_CAT"]=pd.cut(agg_df["AGE"],[0,18,23, 30, 40, 70],labels=["0_18","19_23","24_30","31_40","41_66"])
#GOREV6


#for col in ["COUNTRY","SOURCE","SEX","AGE","AGE_CAT"]:
#    print(col)

#for row in agg_df.values]


agg_df = agg_df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE_CAT", "AGE"])[["PRICE"]].sum().reset_index()

pd.set_option('display.max_columns', None)
agg_df["customers_level_based"]=agg_df["COUNTRY"].str.upper()+"_"+ agg_df["SOURCE"].str.upper()+"_"+agg_df["SEX"].str.upper()+"_"+agg_df["AGE_CAT"].str.upper()

agg_df[["customers_level_based","PRICE"]].groupby("customers_level_based").mean()


agg_df2["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper()
                                    + "_" + str(row[5]) for row in agg_df.values]

# GOREV 7
agg_df["SEGMENT"]=pd.qcut(agg_df["PRICE"],4 ,labels=["D","C","B","A"])
agg_df.groupby("SEGMENT").agg(["mean","max","sum"])

agg_df[agg_df["SEGMENT"]=="C"].describe()


#gorev 8

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"]==new_user]


new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"]==new_user]