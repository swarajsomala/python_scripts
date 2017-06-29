import re
import docx
#regex = r"\\[SWS_Rte_*\\]\\ \\|"
#regex = r"\[SWS_Rte|CONSTR_\d+\]\s\|"
#regex = r"\[[A-Z]{3,}_[A-Za-z]{3,6}|_\d+\]\s\|"
regex = r"\[\w+_\w|\W+_\d+\]\s\|"
doc = docx.Document('selection5.docx')
f = open('Res.txt',"w")
for para in doc.paragraphs:
	line = para.text
	if re.match(regex, line):
		str = line[line.index('[') : line.index(']')]
		print(str)
		f.write(str+'\n')