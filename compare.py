import pandas as pd

i = 0
csv = []

while True:
    i = str(input('Give me a CSV or press ENTER to start comparing'))
    if i != '':
        i = i.replace('\\','')
        if i[-1] = '':
            i = i[:-1]
        csv.append(i)
    else:
        break

dfs = []
for i in csv:
    df = pd.read_csv(i)
    dfs.append(df)

dfu = pd.concat(dfs)
dfu = dfu.drop_duplicates()
dfu.to_csv('output.csv')
