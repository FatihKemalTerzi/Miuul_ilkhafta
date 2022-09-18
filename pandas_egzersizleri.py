import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

#görev 2
df.loc[df["sex"] == "male"].count()
df.loc[df["sex"] == "female"].count()
df.head()
#görev 3
df.value_counts()
#görev 4
df["pclass"].value_counts()
df["pclass"].nunique()

#görev 5
df[["pclass", "parch"]].nunique()

#görev 6
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
#görev 7
df.loc[df["embarked"] == "C"].head()

#görev 8
df.loc[df["embarked"] != "S"].head()

#görev 9
df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()

#görev 10
df.loc[(df["fare"] > 500) | (df["age"] >70)].head()

#görev 11
df.isnull().count()

#görev 12
df.drop("who", axis=1, inplace=False).head()

#görev 13######### fillna fonksiyonu önemli

df["deck"].fillna(df["deck"].mode().iloc[0], inplace=True)
df.head()

#görev 14

df["age"].fillna(df["age"].median(),inplace=True)

#görev 15
df.groupby(["survived"])["pclass", "sex"].aggregate(["mean", "sum", "count"])
#alttaki daha doğru
df.groupby(["pclass", "sex"]).aggregate({"survived": ["mean", "sum", "count"]})

#görev 16
df["age_flag"] = [1 if i<30 else 0 for i in df["age"]]
#apply ve lambda kullanarak yapımı

#görev 17
df2 =sns.load_dataset("tips")
df2.head()

#görev 18#####önemli
df2.groupby("time").aggregate({"total_bill" : ["sum", "min", "max", "mean"]})
###
#görev 19### çokomelli
df2.groupby(["time", "day"]).aggregate({"total_bill": ["sum", "min", "max", "mean"]})

#görev 20
df2[["total_bill", "tip", "day"]].loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill" : ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})
df2[["total_bill", "tip", "day"]].loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})
df2.loc[df2["time"] == "Dinner"].count()

filter1 = (df2.time == "Lunch") & (df2.sex == "Female")
df2[filter1].groupby("day").agg({"total_bill":["sum", "min", "max", "mean"], "tip" : ["sum", "min", "max", "mean"]})

#GÖREV 21
df.head()
df2.loc[(df2["size"] < 3) & (df2["total_bill"] > 10)].mean()

#görev 22
df2["total_bill_tip_sum"] = df2["total_bill"] + df2["tip"]

#görev 23#############olmadı
femaleort = df2["total_bill"].loc[df2["sex"] == "Female"].mean()
maleort = df2["total_bill"].loc[df2["sex"] == "male"].mean()
#buraya tekrar bak alt tarafa
df2["total_bill_flag"] = df2[["sex", "total_bill"]].apply(lambda x: func(x["sex"], x["total_bill"]), axis=1)

#görev 24
#value_counts() metodu ile unique değerlerin sayısına eriştik
df2["sex"].loc[df2["total_bill_flag"] == 0].value_counts()

#görev 25
df2["total_bill_tip_sum"].sort_values(ascending = False).head(30).head()

# Bu yalnizca secilen sutunu siralar oysa biz dataframe' i "total_bill_tip_sum" e gore siralamak istedigimiz icin asagidaki gibi ilerlemeliyiz.
df2.sort_values(by = ["total_bill_tip_sum"], ascending = False).head(30).head()

# ya da;
df2.sort_values("total_bill_tip_sum", ascending = False).head(30).head()

# ya da;
new_df2 = df2.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df2.shape