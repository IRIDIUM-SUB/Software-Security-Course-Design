from tkinter import *
from tkintertoolbox import *
import time
import os
class  uniframe(object):
    def __init__(self):
        root=Tk()
        self.path=""
        self.toolbox=tkintertoolbox()

        #self.toolbox.center_window(root,900,600)
        center_window(root,700,900)
        root.resizable(width=False, height=False)
        root.title("Overflow")
        self.text=Frame(root,borderwidth=2, relief="groove")
        self.bot=Frame(root,borderwidth=2, relief="flat")

        self.codefr=Frame(self.text)
        self.tokenfr=Frame(self.text)

        self.codetext=Text(self.codefr,state='disabled',width=80,height=20)
        self.tokentext=Text(self.tokenfr,state='disabled',width=80,height=20)

        self.codescr=Scrollbar(self.codefr)
        self.tokenscr=Scrollbar(self.tokenfr)

        self.codescr.config(command=self.codetext.yview)
        self.tokenscr.config(command=self.tokentext.yview)

        self.codescr.pack(side='right',fill='y')
        self.tokenscr.pack(side='right',fill='y')

        self.codetext.pack(padx=10,pady=10)
        self.tokentext.pack(padx=10,pady=10)

        self.mid=Frame(root,borderwidth=2, relief="groove")
        self.codepath=Label(self.mid,text="",borderwidth=2, relief="groove",width=30)

        Button(self.bot,text="Select file",command=self.getfilename).pack(padx=5,side='left')
        self.launch=Button(self.bot,text="Launch",command=self.deploy)
        self.launch.pack(padx=5,side='left')
        Button(self.bot,text="Remove",command=self.cleanfile).pack(padx=5,side='left')
        Button(self.bot,text="Exit",command=root.destroy).pack(padx=5,side='left')

        self.codefr.pack()
        self.tokenfr.pack()

        self.text.pack(pady=10)
        self.mid.pack(pady=10)
        self.bot.pack(pady=10)
        root.mainloop()

    def cleanfile(self):
	    self.path=""
	    self.toolbox.scrcls(self.codetext)
	    self.toolbox.scrcls(self.tokentext)
	    self.codepath.config(text="")
    def getfilename(self):

        temp=self.toolbox.fileselect()
        if temp is not None:
            self.path=temp
        self.codepath.config(text=self.path)
        if self.path is not None:
            fi=open(self.path)
            if fi is not None:
                self.toolbox.textupdate(self.codetext,fi.read())

                fi.close()
    def deploy(self):
        kksk=1
    def filesort(self):
        if self.path !="":
            os.system("mkdir -p ../tool3")
            os.system("mkdir -p ../tool3/temp")
            now=int(round(time.time()*1000))
            current_time=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(now/1000))#To name file
            command="cp -i "+self.path+" ../tool3/temp/"+current_time+".c"
            os.system(command)
            self.path="../tool3/temp/"+current_time+".c"

