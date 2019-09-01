from tkinter import *
class infowindow(object):
	def __init__(self):
		self.inw=Tk()
		self.inw.title("Info")
		self.inw.geometry("250x200")
		self.textfr=Frame(self.inw)
		self.botfr=Frame(self.inw)
		#self.img_bit = PhotoImage(file = 'cbhd4-e5gcb.gif')
		#self.imagefr=Frame(self.inw)
		self.text=Label(self.textfr,text="Designed by IRIDIUM\n19/8~19/9\nReserved")
		#self.img=Label(self.imagefr,image=self.img_bit)
		#self.text.grid(row=0, column=0)
		self.exit=Button(self.botfr,text="Exit",command=self.inw.destroy,width=8)
		#self.exit.grid(row=0, column=0)

	def deploy(self):
		#self.imagefr.pack(side="left")
		self.text.pack()
		self.textfr.pack()
		self.exit.pack()
		self.botfr.pack(side="bottom")
		self.inw.mainloop()