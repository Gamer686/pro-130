import pandas as pd
import csv

df = pd.read_csv("details.csv")



del df["Luminosity"]
del df["Star_namee"]
del df["Distancee"]
del df["Masse"]
del df["Radiuse"]
df.dropna()
print(df.head())
