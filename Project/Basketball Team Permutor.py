import pandas as pd
import numpy as np

dates = ['11-7-18','11-8-18','11-9-18','11-11-18','11-13-18','11-14-18','11-15-18','11-16-18','11-17-18']

for date in dates:
	print("Working on date %s" % date)
#date = "11-7-18"
	df = pd.read_csv("Cleaned Datasets\Stats and Salary %s.csv" % date) ## Dataframe is already sorted by salary as it is loaded in

	Salary = 31500

	df['Score'] = df['PTS'] + .5*df['3PM'] + 1.25*df['REB'] + 1.5*df['AST'] + 2*df['STL'] + 2*df['BLK'] - .5*df['TOV'] +1.5*df['DD2'] + 3*df['TD3']


	drop_cols = set(range(34)) - set([1,3,4,33])
	df = df.drop(df.columns[list(drop_cols)], axis =1)

	PGs = df.loc[df['Position'] == 'PG']
	SGs = df.loc[df['Position'] == 'SG']
	SFs = df.loc[df['Position'] == 'SF']
	PFs = df.loc[df['Position'] == 'PF']
	Cs = df.loc[df['Position'] == 'C']

	PG_count = 1
	SG_count = 1
	SF_count = 1
	PF_count = 1
	C_count = 1

	cols = ['PG','SG','SF','PF','C','Price','Score']


	num_lineps = 50

	i = 0

	rosters = [cols]

	while(i < num_lineps):
		## Selection algorithm ## 
		## Pick a random position from the pos array ##
			## If pos_count < 0
			## Select one player randomly and subtract Salary from the total ##
			## Continue until either salary = 0 or no more positions remain ##
		PG = PGs.sample(n=1)
		SG = SGs.sample(n=1)
		SF = SFs.sample(n=1)
		PF = PFs.sample(n=1)
		C = Cs.sample(n=1)


		lineup = pd.DataFrame()
		lineup = lineup.append(PG)
		lineup = lineup.append(SG)
		lineup = lineup.append(SF)
		lineup = lineup.append(PF)
		lineup = lineup.append(C)

		lineup.drop_duplicates()


		
		score = lineup['Score'].sum()
		price = lineup['Salary'].sum()
		roster = lineup['PLAYER'].tolist()
		sr = set(roster)

		if len(sr) < 5:
			continue

		if price > Salary:
			continue
		
		roster.append(price)
		roster.append(score)

		rosters.append(roster)

		i+=1
		if i%10000 == 0:
			print(i)

	final = pd.DataFrame(rosters, columns = rosters.pop(0))  ## Creates a dataframe of lineups that are randomly sampled from the off all posisble lineups
	final = final.drop_duplicates()


	win = np.ones(len(final))



	## To Do: ##
	## 1. Mark winning lineups
		## 1. Sort final by score ascending
		## 2. Create column of 1s, and 0s that correspond to the winning lineups
		## 3. Append to dataframe

	win = np.zeros(len(final))
	final = final.sort_values(['Score'], ascending = False)

	num_winners = int((len(final))*.15)
	win[0:num_winners] = 1
	min_score = final.iloc[num_winners]['Score']
	final['Win']= win

	## 2. Compute index for each player (May want to use a new file for this)
	## Want to export a csv with Player, Salary, Index, Score, based on these values
		## Count total number of player appearances
		## Count total nunber of player appearances in winning lineups
		## Compute Index, Index to Salary and plot on axis


	## Creates the backbone of the exported csv, needs to add index
	players = df.drop(df.columns[0],axis = 1)
	players= players.drop_duplicates()



	appearances = {}
	winning_appearances = {}
	p_scores = {}
	B_points = 0

	for row, index in players.iterrows():
#		appearances[index[1]] = 0
		p_scores[index[1]] = index[2]
		winning_appearances[index[1]] = 0	 


	for row, index in final.iterrows():
		if index[7] == 1: ## If coalition is winning 
			if index[6] - p_scores[index[1]] < min_score:
				winning_appearances[index[1]] += 1
				B_points += 1
			if index[6] - p_scores[index[2]] < min_score:
				winning_appearances[index[2]] += 1
				B_points += 1
			if index[6] - p_scores[index[3]] < min_score:
				winning_appearances[index[3]] += 1
				B_points += 1
			if index[6] - p_scores[index[4]] < min_score:
				winning_appearances[index[4]] += 1
				B_points += 1
			if index[6] - p_scores[index[0]] < min_score:
				winning_appearances[index[0]] += 1
				B_points += 1
#		appearances[index[1]] += 1
#		appearances[index[2]] += 1
#		appearances[index[3]] += 1
#		appearances[index[4]] += 1
#		appearances[index[0]] += 1

	power_index = []

	for row, index in players.iterrows():
		try:
			power_index.append(winning_appearances[index[1]]/B_points)
		except(ZeroDivisionError):
			power_index.append(0)
	players['Power Index'] = power_index

	## Export the players dataframe to a csv for further analytics

	#players.to_csv("Cleaned Datasets\Power Index\Player Power Index %s.csv" % date, sep = ",")
	#final.to_csv("Cleaned Datasets\Power Index\Sample Lineups\Sampled Lineups %s.csv" % date, sep= ",")