user_id = {}

with open("../csv/demographics.csv") as f:
	f.readline()

	for line in f:
		line = line.strip()
		parts = line.split(",")
		id_ = int(parts[1])

		if parts[2] == 'male':
			gender = 1
		elif parts[2] == 'female':
			gender = 2
		else:
			gender = ''

		affiliation = parts[3]
		country = ''

		#USA #101 North America
		if ('USA' in affiliation) or ('State' in affiliation) or ('Chicago' in affiliation) or ('Georgia' in affiliation) or ('Pennsylvania' in affiliation) or ('Massachusetts' in affiliation) or ('Stanford' in affiliation) or ('Harvard' in affiliation) or ('New York' in affiliation) or ('California' in affiliation) or ('Ohio' in affiliation) or ('Maryland' in affiliation) or ('Utah' in affiliation) or ('Seattle' in affiliation) or ('Virginia' in affiliation) or ('Arizona' in affiliation) or ('Michigan' in affiliation) or ('Duke' in affiliation) or ('Palo Alto' in affiliation):
			country = 101
		#102 UK/Ireland 
		if ('UK' in affiliation) or ('London' in affiliation) or ('Bedfordshire' in affiliation) or ('Scotland' in affiliation) or ('Oxford' in affiliation) or ('Aberdeen' in affiliation) or ('Manchester' in affiliation):
			country = 102
		#Germany #103 Europe
		if ('Germany' in affiliation) or ('Berlin' in affiliation) or ('Munich' in affiliation) or ('München' in affiliation) or ('Saarland' in affiliation) or ('Hagen' in affiliation) or ('Darmstadt' in affiliation) or ('Reutlingen' in affiliation) or ('Kaiserslautern' in affiliation) or ('Karlsruhe' in affiliation) or ('Freiburg' in affiliation) or ('Stuttgart' in affiliation) or ('Aachen' in affiliation) or ('Dresden' in affiliation) or ('Tübingen' in affiliation):
			country = 103
		#France
		if ('France' in affiliation) or ('Avignon' in affiliation) or ('Paris' in affiliation) or ('Versailles' in affiliation) or ('Toulouse' in affiliation) or ('Marseille' in affiliation) or ('Nancy' in affiliation):
			country = 103
		#Italy
		if ('Italy' in affiliation) or ('Rome' in affiliation) or ('Turin' in affiliation) or ('Milan' in affiliation) or ('Padua' in affiliation) or ('Pisa' in affiliation):
			country = 103
		#China #122 Asia
		if ('China' in affiliation) or ('Hong Kong' in affiliation) or ('Chinese' in affiliation) or ('Peking' in affiliation) or ('Zhejiang' in affiliation):
			country = 122
		#Australia
		if ('Australia' in affiliation) or ('Queensland' in affiliation):
			country = 107
		#Canada
		if ('Canada' in affiliation) or ('Toronto' in affiliation) or ('Waterloo' in affiliation):
			country = 101
		#Netherlands
		if 'Netherlands' in affiliation:
			country = 103
		#South America
		if ('Brazil' in affiliation) or ('Chile' in affiliation) or ('Venezuela' in affiliation) or ('Mexico' in affiliation):
			country = 110
		#Switzerland
		if ('Switzerland' in affiliation) or ('Zurich' in affiliation) or ('Zürich' in affiliation):
			country = 103
		#Israel #123 Middle East
		if ('Israel' in affiliation) or ('Tel Aviv' in affiliation):
			country = 123
		#Singapore #122 Asia
		if ('Singapore' in affiliation) or ('Nanyang' in affiliation):
			country = 122
		#India #122 Asia
		if ('India' in affiliation) or ('Bombay' in affiliation):
			country = 122
		#Spain
		if ('Spain' in affiliation) or ('Madrid' in affiliation) or ('Catalunya' in affiliation):
			country = 103
		#Austria
		if ('Austria' in affiliation) or ('Vienna' in affiliation):
			country = 103
		#UK/Ireland
		if 'Ireland' in affiliation:
			country = 102
		#Greece
		if ('Greece' in affiliation) or ('Hellas' in affiliation) or ('Athens' in affiliation) or ('Athena' in affiliation) or ('Piraeus' in affiliation) or ('Crete' in affiliation):
			country = 103
		#Japan #122 Asia
		if ('Japan' in affiliation) or ('Tokyo' in affiliation) or ('Kyoto' in affiliation):
			country = 122
		#Scandinavia
		if ('Norway' in affiliation) or ('Sweden' in affiliation) or ('Finland' in affiliation) or ('Helsinki' in affiliation):
			country = 103
		#otherEU: Denmark, Belgium, Portugal, Hungary, Czech, Poland, Slovenia, Luxembourg, Estonia, Bratislava
		if ('Denmark' in affiliation) or ('Belgium' in affiliation) or ('Portugal' in affiliation) or ('Hungary' in affiliation) or ('Czech' in affiliation) or ('Poland' in affiliation) or ('Slovenia' in affiliation) or ('Luxembourg' in affiliation) or ('Estonia' in affiliation) or ('Bratislava' in affiliation):
			country = 103
		#otherAsia: Korea, Taiwan
		if ('Korea' in affiliation) or ('Taiwan' in affiliation):
			country = 122
		#Middle East: Qatar, Arabia, UAE, Turkey, Egypt, Iran
		if ('Qatar' in affiliation) or ('Arabia' in affiliation) or ('UAE' in affiliation) or ('Turkey' in affiliation) or ('Egypt' in affiliation) or ('Iran' in affiliation):
			country = 123
		#other: New Zealand, Russia, Albany
		if ('New Zealand' in affiliation) or ('Russia' in affiliation) or ('Albany' in affiliation):
			country = 124

		years = int(parts[4])
		if years < 9:
			seniority = 4 #starting
		elif years < 13:
			seniority = 5 #junior
		elif years < 16:
			seniority = 6 #senior
		elif years < 22:
			seniority = 7 #highly senior
		else:
			seniority = 8 #confirmed

		pub_rate = float(parts[6])
		productivity = ''

		if (pub_rate > 0.18):
			if (pub_rate < 1.48):
				productivity = 9  #active
			elif pub_rate < 2.49:
				productivity = 10 #very active
			elif pub_rate < 3.72:
				productivity = 11 #productive
			elif pub_rate < 6.01:
				productivity = 12 #very productive
			else:
				productivity = 13 #prolific

		pub_num = int(parts[5])
		publications = ''

		if pub_num > 3:
			if pub_num < 15:
				publications = 14 #very few
			elif pub_num < 29:
				publications = 15 #few
			elif pub_num < 54:
				publications = 16 #fair
			elif pub_num < 108:
				publications = 17 #high
			else:
				publications = 18 #very high


		out = ''
		if country != '' and gender != '':
			for term in [gender,seniority,productivity,country]: #,publications,country]:
				if term != '':
					out += str(term) + " "
				
			if id_ in user_id:
				user_id[id_] += out
			else:
				user_id[id_] = out


with open("../csv/activities.csv") as f:

	for line in f:
		line = line.strip()
		parts = line.split(",")
		id_ = int(parts[0])
		if int(parts[1]) >= 30000:
			if id_ in user_id:
				user_id[id_] += parts[1] + " "
			#else:
			#	user_id[id_] = parts[1] + " "


keys = list(user_id.keys())
print('Number of users: ', len(keys))
with open("../csv/pmr.csv","w") as fout:
	for key in keys:
		fout.write(user_id[key]+"\n")

i = 0
with open("../csv/user_id_mapping.csv", "w") as fout:
	for key in keys:
		fout.write(str(key)+","+str(i)+"\n")
		i += 1
