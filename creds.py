import pandas as pd

df = pd.read_csv("secretCSV.csv", usecols = ['client','uname','passw','stoken'])
indxvar = 0
rownumvar = df.shape[0]

print(indxvar, rownumvar)

while indxvar < rownumvar:
    orgname = df.loc[[indxvar],'client'].values[0]
    username = df.loc[[indxvar],'uname'].values[0]
    password = df.loc[[indxvar],'passw'].values[0]
    sectocken = df.loc[[indxvar],'stoken'].values[0]

    print(orgname, username, password, sectocken)
    indxvar += 1

