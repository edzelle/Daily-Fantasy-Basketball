import pandas as pd
import numpy as np

class Lineup:
	def __init__(self,PG,SG,SF,PF,C):
		self.PG = PG[[2]]
		self.SG = SG[[2]]
		self.SF = SF[[2]]
		self.PF = PF[[2]]
		self.C = C[[2]]
		self.price = PG[[1]] + SG[[1]] + SF[[1]] + PF[[1]] + C[[1]]
		self.points = PG[[3]] + SG[[3]] + SF[[3]] + PF[[3]] + C[[3]]

	def Verbose(self):
		print("Lineup: %s, %s, %s, %s, %s" %PG %SG %SF %PF %C)

	def getscore(self):
		return points

	def getprice(self):
		return self.price