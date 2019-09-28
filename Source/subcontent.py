from tkinter import *
import tkintertoolbox

import heapovf
import Truncated
import emptypointer

class subwindow(object):
    def __init__(self):
        root=Tk()
        root.title=("DLC Content")
        root.resizable(width=False, height=False)
        self.tktool=tkintertoolbox.tkintertoolbox()
        tkintertoolbox.center_window(root,300,400)
        buttonfr=Frame(root)
        Button(buttonfr,text="Heap Overflow",command=self.deployheap,width=16).pack(pady=5)
        Button(buttonfr,text="INT Width",command=self.deploytruncated,width=16).pack(pady=5)
        Button(buttonfr,text="Null Pointer",command=self.deployemptypointer,width=16).pack(pady=5)

        bot=Frame(root)
        Button(bot,text="Exit",command=root.destroy).pack(side="right")

        buttonfr.pack(pady=10)
        bot.pack()
        root.mainloop()
    def deployheap(self):
        e1=heapovf.heapdetection()
    def deploytruncated(self):
        e2=Truncated.inttruncationdetection()
    def deployemptypointer(self):
        e3=emptypointer.nulldetection()
