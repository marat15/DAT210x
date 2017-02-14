import pandas as pd

#declare url variable with html address
url = 'http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'

#load the html table into a dataframe, header=1 means that there are headers in the table
df = pd.read_html(url,header=1)[0]

#rename table columns
df.columns=['RK','PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','G2','A2','G3','A3']

#drop rows (axis=0) where there is atleast 4 Nans present
df=df.dropna(axis=0,thresh = 4)
df
#drop duplicates from the table (specify column names)
df.drop_duplicates(subset=['PLAYER','TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','G2','A2','G3','A3'],inplace=True)

# drop RK column, axis =1 for columns, inplace=True - do the action to this table
df.drop('RK',1,inplace=True)

#drop row 11 in the dataframe, axis = 0 for rows
df.drop(11,0,inplace=True)

#Converting columns to appropriate types
df.PCT = pd.to_numeric(df.PCT, errors='coerce')
df.GP = pd.to_numeric(df.GP, errors='coerce')
df.G = pd.to_numeric(df.G, errors='coerce')
df.A = pd.to_numeric(df.A, errors='coerce')
df.PTS = pd.to_numeric(df.PTS, errors='coerce')
df["+/-"] = pd.to_numeric(df["+/-"], errors='coerce')
df.PIM = pd.to_numeric(df.PIM, errors='coerce')
df['PTS/G'] = pd.to_numeric(df['PTS/G'], errors='coerce')
df.SOG = pd.to_numeric(df.SOG, errors='coerce')
df.GWG = pd.to_numeric(df.GWG, errors='coerce')
df.G2 = pd.to_numeric(df.G2, errors='coerce')
df.A2 = pd.to_numeric(df.A2, errors='coerce')
df.G3 = pd.to_numeric(df.G3, errors='coerce')
df.A3 = pd.to_numeric(df.A3, errors='coerce')
df.dtypes
#reset the index in hte dataframe
df.PCT.unique().size

