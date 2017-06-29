import re
shakes = open("selection6.txt","r")
regex = r"([[]+)SWS_Rte|CONSTR_(\d+)(/|$)"
for line in shakes:
    if re.match(regex, line):
        #print(line.split(None, 1)[0])
        s=line[1:line.index(']')]
        baconFile = open('bacon.txt', 'w')
		baconFile.write('Hello world!\n')
		baconFile.close()

        
