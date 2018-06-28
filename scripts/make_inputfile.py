import os
root = "../raw_data/"

allinputs = []
onlytwo = False #only use two features and two Persons

for folder in os.listdir(root):
	for subfolder in os.listdir(os.path.join(root,folder)):
		for file in os.listdir(os.path.join(root,folder,subfolder)):
			if file == "output.txt": # and "1" in subfolder:
				with open(os.path.join(root,folder,subfolder,file)) as infile:
					for line in infile:
						allinputs.append(line)

i = 0
with open("../proc_data/data","w") as outfile:
	for line in allinputs:
		if not "feature" in line:
			if not onlytwo:
				outfile.write(line)
			elif ("p007" in line or "p008" in line or "p009" in line or "p001" in line) and (i%16==0 or i%16==1):
				outfile.write(line)
			i+=1