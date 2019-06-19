from __future__ import unicode_literals
from pattern3.web import URL
import urllib
from bs4 import BeautifulSoup
from unidecode import unidecode

conferences = ["WWW","VLDB","SIGMOD","ICWSM","ICDE","SIGIR","CIKM","DEXA1","DEXA2","DEXA3","RecSys","EDBT", "HILDA"]

# The substring REPLACE should be replaced by year
conference_link={}
conference_link["WWW"]="http://dblp.uni-trier.de/db/conf/www/wwwREPLACE.html"
conference_link["VLDB"]="http://dblp.uni-trier.de/db/journals/pvldb/pvldbREPLACE.html"
conference_link["SIGMOD"]="http://dblp.uni-trier.de/db/conf/sigmod/sigmodREPLACE.html"
conference_link["ICWSM"]="http://dblp.uni-trier.de/db/conf/icwsm/icwsmREPLACE.html"
conference_link["ICDE"]="http://dblp.uni-trier.de/db/conf/icde/icdeREPLACE.html"
conference_link["SIGIR"]="http://dblp.uni-trier.de/db/conf/sigir/sigirREPLACE.html"
conference_link["CIKM"]="http://dblp.uni-trier.de/db/conf/cikm/cikmREPLACE.html"
conference_link["DEXA1"]="http://dblp.uni-trier.de/db/conf/dexa/dexaREPLACE.html"
conference_link["DEXA2"]="http://dblp.uni-trier.de/db/conf/dexa/dexaREPLACE-1.html"
conference_link["DEXA3"]="http://dblp.uni-trier.de/db/conf/dexa/dexaREPLACE-2.html"
conference_link["RecSys"]="http://dblp.uni-trier.de/db/conf/recsys/recsysREPLACE.html"
conference_link["EDBT"]="http://dblp.uni-trier.de/db/conf/edbt/edbtREPLACE.html"
conference_link["HILDA"]="https://dblp.org/db/conf/sigmod/hildaREPLACE.html"

# the year that each confernce has begun. We are interested to 2006-2016.
conference_first_year={}
conference_first_year["WWW"]=2006
conference_first_year["VLDB"]=2008
conference_first_year["SIGMOD"]=2006
conference_first_year["ICWSM"]=2007
conference_first_year["ICDE"]=2006
conference_first_year["SIGIR"]=2006
conference_first_year["CIKM"]=2006
conference_first_year["RecSys"]=2007
conference_first_year["EDBT"]=2008
conference_first_year["DEXA2"]=2010
conference_first_year["DEXA3"]=2010
conference_first_year["DEXA1"]=2007
conference_first_year["HILDA"]=2016

conference_last_year={}
conference_last_year["WWW"]=2018
conference_last_year["VLDB"]=2018
conference_last_year["SIGMOD"]=2018
conference_last_year["ICWSM"]=2018
conference_last_year["ICDE"]=2018
conference_last_year["SIGIR"]=2018
conference_last_year["CIKM"]=2018
conference_last_year["RecSys"]=2018
conference_last_year["EDBT"]=2018
conference_last_year["DEXA2"]=2018
conference_last_year["DEXA3"]=2018
conference_last_year["DEXA1"]=2009
conference_last_year["HILDA"]=2018

# out file
fout = open("../csv/authors.csv","w")

# print header
fout.write("author_name, dblp_link, seen_in_conf, year\n")

for conference in conferences:
	for year in range(conference_first_year[conference],conference_last_year[conference]+1):
		current_link = ""
		if conference == "VLDB":
			current_link = conference_link[conference].replace("REPLACE",str(year-2006))
		else:
			current_link = conference_link[conference].replace("REPLACE",str(year))
		current_page = urllib.request.urlopen(current_link).read()
		soup = BeautifulSoup(current_page, "lxml")
		author_spans = soup.findAll('span', itemprop="author", itemtype="http://schema.org/Person")
		for author_span in author_spans:
			author_internal_part = author_span('a')[0]
			author_link = author_internal_part["href"]
			author_name = unidecode(author_internal_part("span")[0].string)
			author_name = author_name.replace(",","")
			reported_conference = conference
			if conference[0:4]=="DEXA":
				reported_conference = "DEXA"
			# print author_name+", "+author_link+", "+reported_conference+", "+str(year)
			fout.write(author_name+", "+author_link+", "+reported_conference+", "+str(year)+"\n")
		print("done with "+conference+" "+str(year))