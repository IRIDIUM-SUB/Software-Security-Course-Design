from tkinter import *
from tkintertoolbox import *
import re#正则表达式相关
import os
import difflib
import platform
import time
import difflib
'''
原理:
1. 收集函数声明
2.建立函数调用链图
3. 比较
'''


class CFG(object):
	"""PART 2:CFG"""
	def __init__(self):


		self.root=Tk()
		self.tempfilepath=""
		self.samplefilepath=""
		self.toolbox=tkintertoolbox()
		self.root.title("CFG Dempstration")
		self.root.resizable(width=False, height=False)
		center_window(self.root,900,950)
		'''
		UI Layout
		'''
		top=Frame(self.root,borderwidth=2, relief="groove")
		topleft=Frame(top,borderwidth=2, relief="groove")
		topright=Frame(top,borderwidth=2, relief="groove")

		subleft=Frame(topleft)
		self.samplecode=Text(subleft,state='disabled',width=50,height=20)
		Scrollbar(subleft,command=self.samplecode.yview).pack(side='right',fill='y')
		self.samplecode.pack()
		
		ascleft=Frame(topleft)
		self.samplemap=Text(ascleft,state='disabled',width=50,height=20)
		Scrollbar(ascleft,command=self.samplemap.yview).pack(side='right',fill='y')
		self.samplemap.pack()

		botleft=Frame(topleft)
		self.samplepath=Label(botleft,borderwidth=2, relief="groove",width=30)
		Button(botleft,text="Select Sample file",command=self.getsampltfilename).pack(side='right',padx=10)
		self.samplepath.pack(side='left',fill='x',padx=10)



		subright=Frame(topright)
		self.tempcode=Text(subright,state='disabled',width=50,height=20)
		Scrollbar(subright,command=self.tempcode.yview).pack(side='right',fill='y')
		self.tempcode.pack()

		ascright=Frame(topright)
		self.tempmap=Text(ascright,state='disabled',width=50,height=20)
		Scrollbar(ascright,command=self.tempmap.yview).pack(side='right',fill='y')
		self.tempmap.pack()

		botright=Frame(topright)
		self.temppath=Label(botright,borderwidth=2, relief="groove",width=30)
		Button(botright,text="Select Template file",command=self.gettempfilename).pack(side='right',padx=10)
		self.temppath.pack(side='left',fill='x',padx=10)

		mid=Frame(self.root,borderwidth=2, relief="groove")
		Label(mid,text="Similarity rate%:\t").pack(side='left')
		self.rate=Label(mid,width=20,text="0.0")
		self.rate.pack(side='right')

		bot=Frame(self.root,borderwidth=2, relief="flat")
		Button(bot,text="Exit",command=self.root.destroy).pack(padx=10,side='right')
		Button(bot,text="Remove",command=self.cleanfile).pack(padx=10,side='right')
		Button(bot,text="Launch",command=self.deployanalysis).pack(padx=10,side='right')



		'''
		Deploy
		'''
		subleft.pack(pady=10)
		ascleft.pack(pady=10)
		botleft.pack(pady=10)
		topleft.pack(padx=10,side='left')
		
		subright.pack(pady=10)
		ascright.pack(pady=10)
		botright.pack(pady=10)
		topright.pack(padx=10,side='right')

		top.pack(pady=10,anchor="c")
		mid.pack(pady=10)
		bot.pack(pady=10,anchor="c")

		self.root.mainloop()

	def gettempfilename(self):
		self.tempfilepath=self.toolbox.fileselect()
		if self.tempfilepath != '':
			self.temppath.config(text=self.tempfilepath)
			tempfile=open(self.tempfilepath)
			if tempfile is not None:
				self.toolbox.textupdate(self.tempcode,tempfile.read())
				tempfile.close()
	def getsampltfilename(self):
		self.samplefilepath=self.toolbox.fileselect()
		if self.samplefilepath != '':
			self.samplepath.config(text=self.samplefilepath)
			sampfile=open(self.samplefilepath)
			if sampfile is not None:
				self.toolbox.textupdate(self.samplecode,sampfile.read())
				sampfile.close()
	def cleanfile(self):
		self.samplefilepath=""
		self.tempfilepath=""
		self.toolbox.textupdate(self.samplecode,"")
		self.toolbox.textupdate(self.tempcode,"")
		self.toolbox.textupdate(self.sampletoken,"")
		self.toolbox.textupdate(self.temptoken,"")
		self.rate.config(text="0.0")
		self.samplepath.config(text="")
		self.temppath.config(text="")

	def deployanalysis(self):
		frate=self.CFGmainprocess()
		if frate is not None:
			self.rate.config(text=str(frate*100))

	def CFGmainprocess(self):
		'''
		The main process of CFG. Return simliraity.
		'''

		'''
		Preparation Phase
		'''
		command=""
		self.sampletoken=""
		self.temptoken=""
		command="mkdir -p ../tool2/temp"
		os.system(command)#mkdir temp if not exist
		now=int(round(time.time()*1000))
		current_time=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(now/1000))#To name folder
		command="mkdir -p ../tool2/temp/"+current_time+"/"
		path="../tool2/temp/"+current_time+"/"
		os.system(command)# New a folder

		'''
		Dealing Sample file
		'''
		command="cp -i "+self.samplefilepath+" "+path+current_time+"sample.c"	#cp -i source target folder#Rename
		os.system(command)
		path=path+current_time+"sample.c"#Update path

		command="cflow -T  -m main -n "+path+" > "+path+"sample.txt"
		os.system(command)
		path=path+"sample.txt"
		samplefile=open(path,"r")
		if samplefile is not None:
			self.sampletoken=samplefile.read()
			self.sampletoken=re.sub(r'<[\s\S]*?>', '',self.sampletoken)
			self.toolbox.textupdate(self.samplemap,self.sampletoken)

		'''
		Dealing Temp file
		'''
		path="../tool2/temp/"+current_time+"/"#Initialization
		command="cp -i "+self.tempfilepath+" "+path+current_time+"temp.c"	#cp -i source target folder#Rename
		os.system(command)
		path=path+current_time+"temp.c"#Update path

		command="cflow -T -m main -n "+path+" > "+path+"temp.txt"
		os.system(command)
		path=path+"temp.txt"
		tempfile=open(path,"r")
		if tempfile is not None:
			self.temptoken=tempfile.read()
			self.temptoken=re.sub(r'<[\s\S]*?>', '',self.temptoken)# non-greddy mode
			self.toolbox.textupdate(self.tempmap,self.temptoken)

		'''
		Temporarily Comparison
		'''
		if self.sampletoken !="" and self.temptoken!= "":
			return difflib.SequenceMatcher(None, self.sampletoken,  self.temptoken).ratio()
		else:
			return 0

		

