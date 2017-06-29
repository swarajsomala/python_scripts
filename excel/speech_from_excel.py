import win32com.client as wincl
import time
import openpyxl
speak = wincl.Dispatch("SAPI.SpVoice")
wb = openpyxl.load_workbook('Copy of Final Consolidated RTE Requirements21June.xlsx')
sheets =  wb.get_sheet_names()
f = open("res.txt","w")
for name in sheets:
	sheet = wb.get_sheet_by_name(name)
	flag = 1
	for i in range(2,sheet.max_row+1):
		tar = 'C'+str(i)
		src = 'D'+str(i)
		name1 = 'B'+str(i)
		s = sheet[src].value
		if s!= None and s.startswith('C'):			
			if flag:
				speak.Speak(name)
				f.write(name + '\n')
				time.sleep(1)
				flag = 0
			sw = sheet[tar].value[16:]
			sw1 = sheet[name1].value[8:]
			speak.Speak(sw+' '+sw1)
			time.sleep(2)
			f.write(sw+' '+sw1+'\n')
	time.sleep(2)
                       