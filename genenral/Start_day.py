import os
import time
path = "E:\\Softwares\\"
directory = "C:\\Users\\"
softwares = ['Outlook 2016','Skype for Business 2016','eclipse']
try:
	for i in softwares:
		os.startfile(path+i)
	day = time.strftime("%d_%m")
	os.makedirs(directory+day)
except:
	print('')
