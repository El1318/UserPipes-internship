author_list = []
author_count = {}

fout = open("../csv/authors_unique.csv","w")

f = open("../csv/authors.csv")
for line in f:
	line = line.strip()
	parts = line.split(",")
	author_name = parts[0]
	author_link = parts[1]
	identifer = author_name+", "+author_link
	if identifer in author_list:
		author_count[identifer] += 1
	else:
		author_list.append(identifer)
		author_count[identifer] = 1

# print header
fout.write("author_code,author_name,dblp_link,count\n")

# cnt = 0
author_universal_code = 1000
for author in author_list:
	# cnt += 1
	# if cnt % 1000 == 0:
	# 	print "done with",cnt,"authors ..."
	if author_count[author] > 1:
		out_line = str(author_universal_code)+", "+author +", "+str(author_count[author])+"\n"
		author_universal_code += 1
		fout.write(out_line)