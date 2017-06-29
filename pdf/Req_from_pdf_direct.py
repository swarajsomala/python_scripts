import re
import time
import PyPDF2
pdfFileObj = open('RTE.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
f = open('Res.txt',"w")
for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	line = pageObj.extractText()
	try:
		print(line)
		s = re.search('SWS_Rte_',line)
		print(s.group())
		if 'SWS_Rte_' in line:
			print(line)
			print(line[line.index('W'):16])
		print('***************************************')
		print(line[line.index('SWS_Rte'):15])
		f.write(line)
	except:
			''