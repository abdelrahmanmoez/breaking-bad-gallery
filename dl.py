from BeautifulSoup import BeautifulSoup
import urllib
import os

base_link = "http://galleryroulette.com/movies-t-v/a-poster-for-every-single-episode-of-breaking-bad/?subpage="
base_dir = "Breaking bad"

for x in range(1, 63):
	# Form the link
	link = base_link+str(x)
	print "Downloading image "+str(x)+ " ..."
	# Open link
	url = urllib.urlopen(link)
	content = url.read()
	
	soup = BeautifulSoup(content)
	# Scrape title
	title = soup.find("div", {"class": "item-description"}).text
	title = title.replace("/", "-")[3:]
	file_name = title+".jpg"
	
	# Scrape image
	img_src = soup.find("div", {"id": "item-images"}).find("img")['src']
	img_dst = os.path.join(base_dir, file_name)

	# Download image
	urllib.urlretrieve(img_src, img_dst)

# Beep
print "\a\a\a\a\a"
