import re,fileinput
import os
import sys
fp = open('13.arxml') # open file on read mode
#lines = fp.read().split("\n") # create a list containing all lines --->for removing new lines
lines = fp.read() #reads as it is
#print(lines)
fp.close() # close file
with open('13.arxml') as my_file:
	for i in my_file:
		testsite_array = my_file.readlines()
		#print(i)

walk_dir = "E:\\swaraj\\temp\\Rte_UnitTest"
new = "E:\\swaraj\\python\\files"
for path, dirs, files in os.walk(walk_dir):
	for dir in dirs:
		#print(path+"\\"+dir)
		directory = new+"\\"+dir
		if not os.path.exists(directory):
			os.makedirs(directory)
	for filename in files:
			fullpath = path.replace(walk_dir,new)
			fullpath=os.path.join(fullpath,filename)
			#s=open(fullpath, 'r').read().find('PORT')
			if not os.path.exists(fullpath):
				f = open(fullpath,'w')
			print(fullpath)
		
	
	
		