import re
import docx
import openpyxl
#regex = r"([[]+)SWS_Rte|CONSTR_(\d+)(/|)"
#regex = r"\\[SWS_Rte|CONSTR_*\\]\\|"
#regex = "[SWS_Rte_"
#regex1 = "[SWS_Rte_CONSTR_"
#regex = r"\\[SWS_Rte_*\\]\\ \\|"
doc = docx.Document('selection5.docx')
f = open('Res.txt',"w")
for para in doc.paragraphs:
	line = para.text
	#if re.match(regex, line):
	#print(regex in line)
	try:
		if (regex in line ) and '|' in line:
			str = line[line.index('[')+1:line.index(']')]
			#if not str in open('4_A.txt').read():
			print(str)
		#if line.startswith('[') and "|" in line:
		#str = line[1 : 15]
		#for word in line.split():
		#print(line)
		#if "[" in line and "|" in line :
		#	s = line[line.index("[")+1:line.index("]")]
		#s=line[1:line.index('|')]
			f.write(str+'\n')
	except:
		print('')