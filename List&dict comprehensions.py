#bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns
df= sns.load_dataset("car_crashes")

df.columns=["NUM_" + kelime.upper() for kelime in df.columns if kelime!="O"]
print(df.columns)


import seaborn as sns

df=sns.load_dataset("car_crashes")
seven=[kelime.upper()+"_FLAG" for kelime in df.columns if "no" not in kelime]

print(seven)