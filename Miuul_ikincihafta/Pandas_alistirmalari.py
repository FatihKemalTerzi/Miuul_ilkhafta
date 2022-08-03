import pandas as pd
import seaborn as sns
#görev1
df = sns.load_dataset("titanic")
df.head()
#bütün sütünları gösteren
pd.set_option('display.max_columns',None)
df.head()
#df.drop(0,axis=0).head(10) belirli indexi silmek istediğimiz zaman(axis=0 ise satırlardan axis=1 ise sütünlarda değişiklik yapıyor)
#birden fazla index gönderip buna göre silme işlemi yaparsak
#delete_indexes=[1,3,5,7]
#df.drop(delete_indexes,axis=0).head(10) burada yapılan değişiklik kalıcı değiildir
#df.drop(delete_indexes,axis=0,inplace=True).head(10) inplace eklersek kalıcı olur

#age değişkenini index olarak ekledik
#df.index=df["age"]
#age değişkenini kalıcı olarak sildik
df.drop("age",axis=1,inplace=True) #age değişkenini kalıcı olarak sildik

#indextekteki age i değişkene çevirdik
#df["age"]=df.index

#ikiside değişken seçim işi görüyor
"""df["age"].head()
df.age.head()

df[["age"]].head() iki köşeli parantez kullanmamız durumunda veri yapımızın tipi bozulmaz ve dataframe olmaya devam eder(aksi takdirde yukarıdaki gibi olursa veri tipi pandas series olacaktır.)
"""
#iloc= index(integer) bilgisi vererek seçim yapar
#loc= label bilgisi ile seçim yapar
"""df.head()
df.loc[]"""

#df[df["age"]>50]["age"].count()#age değişkenin içerisinde yaşı 50 den büyük olan kaç kişi var

df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[df["sex"] == "male"].count()
df.loc[df["sex"] == "female"].count()
df.head()
##görev 3
#value.counts ifadesi Sütundaki NaN olmayan her bir unique değerin kaç kez kullanıldığını gösteren bir seri döndürür.
df.value_counts()
#görev4
df.loc[df["pclass", "parch"]].value_counts()
#görev6
type(df[["embarked"]])
#görev7

df[df["embarked"] == "C"].head()

#sadece age içeren ifadeleri seçti
df.loc[:, df.columns.str.contains("age")].head()
#görev8???
df.loc[:, df["embarked"] == "S"].head()
#görev9

df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()

#görev10
df.loc[(df["fare"] > 500) | (df["age"] > 70)].head()

#görev11????
df.loc[~df.head().value_counts()].head()

#görev12
df.drop("who",axis=1)
df.head()
#burada yaşın ortalamsını bulduk .mean() komutu ile
df["age"].mean()
#cinsiyete göre yaşın ortalamsını almak istediğimiz zaman groupby kullanıyoruz (bir değişkenin başka bir değişkene göre ortalaması)
df.groupby("sex")["age"].mean()
######
#topluluaştırma& gruplama
"""
count()
first()
last()
mean()
median()
min()
max()
std()
var()
sum()
pivot table
özet istatistikler veren fonksiyonlar
"""
df.groupby("sex").agg({"age": "mean"})  #aggrigation fonk ile yaş değişkenine göre ortalamsını aldık


#eğer birden fazla aggrigation fonk istiyorsak


df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"], "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean", "sum"], "survived":"mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean", "sum"], "survived":"mean","sex":"count"})

#pivot table ön tanımlı değeri ortalamadır. Burada survived kısmı kesişim değerlerini, sex değişkeni satır indexinde, sütün indexinde de embarked değişkeni oluyor

df.pivot_table("survived", "sex", "embarked")
#burada ön tanımlı değeri aggfunc ile değiştirip standart sapma hesapla diyoruz
df.pivot_table("survived", "sex", "embarked", aggfunc="std")

#sayısal değişkenleri kategorik değişkene çevirirken en yaygın kullanılan fonksiyon .cut() ve .qcut() dır
#burada cut fonksiyonuna neyi böleceğini ve neye göre böleceğini veriyoruz

df["new_age"]=pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.head()

df.pivot_table("survived", "sex", "new_age")

##apply ve lambda fonksiyonları
#apply :satır ve sütünlarda otomatik olarak fonksiyon çalıştırmayı sağlar
#lampbda: kullan at fonksiyon tanımlamayı sağlar, kullan at fonksiyondur

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x-x.mean())/x.std()).head()
def standart_scaler(col_name):
    return (col_name - col_name.mean()) /col_name.std()
df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()