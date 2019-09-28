from tkinter import *
from tkintertoolbox import *
import  Homologous_detection
import  Bugdetectionuniversalframe
import CFG
import stack0verf10w
import formatstring
import intsign
import subcontent


class window(object):
	"""description of class"""
	def deploymainwindow(self):
		root=Tk()
		root.resizable(width=False, height=False)
		self.tktool=tkintertoolbox()
		center_window(root,500,300)
		root.title("SoftWare SEC")
		fr1=Frame(root)
		Button(fr1,text="源代码审计",command=self.deployHomologousDetection,width=16).grid(row=0,column=0)
		Button(fr1,text="源代码审计-CFG",command=self.deployCFG,width=16).grid(row=0,column=1)
		Button(fr1,text="栈溢出检查",command=self.deployoverflow,width=16).grid(row=0,column=2)
		Button(fr1,text="格式化字符串",command=self.deployformat,width=16).grid(row=1,column=0)
		Button(fr1,text="整数符号溢出(With Multiprocess)",command=self.deployintsign,width=16).grid(row=1,column=1)
		Button(fr1,text="DLC",command=self.deploydlc,width=16).grid(row=1,column=2)
		fr2=Frame(root)
		Button(fr2,text="Quit",command=root.destroy,width=8).pack(side='right',padx=10)
		Button(fr2,text="Info",command=self.deployinfowindow,width=8).pack(side='right',padx=10)
		fr3=Frame(root)
		Button(fr3,text="Empty pointer",width=8).pack(padx=5)
		Button(fr3,text="Empty pointer",width=8).pack(padx=5)
		fr1.pack(pady=10,anchor='center')
		fr2.pack(pady=10,anchor='center')
		root.mainloop()
	def deployinfowindow(self):
		root=Tk()
		root.title("Info")
		root.resizable(width=False, height=False)
		tkintertoolbox.center_window(root,300,200)
		textfr=Frame(root)
		Label(textfr,text="Designed by Iridium\nhttps://github.com/POTASSIUM7429\n19/8~19/9\n",borderwidth=3, relief="groove").pack(side='right')
		botfr=Frame(root)
		Button(botfr,text="Exit",command=root.destroy,width=8).pack()
		textfr.pack(pady=10)
		botfr.pack(pady=10)
		root.mainloop()

	def deployHomologousDetection(self):
		s1=Homologous_detection.Homologous_detection()

	def deployCFG(self):
		s2=CFG.CFG()

	def deployoverflow(self):
		s3=stack0verf10w.overflowdetection()
	def deployformat(self):
		s4=formatstring.formatdetection()
	def deployintsign(self):
		s5=intsign.intsign()
	def deploydlc(self):
		
		s6=subcontent.subwindow()
		s6.pool.close()
		s6.pool.join()


