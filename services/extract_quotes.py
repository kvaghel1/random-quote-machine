from urllib.request import Request,urlopen,urlretrieve
from bs4 import BeautifulSoup
import requests
#import urllib
import os
import shutil

def get_image(web_url,file_name):
	hdr = {'User-agent':'Mozilla/5.0'}
	req = Request(web_url,headers = hdr)

	page = urlopen(req)
	soup = BeautifulSoup(page,"html.parser")

	r = requests.get(web_url,stream=True, headers=hdr)
	if r.status_code == 200:
		with open(file_name, 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)
	else:
		print (r.status_code)


def get_page(web_url):
	hdr = {'User-agent':'Mozilla/5.0'}
	req = Request(web_url,headers = hdr)

	page = urlopen(req)
	soup = BeautifulSoup(page,"html.parser")

	#print (soup)

	soup_divs = soup.find('div',{'class':'m-brick grid-item boxy bqQt'})
	#print (soup_divs)
	
	base_url = "https://www.brainyquote.com"
	#a tag class = "b-qt qt_371189 oncl_q"
	#print (soup_divs)
	soup_quote_text = soup_divs.findAll('a',{'class':'oncl_q'})

	for quote in soup_quote_text:
		quote_json = {}
		
		quote_text = quote.find('img')['alt']
		print (quote_text)
		
		img_src_url = quote.find('img')['src']
		quote_id = img_src_url.split("/")[4]+"_"+img_src_url.split("/")[5]
		print (quote_id)
		
		quote_json["quote_id"] = quote_id
		quote_json["quote_text"] = quote_text
		quote_json["quote_img_url"] = base_url + img_src_url

		print (quote_json)
		a = input("stop")

def create_url(topic_name):
	pagination_number = 1
	topic_name = topic_name.replace(" ","")
	url = "https://www.brainyquote.com/quotes/topics/topic_"+str(topic_name)+str(pagination_number)+".html?vm=l"
	return url

if __name__ == "__main__":

	
	while(True):
		#https://www.brainyquote.com/quotes/topics/topic_motivational.html?vm=l
		url = create_url("motivational")
		print (url)
		get_page(url)
		pagination_number += 1
		print (pagination_number)
		a = input("Continue?")




