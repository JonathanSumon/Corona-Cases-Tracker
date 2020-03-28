from bs4 import BeautifulSoup
import requests
import time

page = requests.get("https://www.worldometers.info/coronavirus/#countries")
soup = BeautifulSoup(page.content,'html.parser')
table = soup.find(id="main_table_countries_today")
labels=[]

rows=table.find_all('tr')


a=[]
l=[]
m=[]


print("Welcome to RobotX Live Corona Tracker")

while(1):
	a=input("Country: ")
	print("Retrieving Data")
	print("\n")
	time.sleep(3)
	for record in rows:
		for data in record.find_all('td'):
			l.append(data.text)


	if a in l:
		pos=l.index(a)
		print("Total Cases :"+str(l[pos+1]))
		print("New Cases :"+str(l[pos+2]))
		print("Total Deaths :"+str(l[pos+3]))
		print("New Deaths :"+str(l[pos+4]))
		print("Active Cases :"+str(l[pos+6]))
		print("Serious/Critical :"+str(l[pos+7]))
		print("\n")
