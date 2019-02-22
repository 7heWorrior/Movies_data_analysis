import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("Movies_Final.csv",encoding = "ISO-8859-1")
df = pd.DataFrame(data)
year = df.groupby("Year")
six = year.get_group(2016)
seven = year.get_group(2017)
xs = pd.DataFrame(six)
sv = pd.DataFrame(seven)
comedyBudget = 0
comedyColl = 0
thrillerBudget = 0
thrillerColl = 0
dramaBudget = 0
dramaColl = 0
actionBudget = 0
actionColl = 0
romanceBudget = 0
romanceColl = 0
gnr = {0:'Romance',1:'Action',2:'Drama',3:'Thriller',4:'Comedy'}
Budget = list((romanceBudget,actionBudget,dramaBudget,thrillerBudget,comedyBudget))
Coll = list((romanceColl,actionColl,dramaColl,thrillerColl,comedyColl))
for i in range(120):
    for m in range(5):
        if gnr[m] in str(xs["Genre"][i]):
            Budget[m] +=(xs["Budget"][i])
            Coll[m]+=(xs["Box Office"][i])
comedyBudget1 = 0
comedyColl1 = 0
thrillerBudget1 = 0
thrillerColl1 = 0
dramaBudget1 = 0
dramaColl1 = 0
actionBudget1 = 0
actionColl1 = 0
romanceBudget1 = 0
romanceColl1 = 0

Budget1 = list((romanceBudget1,actionBudget1,dramaBudget1,thrillerBudget1,comedyBudget1))
Coll1 = list((romanceColl1,actionColl1,dramaColl1,thrillerColl1,comedyColl1))
for j in range(121,241,1):
    for k in range(5):
        if gnr[k] in str(sv["Genre"][j]):
            Budget1[k] +=(sv["Budget"][j])
            Coll1[k]+=(sv["Box Office"][j])
plt.subplot2grid((2, 2), (0, 0))
plt.pie(Budget,labels=gnr.values(),startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title("Budget(2016)")
plt.subplot2grid((2, 2), (0, 1))
plt.pie(Coll,labels=gnr.values(),startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title("Collection(2016)")
plt.subplot2grid((2, 2), (1, 0))
plt.pie(Budget1,labels=gnr.values(),startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title("Budget(2017)")
plt.subplot2grid((2, 2), (1, 1))
plt.pie(Coll1,labels=gnr.values(),startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title("Collection(2017)")

plt.show()