import pandas as pd
import numpy as np

df=pd.read_csv("test.csv")

missing_values=["na","n/a","-"]
df=pd.read_csv("test.py",na_values=missing_values)

df['Science'].filna(0,inplace=True)
df['Math'].filna(0,inplace=True)
df['lang'].filna(0,inplace=True)
