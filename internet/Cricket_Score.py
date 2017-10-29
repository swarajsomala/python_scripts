from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import *
import time,os
new_score = ""
while True:
    a = urlopen("http://www.cricbuzz.com/live-cricket-scores/18958/ind-vs-nz-3rd-odi-new-zealand-tour-of-india-2017")
    bsobj=BeautifulSoup(a,"lxml")
    temp=bsobj.find("div",{"class":"cb-min-bat-rw" })
    temp = temp.find("span",{"class":"cb-font-20 text-bold"})
    old_score = str(temp)[36:56]
    if old_score != new_score:
        root = Tk()
        root.geometry('400x400')
        frame = Frame(root)
        frame.pack()
        w = Label(root, text = old_score, font = ('Comic Sans MS',18),bg = 'green', fg = 'black')
        #spe = "say '"+old_score+"'"
        #print(spe)
        #os.system(spe)
        new_score = old_score
        w.pack()
        root.after(2000, lambda: root.destroy())
        root.mainloop()
        time.sleep(10)