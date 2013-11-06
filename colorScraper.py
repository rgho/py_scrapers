from bs4 import BeautifulSoup
import urllib2
import string



def getURL(url):
	return urllib2.urlopen(url).read()

def scrapeData():
	#define a url to scrap from
	url = 'http://www.colorhexa.com/color-names'
	#define a 
	soup = BeautifulSoup(getURL(url))
	# get all a tags.
	a_tags = soup.find_all('a')

	#remove the a tag line that dont have relevant data.
	a_tags = a_tags[7:-3] # first 7 are from other parts of the doc last 2 are other.
	names = []
	hexs =[]
	for tagged_line in a_tags:
		#MUST force str type for wierd stuff to not happen.
		line = str(tagged_line)
		if ('#' in line) != True:#removes duplicates sibling a tags.
			# GRAB LINE DATA AND PARSE
			data = line.replace('<a href="/','').replace('</a>','').split('">')
			names.append(data[0])
			hexs.append(data[1])
	
	print names
	print hexs

def listPrint(thelist):
	for i in thelist:
		print i

scrapeData()

