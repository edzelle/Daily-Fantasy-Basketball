import pandas as pd
import numpy as np


dates = ['11-7-18']#,'11-8-18','11-9-18','11-11-18','11-13-18','11-14-18','11-15-18','11-16-18','11-17-18']
for date in dates:
	df = pd.read_csv("Sampled Lineups %s.csv" % date)
	stats = pd.read_csv("../Player Power Index %s.csv" % date)

	## Create a dictionary with Player:Points
	points = {}
	for index, row in stats.iterrows():
		points[row[2]] = row[3]

	min_score = 0
	for index, row in df.iterrows():
		if row[8] == 0:
			break
		else:
			min_score = row[7]

	## This scripts computes the power indicies of an assortment of lineups by position
	## It exports a csv file with the following columns: Player, Pos, Salary, Points, Index for each player in the dataset
	## Methodology:
	## 1. Group dataframe by position (already specified by the columns)
	## 2. Create a 5 dictionaries and populate them with tuples (Player: 0) for each player with that valid position
	## 3. Create 5 more dictionaries and populate them with the same thing as above. These dictionaries will count the total number of appearances for a player at a position
	## 4. Iterate of the dataframe and count 1 for when a player appears in a winning lineup and 1 for any appearance. 

	PGs = df['PG'].tolist()
	SGs = df['SG'].tolist()
	SFs = df['SF'].tolist()
	PFs = df['PF'].tolist()
	Cs = df['C'].tolist()

	players = []
	pos = []
	idxs = []

	PG_W = {}
	SG_W = {}
	SF_W = {}
	PF_W = {}
	C_W = {}


	for i in PGs:
		if i not in PG_W:
			PG_W[i] = 0



	for i in SGs:
		if i not in SG_W:
			SG_W[i] = 0



	for i in SFs:
		if i not in SF_W:
			SF_W[i] = 0
		


	for i in PFs:
		if i not in PF_W:
			PF_W[i] = 0


	for i in Cs:
		if i not in C_W:
			C_W[i] = 0
		
	PGB_points = 0
	SGB_points = 0
	SFB_points = 0
	PFB_points = 0
	CB_points = 0

	for index, row in df.iterrows():
		if row[8] == 1:
			if row[7] - points[row[1]] < min_score:
				PG_W[row[1]] +=1
				PGB_points += 1
			if row[7] - points[row[2]] < min_score:
				SG_W[row[2]] +=1
				SGB_points += 1
			if row[7] - points[row[3]] < min_score:
				SF_W[row[3]] +=1
				SFB_points += 1
			if row[7] - points[row[4]] < min_score:
				PF_W[row[4]] +=1
				PFB_points += 1
			if row[7] - points[row[5]] < min_score:
				C_W[row[5]] +=1	
				CB_points += 1
	


	## Lastly, Compute the power incidicies for each player at each position

	for key in PG_W.keys():
		players.append(key)
		pos.append('PG')
		idxs.append(PG_W[key]/PGB_points)

	for key in SG_W.keys():
		players.append(key)
		pos.append('SG')
		idxs.append(SG_W[key]/SGB_points)

	for key in SF_W.keys():
		players.append(key)
		pos.append('SF')
		idxs.append(SF_W[key]/SFB_points)

	for key in PF_W.keys():
		players.append(key)
		pos.append('PF')
		idxs.append(PF_W[key]/PFB_points)

	for key in C_W.keys():
		players.append(key)
		pos.append('C')
		idxs.append(C_W[key]/CB_points)





	## Create a dataframe of these evaluaitons and save it

	data = {'Player': players, 'Pos': pos, 'Index': idxs}

	final = pd.DataFrame(data = data)
	final = final.sort_values('Player')
	final.to_csv("Positional Results\Positional Results %s.csv" %date, sep = ",")


print(";)")