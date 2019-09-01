
from tkinter import *
import tkinter.filedialog
class fileselect(object,aim):
	def __init__(self,aim):
		self.aim=aim
	def fileselect(self):
		filename = tkinter.filedialog.askopenfilename(title=self.aim,filetypes=[(".c", "*.c")])
		return filename
		


