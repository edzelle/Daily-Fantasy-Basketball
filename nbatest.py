from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os
import statistics
import pandas as pd

def write_stats(flag, DK_scoring, FD_scoring, stdev_out):
	print("in write stats")
	DK_stdev = statistics.stdev(DK_scoring)
	DK_avg = statistics.mean(DK_scoring)
	FD_stdev = statistics.stdev(FD_scoring)
	FD_avg = statistics.mean(FD_scoring)

	stdev_header = ['Player', 'DK_ppm_stdev', 'DK_ppm_avg', 'FD_ppm_stdev', 'DF_ppm_avg']
	stdev_data = [player_name,DK_stdev,DK_avg,FD_stdev,FD_avg]


	if(flag == True):
		print("Writing to file with flag == true")
		with open(stdev_out, 'a') as f:
			writer2 = csv.writer(f, lineterminator = '\n')
			writer2.writerow(stdev_data)
	else:
		flag = True
		with open(stdev_out, 'w') as f:
			writer2 = csv.writer(f, lineterminator = '\n')
			writer2.writerow(stdev_header)
			writer2.writerow(stdev_data)	
	return flag


def clean_up(driver,csv_file):
	#print("in clean up")
	csv_file.close()
	

	
	filters = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[2]/div/div[2]/button")
	#test = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[2]/div/div[2]/button/span")

	time.sleep(1)
	driver.execute_script("window.scrollTo(0,0)")
	filters.click()

	reset = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[2]/div/div[3]")

	p2 = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[2]/div/div[4]")
	p2.click()
	X = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[1]/ul[1]/li[1]/span")
	X.click()
	
	end = time.time()


	print(end-start)
	return 

