import pandas as pd

df = pd.DataFrame([
                   {'First':'Bill'
                    ,'Last':'Thompson'
                    ,'AcctNum':'0001'
                   ,'AcctValue':100},
                   {'First':'James'
                    ,'Last':'Winters'
                    ,'AcctNum':'0002'
                    ,'AcctValue':200},
                   {'First':'Anna'
                    ,'Last':'Steele'
                    ,'AcctNum':'0003'
                    ,'AcctValue':300},
                   {'First':'Sean'
                    ,'Last':'Reilly'
                    ,'AcctNum':'0004'
                    ,'AcctValue':400}
                   ])

# Select data and set it to a variable
account_value = df.loc[df['AcctNum'] == '0003']['AcctValue'].values[0]
print (account_value)