

import pandas as pd

# data_path = "data/count_transposed.csv"
geneExp = 'data/fpkm_transposed.csv'
df1 = pd.read_csv(geneExp)






raw_df = pd.read_csv(geneExp).iloc[[0, 1, 4, 5]]




print(raw_df)

raw_df.to_csv('data/fpkm_1256.csv')

