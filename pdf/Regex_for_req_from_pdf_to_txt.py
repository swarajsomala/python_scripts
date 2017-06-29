import re
shakes = open("selection7.txt","r")
regex = r"([[]+)SWS_Rte|CONSTR_(\d+)(]+)"
#regex = '\\[SWS_Rte|CONSTR_(\d+)\\]\\ $\\|'
#regex = "^[SWS_.*]\\|$"
#regex=r'\\[SWS_Rte|CONSTR_(\d+)\\]\w\|'
for line in shakes:
    if re.match(regex, line):
        #print(line.split(None, 1)[0])
        s=line[1:line.index(']')]
        #s1=open('out.txt',"r")
        #for s in s1:
         #   if s in str:
        if s not in open('out.txt').read():
            print(s)
        
	    
