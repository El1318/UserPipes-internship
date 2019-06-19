f = open("../csv/groups.csv")
fout = open("../csv/groups_out.csv","w")
for line in f:
	new_line = line.replace(")\n", ")")
	fout.write(new_line)
f.close()
fout.close()