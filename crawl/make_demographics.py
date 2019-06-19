# demographics: name, code, gender, affiliation, seniority, pub_rate, first_author_por, avg_coauthor
from unidecode import unidecode
import sexmachine.detector as gender
d = gender.Detector(case_sensitive=False, unknown_value="")


author_names = {}
current_year = 2019

with open("../csv/authors_unique.csv") as f_authors:
	f_authors.readline()
	for line in f_authors:
		line = line.strip()
		parts = line.split(",")
		author_code = parts[0]
		author_name = parts[1]
		author_name = author_name.strip()
		author_names[int(author_code)] = author_name


with open("../csv/basic_demographics.csv") as f, open("../csv/demographics.csv","w") as f_out:
	# write header
	f_out.write("author_name,author_id,gender,affiliation,seniority,nb_publi,pub_rate,first_author_por,avg_coauthor\n")
	f.readline()
	for line in f:
		line = line.strip()
		parts = line.split(",")
		author_id = parts[0]
		first_publication_year = parts[1]
		number_of_publications = parts[2].strip()
		number_of_first_author_publications = parts[3]
		number_of_coauthors = parts[4]
		affiliation = parts[5]
		affiliation = affiliation.strip()
		#affiliation  = unidecode(affiliation)
		author_name = author_names[int(author_id)]
		seniority = current_year - int(first_publication_year)
		first_author_por = int(round(float(number_of_first_author_publications) / float(number_of_publications), 2) * 100)
		avg_coauthor = round(float(number_of_coauthors) / float(number_of_publications),2)
		pub_rate = round(float(number_of_publications) / float(seniority),2)
		author_firstname = author_name.split(" ")[0]
		if "-" in author_firstname:
			first_part = author_firstname.split("-")[0]
			author_firstname = first_part
		gender = d.get_gender(author_firstname)
		if gender == "mostly_female":
			gender = "female"
		if gender == "mostly_male":
			gender = "male"
		final_out = author_name + "," + str(author_id) + "," + str(gender)+ "," +affiliation + "," +str(seniority)+ "," + str(number_of_publications) + "," + str(pub_rate)+ "," +str(first_author_por)+ "," +str(avg_coauthor)+"\n"
		
		f_out.write(final_out)