##############Copying Files and Folders####################
import shutil, os
os.chdir('E:\\')
shutil.copy('E:\\spam.txt', 'E:\\temp')  			##copy spam file to temp folder
shutil.copy('E:\\spam.txt', 'E:\\temp\\spam2.txt')	##copy spam file to temp folder as spam2.txt(we have to cccreate both the files before copying)
#shutil.copy('E:\\temp', 'E:\\temp2')	##copy spam file to temp folder as spam2.txt(we have to cccreate both the files before copying)


