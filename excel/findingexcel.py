import time
import openpyxl
wb = openpyxl.load_workbook('Final Consolidated RTE Requirements 29 June.xlsx')
sheets =  wb.get_sheet_names()
f1 = open("res_new.txt","w")
with open('res.txt') as f:
	for line in f:
		flag = 1
		for name in sheets:
			sheet = wb.get_sheet_by_name(name)
			for i in range(2,sheet.max_row+1):
				tar = 'C'+str(i)
				src = 'B'+str(i)
				try:
					if str(sheet[tar].value) in str(line):			
						sw = sheet[src].value
						flag = 0
						f1.write(sw+'\n')
				except:
					''
		if flag:
			f1.write(line)
