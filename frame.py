from tkinter import *
import infowindow
class frame(object):
	def center_window(self,w, h):
		# 获取屏幕 宽、高
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		# 计算 x, y 位置
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
	def __init__(self):
		self.root=Tk()
		
		self.center_window(500, 350)
		self.root.title("Software Security")
		self.rfr=Frame(self.root,height = 20,width = 400)
		self.fr1=Frame(self.rfr)
		self.fr1.grid(row=0, column=0)
		self.fr2=Frame(self.rfr)
		self.fr2.grid(row=1, column=0)
		self.fr3=Frame(self.rfr)
		self.fr3.grid(row=2, column=0)
		self.br_comp=Button(self.fr1,text="源代码审计",state="disabled",width=16)
		self.br_cfg=Button(self.fr2,text="源代码审计-CFG",state="disabled",width=16)
		self.br_stack=Button(self.fr3,text="栈溢出检查",state="disabled",width=16)
		self.br_format=Button(self.fr1,text="格式化字符串",state="disabled",width=16)
		self.br_contA=Button(self.fr2,text="ContentA",state="disabled",width=16)
		self.br_contB=Button(self.fr3,text="ContentB",state="disabled",width=16)

		self.infofr=Frame(self.root)
		self.info=Button(self.infofr,text="Info",command=self.infodeploy,width=8)
		self.info.grid(row=0,column=0)
		self.exit=Button(self.infofr,text="Quit",command=self.root.destroy,width=8)
		self.exit.grid(row=0,column=1)

	def deploy(self):
		self.br_comp.pack(side="left")
		self.br_cfg.pack(side="left")
		self.br_stack.pack(side="left")
		self.br_format.pack(side="right")
		self.br_contA.pack(side="right")
		self.br_contB.pack(side="right")
		self.rfr.pack(pady=100)
		self.infofr.pack(side="right")

	def infodeploy(self):
		self.inf=infowindow.infowindow()
		self.inf.deploy()
	