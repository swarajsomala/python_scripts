import win32com.client as wincl
import time
speak = wincl.Dispatch("SAPI.SpVoice")
with open('res.txt') as f:
	for line in f:
		speak.Speak(line)
		time.sleep(2)