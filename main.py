#görev1
"""x=8

y=3.2

type(y)"""

##görev 2
"""text="the goal is the turn data into information, and information into insight."
text=text.replace(","," ")

new_list=text.upper().split()

print(new_list)"""

##görev3

"""lst=["D","A","T","A","S","C","I","E","N","C","E",]
print(len(lst))
lst[0]
lst[10]

new_list=[lst[i] for i in range(4)]
print(new_list)
del lst[8]
lst.append("F")
lst.insert(8,"N")
print(lst)"""

#görev4

"""dict={  'Cristian':["America",18],
        'Daisy': ["England",12],
        'Antonio': ["Spain",22],
        'Dante': ["Italy",25]}
print(dict.keys())
print(dict.values())
print(dict['Daisy'])
new_dict={'Daisy':["England",13]}
dict.update(new_dict)
print(dict)
last_dict={'Ahmet':["Turkey",24]}
dict.update(last_dict)
print(dict)
del dict['Antonio']
print(dict)"""

"""l=[2,13,18,93,22]
even_list=[]
odd_list=[]
def fonk(x):

    for i in x:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append((i))
    return even_list,odd_list
print(fonk(l))"""


##görev6

"""import seaborn as sns
df= sns.load_dataset("car_crashes")

df.columns=["NUM_" + kelime.upper() for kelime in df.columns if kelime!="O"]
print(df.columns)
"""


##görev7
"""
import seaborn as sns

df=sns.load_dataset("car_crashes")

seven=[kelime.upper()+"_FLAG" for kelime in df.columns if "no" not in kelime]

print(seven)"""

##görev8
"""import seaborn as sns
df=sns.load_dataset("car_crashes")
og_list=["abbrev","no_previous"]

new_cols=[col for col in df.columns if col!="abbrev" and col!="no_previous" ]
print(new_cols)
new_df=df[new_cols]
print(new_df)"""


