# pip install pandas
import pandas as pd

file = pd.read_csv(r'./valeursfoncieres-2020.txt', delimiter='|')
csv = file.to_csv(r'./data.csv')
