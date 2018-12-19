import pandas as pd
import numpy as np

date = "11-12-18"
df = pd.read_csv("Player Stats %s.csv" % date) ## Loads stats data #3

df = df.drop(df.columns[[29]], axis =1) ## Drops unused columns ##

dk = pd.read_csv("DKSalaries %s.csv" % date)

dk = dk.drop(dk.columns[[1,4,6,7,8,]], axis =1)

temp = dk.copy()
temp = temp.iloc[0:0]

for index, row in dk.iterrows(): ## This loop creats duplicate rows for each player by position
	if "/" not in row[0]:
		continue
	string = row[0]
	pos = string.split("/")
	for pos in pos:
		row[0] = pos
		temp = temp.append(row)

dk = temp ## dk is now the final list of all players and salaries, next step is to join with stats


final = pd.merge(dk,df,how = 'inner', right_on ="PLAYER", left_on = "Name") ## Joins columns on player name
final = final.drop(['Name'], axis = 1) ## Drops duplicate name attribute, the player can be indentified by PLAYER attribute


final.to_csv("Cleaned Datasets\Stats and Salary %s.csv" % date, sep = ",")

