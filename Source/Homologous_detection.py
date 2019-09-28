from tkinter import *
from tkintertoolbox import *
import re#正则表达式相关
import os
import difflib
import platform

class Homologous_detection(object):
	"""description of class"""
	def __init__(self):
		self.blank=1
		'''
		global var
		'''
		self.tempfilepath=""
		self.samplefilepath=""

		'''
		class prepare
		'''
		self.toolbox=tkintertoolbox()

		'''
		GUI Setting
		'''

		self.root=Tk()
		self.root.title("Homologous detection")
		self.root.resizable(width=False, height=False)
		center_window(self.root,900,950)
		self.topfr1=Frame(self.root,borderwidth=2, relief="groove")

		self.subfr1=Frame(self.topfr1)

		self.botfr1=Frame(self.subfr1)
		self.tempcdscr=Scrollbar(self.botfr1)
		self.tempcdscr.pack(side='right',fill='y')
		self.tempcode=Text(self.botfr1,state='disabled',width=50,height=20)
		#tkintertoolbox.textupdate(self.tempcode,"1")#TEST ONLY
		self.tempcode.pack()
		self.tempcdscr.config(command=self.tempcode.yview)
		

		self.botfr2=Frame(self.subfr1)
		self.temptokscr=Scrollbar(self.botfr2)
		self.temptokscr.pack(side='right',fill='y')
		self.temptok=Text(self.botfr2,state='disabled',width=50,height=20)
		#tkintertoolbox.textupdate(self.temptok,"2")#TEST ONLY
		self.temptok.pack()
		self.temptokscr.config(command=self.temptok.yview)

		self.botfr3=Frame(self.subfr1)
		Button(self.botfr3,text="Select template file",command=self.gettempfilename).pack(side='right',padx=10)
		self.temppath=Label(self.botfr3,borderwidth=2, relief="groove",width=30,text=self.tempfilepath)
		self.temppath.pack(side='left',fill='x',padx=10)
		
		self.subfr2=Frame(self.topfr1)

		self.botfr4=Frame(self.subfr2)
		self.sampcdscr=Scrollbar(self.botfr4)
		self.sampcdscr.pack(side='right',fill='y')
		self.sampcode=Text(self.botfr4,state='disabled',width=50,height=20)
		#tkintertoolbox.textupdate(self.sampcode,"3")#TEST ONLY
		self.sampcode.pack()
		self.sampcdscr.config(command=self.sampcode.yview)
		


		self.botfr5=Frame(self.subfr2)
		self.samptokscr=Scrollbar(self.botfr5)
		self.samptokscr.pack(side='right',fill='y')
		self.samptok=Text(self.botfr5,state='disabled',width=50,height=20)
		#tkintertoolbox.textupdate(self.samptok,"4")#TEST ONLY
		self.samptok.pack()
		self.samptokscr.config(command=self.samptok.yview)
		

		self.botfr6=Frame(self.subfr2)
		Button(self.botfr6,text="Select sample file",command=self.getsamplefilename).pack(side='right',padx=10)
		self.samppath=Label(self.botfr6,borderwidth=2, relief="groove",width=30,text=self.samplefilepath)
		self.samppath.pack(side='left',fill='x',padx=10)

		self.topfr2=Frame(self.root,borderwidth=2, relief="flat")
		Button(self.topfr2,text="Exit",command=self.root.destroy).pack(padx=10,side='right')
		Button(self.topfr2,text="Remove",command=self.cleanfile).pack(padx=10,side='right')
		Button(self.topfr2,text="Launch",command=self.mainprocess).pack(padx=10,side='right')
		
		self.superfr=Frame(self.root,borderwidth=2, relief="groove")
		Label(self.superfr,text="Similarity rate%:\t").pack(side='left')
		self.persentage=Label(self.superfr,width=30,text="0.0")
		self.persentage.pack(side='right')
		'''
		Deploy
		'''
		self.botfr1.pack(pady=20)
		self.botfr2.pack(pady=20)
		self.botfr3.pack(pady=10)
		self.subfr1.pack(side='left')
		self.botfr4.pack(pady=20)
		self.botfr5.pack(pady=20)
		self.botfr6.pack(pady=10)
		self.subfr2.pack(side='right')

		self.topfr1.pack(pady=10)
		self.superfr.pack(pady=10)
		self.topfr2.pack(pady=10)
		self.root.mainloop()
		
	def getsamplefilename(self):
		self.samplefilepath=self.toolbox.fileselect()
		self.samppath.config(text=self.samplefilepath)
		sampfile=open(self.samplefilepath)
		if sampfile is not None:
			self.toolbox.textupdate(self.sampcode,sampfile.read())
			sampfile.close()

	def gettempfilename(self):
		self.tempfilepath=self.toolbox.fileselect()
		self.temppath.config(text=self.tempfilepath)
		tempfile=open(self.tempfilepath)
		if tempfile is not None:
			self.toolbox.textupdate(self.tempcode,tempfile.read())
			tempfile.close()

	def cleanfile(self):
		self.samplefilepath=""
		self.tempfilepath=""
		self.toolbox.textupdate(self.sampcode,"")
		self.toolbox.textupdate(self.tempcode,"")
		self.toolbox.textupdate(self.samptok,"")
		self.toolbox.textupdate(self.temptok,"")
		self.persentage.config(text="0.0")
		self.samppath.config(text="")
		self.temppath.config(text="")



	'''
	TODO:Adaption
	'''
	def mainprocess(self):

		'''
		Check files' existance

		'''
		print(self.samplefilepath,self.tempfilepath)
		if self.samplefilepath!="" and self.tempfilepath!="":
			'''
			开始处理模板文件
			'''

			sysstr = platform.system()
			if sysstr =="Windows":
				'''
				test part
				'''
				temp=Source_code_processing(self.tempfilepath)
				sample=Source_code_processing(self.samplefilepath)
			else:

				temp=tokendealing(self.samplefilepath)#temp is final token
				#print(temp)
				sample=tokendealing(self.tempfilepath)#sample is final token
				#print(sample)
			"""
			Print Screen
			"""
			self.toolbox.textupdate(self.temptok,temp)
			self.toolbox.textupdate(self.samptok,sample)
			#Comparasion see https://blog.csdn.net/qq_41020281/article/details/82194992 ,Use difflib 
			Similarityrate=difflib.SequenceMatcher(None, temp, sample).ratio() 
			self.persentage.config(text=str(Similarityrate*100))
def Source_code_processing(filename):
	
	#C_Rule = "(///*(/s|.)*?/*//)|(////.*)"
	fi=open(filename,mode='r')
	source=fi.read()
	str=source
	fi.close()
	str = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"\n" ,str) # remove all occurance streamed comments (/*COMMENT */) from string WITH \n
	str = re.sub(re.compile("//.*?\n" ) ,"\n" ,str) # remove all occurance singleline comments (//COMMENT\n ) from string
	str = re.sub(re.compile("\n+\n" ) ,"\n" ,str)#sort out
	return str
	
def tokendealing(filename):

	base=Source_code_processing(filename)
	mid=open('../tool1/temp.c','w+')
	mid.write(base)
	mid.close()
	#os.system("../tool1/a.out<../tool1/temp.c")
	r= os.popen("../tool1/a.out<../tool1/temp.c")
	textlist =r.readlines()
	final=""
	for text in textlist:
		#print(text) # 打印cmd输出结果
		final=final+text
	return final
	'''
	ToDo: Sort the ducument structure
	'''
