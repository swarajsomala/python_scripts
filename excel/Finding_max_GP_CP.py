import openpyxl
wb = openpyxl.load_workbook('Final Consolidated RTE Requirements 22 June.xlsx')
sheets =  wb.get_sheet_names()
f = open("res.txt","w")
for name in sheets:
	sheet = wb.get_sheet_by_name(name)
	for i in range(2,sheet.max_row+1):
		tar = 'C'+str(i)
		s= sheet[tar].value
		if s!= None and ('CP' in s):						
				f.write(s + '\n')
