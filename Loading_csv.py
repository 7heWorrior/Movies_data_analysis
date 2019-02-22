import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("Movies_Final.csv",encoding = "ISO-8859-1")
df = pd.DataFrame(data)
def graph (a,gnr,Budget,Coll):
    plt.xticks(a,gnr)
    plt.bar(a - 0.125, Budget, label='Budget', width=0.25)
    plt.bar(a + 0.125, Coll, label="Collection", width=0.25)
    plt.legend()
    plt.title("Comparison Between the Budget And Collection Data of Various Genre")
    plt.xlabel("Genre")
    plt.ylabel("in Millions")
    plt.show()

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
gnr ={0:'Romance',1:'Action',2:'Drama',3:'Thriller',4:'Comedy'}
Budget = list((romanceBudget,actionBudget,dramaBudget,thrillerBudget,comedyBudget))
Coll = list((romanceColl,actionColl,dramaColl,thrillerColl,comedyColl))
for i in range(241):
    for m in range(5):
        if gnr[m] in str(df["Genre"][i]):
            Budget[m] +=(df["Budget"][i])
            Coll[m]+=(df["Box Office"][i])
a = np.arange(5)

graph(a,gnr.values(),Budget,Coll)
plt.subplot(1,2,1)
plt.pie(Budget,labels=gnr.values(),startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title("Budget")
plt.subplot(1,2,2)
plt.pie(Coll,labels=gnr.values(),startangle=90,shadow=True,explode=(0.1,0,0,0,0),autopct='%1.1f%%')
plt.title("Collection")
plt.show()
b = np.arange(12)
mnt = list(('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
f = df.groupby('Month').sum()
f.index = pd.CategoricalIndex(f.index,categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
f= f.sort_index()
bd = f['Budget']
cl = f['Box Office']
plt.xticks(b,mnt)
plt.plot(b,bd,label='Budget',color='r')
plt.plot(b,cl,label='Collection',color='b')
plt.legend()
plt.title("Monthly Summary of All Movies")
plt.show()
