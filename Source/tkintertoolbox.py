
from tkinter import *
from tkinter import filedialog

class tkintertoolbox(object):

	def textupdate(self,textbox,newtext):
		"""
		textbox is a disabled Text obj
		"""
		textbox.config(state=NORMAL)
		#textbox.delete(1.0, END)
		textbox.insert(1.0, newtext)
		textbox.config(state=DISABLED)

	def fileselect(self):
		filename = filedialog.askopenfilename(filetypes = [(".c", "*.c"), (".cpp", "*.cpp")] )
		return filename

	def folderselect(self):
		return filedialog.askdirectory()
	def scrcls(self,textbox,):
		textbox.config(state=NORMAL)
		textbox.delete(1.0, END)
		#textbox.insert(1.0, newtext)
		textbox.config(state=DISABLED)

def center_window(window,w, h):
	# 获取屏幕 宽、高
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	# 计算 x, y 位置
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)		
	window.geometry('%dx%d+%d+%d' % (w, h, x, y))



