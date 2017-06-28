import openpyxl
wb = openpyxl.load_workbook('Amith.xlsx')
sheets =  wb.get_sheet_names()
name = 'MetaModel'
sheet = wb.get_sheet_by_name(name)
for i in range(2,51):
	tar = 'C'+str(i)
	src = 'D'+str(i)
	s = sheet[src].value
	if s.startswith('G'):
		sheet[tar] = 'AVIN_RTE_GP'+sheet[tar].value[8:]
	if s.startswith('C'):
		sheet[tar] = 'AVIN_RTE_CP'+sheet[tar].value[8:]
	print(sheet[tar].value)
wb.save('Amith.xlsx')
		
		