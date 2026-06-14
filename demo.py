
import PyWGCNA
import pandas as pd

# geneExp = "data/count_transposed.csv"
# geneExpPath = 'data/fpkm_1256.csv'
geneExpPath = "data/fpkm_1256.csv"
expressionList = pd.read_csv(geneExpPath, index_col=0)

# raw_df = pd.read_csv(geneExp).iloc[[0, 1, 4, 5]]
print(expressionList)
# exit()
sampleInfo = pd.DataFrame(index=expressionList.index)
sampleInfo['treatment'] = ['A', 'A', 'B', 'B']
print(sampleInfo)

# exit()
pyWGCNA_5xFAD = PyWGCNA.WGCNA(
    name='5xFAD', 
    species='mus musculus', 
    geneExp=expressionList, 
    # geneExpPath=geneExpPath,
    outputPath='1256',
    save=True,
    sampleInfo=sampleInfo
)

df = pyWGCNA_5xFAD.geneExpr.to_df()

print(df)

print("------------------")
pyWGCNA_5xFAD.preprocess()
print("-------preprocess end-----------")

print("-------findModules start-----------")
pyWGCNA_5xFAD.findModules()
print("-------findModules end-----------")

# print(df)


# pyWGCNA_5xFAD.geneExpr.to_df().head(5)





