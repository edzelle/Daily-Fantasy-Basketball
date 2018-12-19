import pandas as pd
import numpy as np

df = pd.read_csv("Test Data.csv")

Salary = 100

df = df.sort(column = 'Salary', ascending = False)

QBs = df.loc[df['Position'] == 'QB']
RBs = df.loc[df['Position'] == 'RB']
WRs = df.loc[df['Position'] == 'WR']
TEs = df.loc[df['Position'] == 'TE']
D = df.loc[df['Position'] == 'D']

QB_count = 1
RB_count = 2
WR_count = 2
TE_count = 1
D_count = 1

pos = ['QB','RB','WR','TE','D']

i = 0

while(i < 100):
	## Selection algorithm ## 
	## Pick a random position from the pos array ##
		## If pos_count < 0
		## Select one player randomly and subtract Salary from the total ##
		## Continue until either salary = 0 or no more positions remain ##
	num 