import re
import docx
import openpyxl
regex = re.compile(r'[SWS_Rte_(CONSTR_)_\d\d\d\d\d)]')
#regex = r"\\[SWS_Rte|CONSTR_*\\]\\|"
#regex = r"\\[SWS_Rte_*\\]\\ \\|"
doc = docx.Document('selection4.docx')
f = open('res.txt',"w")
for para in doc.paragraphs:
	line = para.text
	try:
			mo = regex.search(line)
			if mo:
				str = line[line.index('[')+1:line.index(']')]
				print(str)
				f.write(str+'\n')
	except:
		print('')