from bs4 import BeautifulSoup
import urllib2
import string
import json






def getURL(url):
	return urllib2.urlopen(url).read()

def scrapeData():
	#define a url to scrap from
	# another one to scrape from http://www.color-hex.com/color-names.html
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
			hexs.append(data[0])
			names.append(data[1])
	
	#print names
	#print hexs

	# LOOP AND BUILD A DICT
	output = {}
	for index in range(len(names)):
		output[names[index]] = hexs[index]
	#SAVE DICT AS JSON
	save_as_json(output,'hex-human-colors.txt')



def dict_to_json(my_dict):
    return json.dumps(my_dict)

def write_to_file(filename, data):
    target = open(filename, 'w')
    target.write(str(data))
    target.close
    return True

def save_as_json(knowledge_dict, filename):
    write_to_file(filename, dict_to_json(knowledge_dict))    


def listPrint(thelist):
	for i in thelist:
		print i

scrapeData()