def grab_data(driver, writer,stdev_out,flag):
	#print("in grab data")
	try:	
		for i in range(1,201):
			if i % 50 == 0:
				print(i)
			player = player_name
			team = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[2]" % i).text,
			date = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[3]" % i).text
			matchup = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[4]" %i).text
			#wl = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[5]"%i).text
			mins = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[6]"%i).text)
			pts = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[7]"%i).text)
			#fgm = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[8]"%i).text
			#fga = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[9]"%i).text
			#fgp = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[10]"%i).text
			#tpm = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[11]"%i).text
			#tpa = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[12]"%i).text
			#tpp = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[13]"%i).text
			#ftm = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[14]"%i).text
			#fta = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[15]"%i).text
			#ftp = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[16]"%i).text
			#oreb = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[17]"%i).text
			#dreb = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[18]"%i).text
			reb = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[19]"%i).text)
			ast = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[20]"%i).text)
			stl = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[21]"%i).text)
			tov = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[22]"%i).text)
			blk = int(driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[23]"%i).text)
			#pf = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[24]"%i).text
			#pm = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[1]/div[1]/table/tbody/tr[%d]/td[25]"%i).text
			doubles = reb / 10 + pts / 10 + ast / 10 + blk / 10
			if doubles >= 2:
				dd = 1
			else: dd= 0 
			if doubles >= 3:
				td = 1
			else: td = 0





			## This part calculates the fantasy points for each day: ##
				
				
			FD_pts = pts+ 1.5*ast + 1.2*reb + 3*stl + 3*blk -1*tov
			try:
				FD_ppm = FD_pts / mins
				FD_scoring.append(FD_ppm)
			except:
				FD_scoring.append(0)

				
			DK_pts = pts + 1.5*ast + 1.25*reb + 2*stl + 2*blk -.5*tov + 1.5*dd+ 3*td
			try:
				DK_ppm = DK_pts / mins
				DK_scoring.append(DK_ppm)
			except:
				DK_scoring.append(0)

			#row = [player, team, date, matchup, wl, mins, pts, fgm, fga, tpm, tpa, tpp, ftm, fta, ftp, oreb, dreb, reb, ast, stl, tov, blk, pf, pm]
			row = [player, team, date, matchup, mins, pts, reb, ast, stl, tov, blk, dd, td, FD_pts, DK_pts]
			writer.writerow(row)
			#print("row written %s" %row)
		flag = write_stats(flag= flag, DK_scoring = DK_scoring, FD_scoring= FD_scoring, stdev_out = stdev_out)
	
		return flag

	except:
		print("Dumb execption in grab data")
		flag = write_stats(flag= flag, DK_scoring = DK_scoring, FD_scoring= FD_scoring, stdev_out = stdev_out)
		return flag	
		
		
	

X = pd.read_csv("player list.csv")
players = X['Name'].tolist()


driver = webdriver.Chrome()

driver.get("https://stats.nba.com/search/player-game/#")
stdev_out =  "Player Data/missed_fantasy_players_stdev.csv"

header = ['PLAYER', 'TEAM','DATE','MATCHUP', 'MIN', 'PTS',  'REB', 'AST','STL', 'TOV', 'BLK', 'DD', 'TD', 'FD_pts', 'DK_pts']


element = driver.find_element_by_xpath("//*[@id='custom-filters']/div/table/tbody/tr/td[4]/button")



element.click() ## Deletes the filter for 30 point games searches



run = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[2]/div/div[2]/stats-run-it/button") 
## the run element is the button to run the query

time.sleep(1)
## This next part allows for player names to be entered in the search box ##
element = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div")
element.click()

player_element = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[1]/ul[1]/li[1]/input")


## Uncomment to test script with just a few players ##
#players = ["Grayson Allen", "Anthony Davis", "Kyrie Irving", "Lebron James", "Derrick Rose", "Chris Paul", "Kevin Durant", "James Harden", "Andrew Wiggins", "Towns", "Zach Lavine"]

execptions = []
flag = False


for player_name in players:
	try:
		start = time.time()
		print(player_name)

		outfile = "./Player Data/%s Stats.csv" %player_name
		csv_file = open(outfile, 'w')
		writer = csv.writer(csv_file, lineterminator = '\n')
		writer.writerow(header)

		FD_scoring = []
		DK_scoring = []

		time.sleep(1)
		#print(player_name)
		player_element.send_keys(player_name)
		time.sleep(1)
		temp = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[1]/ul[2]/li")
		temp.click()
		time.sleep(1)
		element.click()
		time.sleep(1)
		run.send_keys(Keys.RETURN)
		time.sleep(2)


		driver.execute_script("window.scrollTo(0,0)")
		try: ## For players with less than 50 rows: need to make sure this doesn't mess up
			load_more = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[2]/div/a") 
			load_more.click()
			load_more.click()
			load_more.click()
		except:
			time.sleep(2)
			try:
				load_more = driver.find_element_by_xpath("//*[@id='stat-table']/nba-stat-table/div[2]/div/a")
				load_more.click()
				load_more.click()
				load_more.click()
			except:
				try: 
					flag = grab_data(driver = driver, stdev_out= stdev_out, writer=writer, flag=flag)
					csv_file.close()
					clean_up(driver = driver, csv_file = csv_file)
					continue
				except:
				#	print("I fucked up")
					csv_file.close()
					clean_up(driver = driver, csv_file = csv_file)
					print("Finished early, should continue")
					continue

		

		## Match up categories with XPATHS ## 
		## Notes: The tr[index] specifies the row of the table. The td[index] specifies the columns
		#print("in the real loop")
		print("In second grab data")
		flag = grab_data(driver = driver, stdev_out= stdev_out, writer=writer, flag=flag)
		
		clean_up(driver = driver, csv_file = csv_file)
		
	except:
		##Something went wrong in retriving the player data: ##
		## Log player name and continue ##
		execptions.append(player_name)
		time.sleep(5)
		filters = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[2]/div/div[2]/button")
		#test = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[2]/div/div[2]/button/span")

		time.sleep(1)
		driver.execute_script("window.scrollTo(0,0)")
		filters.click()

		reset = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[2]/div/div[3]")

		p2 = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[2]/div/div[4]")
		p2.click()
		X = driver.find_element_by_xpath("//*[@id='streak-finder']/div[2]/section/div/div[3]/div/div/form/div/section[5]/div/div[1]/ul[1]/li[1]/span")
		X.click()
		
		end = time.time()

driver.close()

with open("Missed Players.csv", 'w') as f:
	writer3 = csv.writer(f, lineterminator = '\n')
	for i in execptions:
		writer3.writerow(i)
