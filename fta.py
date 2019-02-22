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
