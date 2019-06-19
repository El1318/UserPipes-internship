from __future__ import unicode_literals
# from pattern.web import URL
import urllib
from bs4 import BeautifulSoup
# from unidecode import unidecode

topics = []
topic_codes = {}
with open("../csv/db_keywords.csv") as ftopics:
	for line in ftopics:
		line = line.strip()
		parts = line.split(",")
		topics.append(parts[1])
		topic_codes[parts[1]] = parts[0]

author_ids = []
dblp_links = []
with open("../csv/authors_unique.csv") as f:
	f.readline()
	for line in f:
		line = line.strip()
		parts = line.split(",")
		author_ids.append(parts[0])
		dblp_links.append(parts[2])
		
start = 7441
end = len(author_ids)
# (6009,7009) !
# (7441, )    !

# publications.csv < author_id, paper_title, paper_conference, paper_year, nb_authors, is_first_author, topics (separated by ":"") >
# basic_demographics.csv < author_id, first_publication_year, number_of_publications, number_of_first_author_publications, number_of_coauthors, affiliation >
with open("../csv/publications.csv","a") as fout1, open("../csv/basic_demographics.csv","a") as fout2:
	#fout2.write("author_id, first_publication_year, number_of_publications, number_of_first_author_publications, number_of_coauthors, affiliation \n")
	#fout1.write("author_id, paper_title, paper_conference, paper_year, nb_authors, is_first_author, topics \n")

	# loop on authors
	for i in range(start,end):
		author_id = author_ids[i] 
		dblp_link = dblp_links[i]
		# if int(author_id) > 10000:
		# 	exit()
		# if int(author_id) < 7000:
		# 	continue
		current_page = urllib.request.urlopen(dblp_link).read()
		soup = BeautifulSoup(current_page,"html.parser")

		affiliation = ""
		affiliation_span = soup.findAll(itemprop="affiliation", itemtype="http://schema.org/Organization")
		if len(affiliation_span) > 0:
			affiliation = affiliation_span[0].span.string
		affiliation = affiliation.replace(",","")
		
		first_publi_year = 2018

		# loop on author papers
		number_of_first_author_publications = 0
		number_of_coauthors = 0
		paper_divs = soup.findAll('div', itemprop="headline", class_="data")
		number_of_publications = str(len(paper_divs))
		for paper_div in paper_divs:
			author_spans = paper_div.findAll('span', itemprop="author", itemtype="http://schema.org/Person")
			being_first_author = author_spans[0].findAll('span', itemprop="name", class_="this-person")
			is_first_author = "false"
			if len(being_first_author) > 0:
				is_first_author = "true"
				number_of_first_author_publications += 1
			nb_authors = len(author_spans)
			number_of_coauthors += nb_authors
			paper_title = paper_div.findAll('span', itemprop="name", class_="title")
			paper_title_clean = ""
			c = paper_title[0].contents
			# try:
		
			for cc in c:
				try:
					temp = cc.string
					paper_title_clean += temp
				except:
					temp = ""
				#	paper_title_clean += temp	
				
			paper_title_clean = paper_title_clean[:-1].lower()
			paper_title_clean = paper_title_clean.replace(",","")
			# except:
			# 	print paper_title
			# 	print c
					
			paper_topics = ""
			for topic in topics:
				if topic in paper_title_clean:
					paper_topics += topic+":"
					
			paper_conference =""
			paper_conf_span = paper_div.findAll('span', itemprop="isPartOf")
			if len(paper_conf_span)>0:
				l = paper_conf_span[0].findAll('span', itemprop="name")
				if len(l) > 0:
					paper_conference = l[0].string

			paper_conference = paper_conference.replace(",","")	
				# if s.find("<span itemprop=\"name\">"):
				# 	print paper_conference, "**"
				# 	print s
		
			paper_year_span = paper_div.findAll('span', itemprop="datePublished")
			paper_year = paper_year_span[0].string
			
			if int(paper_year) < first_publi_year:
				first_publi_year = int(paper_year)

			final_fout1 = author_id + ", " + paper_title_clean + ", " + paper_conference + ", " + str(paper_year) + ", " + str(nb_authors) + ", " + is_first_author + ", " + paper_topics + "\n"
			final_fout1 = final_fout1
			# print hello
			# exit()
			fout1.write(final_fout1)

		first_publication_year = first_publi_year
		fout2_final = author_id + ", " + str(first_publication_year) + ", " + str(number_of_publications) + ", " + str(number_of_first_author_publications) + ", " + str(number_of_coauthors) + ", " + affiliation + "\n"
		fout2_final = fout2_final
		fout2.write(fout2_final)
		if i%100 == 0:
			print(author_id, "done ...")