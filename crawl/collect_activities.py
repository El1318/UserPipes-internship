import operator
import sys

confs = []
ignore_confs = []
all_kws = []

conf_codes = {}
kw_codes = {}
conf_cnt = 30000
kw_cnt = 20000


with open('../csv/conference_mapping.csv', 'r') as mapping:
    mapping.readline()
    for line in mapping:
        split_ = line.split(',')
        conf_codes[split_[1][:-1]] = int(split_[0])

with open('../csv/ignore_confs.csv', 'r') as mapping:
    mapping.readline()
    for line in mapping:
        ignore_confs.append(line[:-1])

ignore_confs = set(ignore_confs)

with open("../csv/publications.csv") as f, open("../csv/activities.csv","w") as fout_activities:
	f.readline()
	for line in f:
		line = line.strip()
		parts = line.split(",")
		conf = parts[2].strip()
		year = int(parts[3].strip())
		kws = parts[6].strip()
		author_id = parts[0]
		if year < 2015:
			continue
		if conf != "" and conf.isdigit() == False:
			#if conf not in confs:
			#	confs.append(conf)
			#	conf_codes[conf] = int(conf_cnt)
			#	fout_activities.write(author_id+","+str(conf_cnt)+"\n")
			#	conf_cnt += 1
			#else:
			#	fout_activities.write(author_id+","+str(conf_codes[conf])+"\n")

			if conf not in ignore_confs:
				confs.append(conf)
				fout_activities.write(author_id+","+str(conf_codes[conf])+"\n")

		kws_parts = kws.split(":")
		for kw in kws_parts:
			kw = kw.strip()
			if kw =="" or kw.isdigit() == True:
				continue
			if kw not in all_kws:
				all_kws.append(kw)
				kw_codes[kw]=int(kw_cnt)
				fout_activities.write(author_id+","+str(kw_cnt)+"\n")
				kw_cnt += 1
			else:
				fout_activities.write(author_id+","+str(kw_codes[kw])+"\n")
