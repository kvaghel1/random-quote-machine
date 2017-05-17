from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import requests

def get_page(web_url):
	hdr = {'User-agent':'Mozilla/5.0'}
	req = Request(web_url,headers = hdr)

	page = urlopen(req)
	soup = BeautifulSoup(page,"html.parser")

	#print (soup)

	soup_divs = soup.find('div',{'class':'m-brick grid-item boxy bqQt'})
	#print (soup_divs)
	
	#a tag class = "b-qt qt_371189 oncl_q"
	soup_quote_text = soup.findAll('a',{'title':'view quote'})
	print (len(soup_quote_text))

	

if __name__ == "__main__":

	pagination_number = 1
	while(True):
		url = "https://www.brainyquote.com/quotes/topics/topic_motivational"+str(pagination_number)+".html?vm=l"
		print (url)
		get_page(url)
		pagination_number += 1
		print (pagination_number)
		#a = input("Continue?")




