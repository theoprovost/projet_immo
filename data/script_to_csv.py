# pip install pandas
import pandas as pd

file = pd.read_csv(r'./data/valeursfoncieres-2020.txt', delimiter='|')
file.fillna('null')

file.to_csv(r'./data/data.csv')
