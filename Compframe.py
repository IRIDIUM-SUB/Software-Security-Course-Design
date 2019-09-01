from tkinter import *

class Compframe(object):
	def __init__(self):
		self.tkframe=Tk()
		self.tkframe.title("Code Compare")
		self.fr1=Frame(self.tkframe)#Left,Template
		self.fr2=Frame(self.tkframe)#Right,Sample
		self.selecttemp=Button(self.fr1,text="Select template file")
		self.selectsample=Button(self.fr2,text="Select Sample file")
		self.fr10=Frame(self.fr1)
		self.fr11=Frame(self.fr1)
		self.fr20=Frame(self.fr2)
		self.fr21=Frame(self.fr2)
		
		self.tempcode=Text(self.fr10, height=2, width=30)
		self.tempcodescroll= Scrollbar(self.fr10)
		self.tempcodescroll.config(command=self.tempcode.yview)
		self.temptoken=Text(self.fr11)
		self.temptokenscroll=Scrollbar(self.fr11)
		self.temptokenscroll.config(command=self.temptoken.yview)

		self.samplecode=Text(self.fr20)
		self.samplecodescroll= Scrollbar(self.fr20)
		self.samplecodescroll.config(command=self.samplecode.yview)
		self.sampletoken=Text(self.fr21)
		self.sampletokenscroll=Scrollbar(self.fr21)
		self.sampletokenscroll.config(command=self.sampletoken.yview)

		self.botfr=Frame(self.tkframe)
		self.launch=Button(self.botfr,text="Launch Analysis")
		self.clear=Button(self.botfr,text="Clean Files")
		self.percentage=Label(self.botfr)
		self.exit=Button(self.botfr,text="EXIT",command=self.tkframe.destroy)
	def deploy(self):
		self.tempcode.pack(side='left')
		self.tempcodescroll.pack(side="right")
		self.temptoken.pack(side='left')
		self.temptokenscroll.pack(side="right")
		self.fr10.grid(row=0,column=0)
		self.fr11.grid(row=1,column=0)
		self.fr1.pack(side='left')

		self.samplecode.pack(side='left')
		self.samplecodescroll.pack(side="right")
		self.sampletoken.pack(side='left')
		self.sampletokenscroll.pack(side="right")
		self.fr20.grid(row=0,column=0)
		self.fr21.grid(row=1,column=0)
		self.fr2.pack(side='right')

		self.launch.grid(row=0,column=0)
		self.clear.grid(row=0,column=1)
		self.exit.grid(row=0,column=2)
		self.percentage.grid(row=0,column=3)
		self.botfr.pack(side='bottom')
		self.tkframe.mainloop()
