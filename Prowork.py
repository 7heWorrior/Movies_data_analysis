import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
data=pd.read_csv("Movies_Final.csv",encoding='ISO-8859-1')
df=pd.DataFrame(data)
m=df.groupby('Year')
p=m.get_group(2016)
q=m.get_group(2017)

r=pd.DataFrame(p)
s=r.groupby("Month")

t=pd.DataFrame(q)
u=t.groupby("Month")

idx=s['Box Office'].sum()
idx.index=pd.CategoricalIndex(idx.index,categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
idx=idx.sort_index()



idy=u['Box Office'].sum()
idy.index=pd.CategoricalIndex(idy.index,categories=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
idy=idy.sort_index()

mnt=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
a=np.arange(12)
mp.xticks(a,mnt)
mp.bar(a-0.125,idx,label='2016',width=0.25)
mp.bar(a+0.125,idy,label='2017',width=0.25)
mp.legend()
mp.title('BOX OFFICE COLLECTION')
mp.ylabel("In Millions")
mp.xlabel('Months')
mp.show()
