import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("Movies_Final.csv",encoding = "ISO-8859-1")
df = pd.DataFrame(data)
gp = df.groupby("Year")
sx = gp.get_group(2017)
vi = pd.DataFrame(sx)
sv = gp.get_group(2016)
vii = pd.DataFrame(sv)
mnt = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

idx = vi.groupby(["Month"])['Box Office'].transform(max) == vi['Box Office']

idy = vii.groupby(["Month"])['Box Office'].transform(max) == vii['Box Office']
print("Top Grossing Movies of 2016(MonthWise) \n\n\n",vii[idy]['Title'])
print("Top Grossing Movies of 2017(MonthWise) \n\n\n",vi[idx]['Title'])