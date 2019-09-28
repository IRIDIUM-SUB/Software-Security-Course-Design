import Bugdetectionuniversalframe
import re
from tkinter import *
from tkintertoolbox import *
import time
import os
import string
import multiprocessing
class intsign():
    def __init__(self):
        root=Tk()
        self.path=""
        self.paths=[]
        self.dicpath=""
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
        Button(self.bot,text="Select Folder with multiprocess",command=self.getfoldername).pack(padx=5,side='left')
        self.launch=Button(self.bot,text="Launch",command=self.multiproxy)
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
	    self.path= ""
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
    def getfoldername(self):
        self.dicpath=self.toolbox.folderselect()
        if self.dicpath is not None:
            self.codepath.config(text=self.dicpath)
            filenames=os.listdir(self.dicpath)
            self.toolbox.textupdate(self.codetext,self.dicpath+"\n"+("\n".join(filenames)))
            self.paths=filenames#Now path is a list
    def multiproxy(self):

        if self.path !="":#Single file
            self.deploy()
        elif self.paths !=[]:
            res=[]
            cpus = multiprocessing.cpu_count()
            print("CPUS=",cpus)
            pool = multiprocessing.Pool(processes = 3)
            print("Pool set up")
            for filename in self.paths:
                
                self.oops=self.dicpath+"/"+filename#is full path
                print(self.oops)
                mul=multi(self.oops)
                time.sleep(2)#Avoid Name confliction
                pool.apply_async(res.append(mul.deploy4multi()),())
            
                #Bug see https://segmentfault.com/q/1010000007250090
            pool.close()
            pool.join()
            print("".join(res))
            self.toolbox.textupdate(self.tokentext,"\n".join(res))
            print("EXit")
            


        
    def deploy(self):
        self.filesort()
        self.pattern=re.compile("((short int|unsigned int|int|short|long|char|float|double)\s*\** +([a-zA-Z1-9_0]+)(?=;))")
        #self.path="intsigntest.c"
        self.scrtext="The following vulnerabilities may exist:\n"#显示文案

        if self.path != "":
            fp=open(self.path)#C
            self.code = fp.read()
            #print (self.code)
            if self.code is not None:
                #self.code=re.sub(r'((?<=\n)|^)[ \t]*\/\*.*?\*\/\n?|\/\*.*?\*\/|((?<=\n)|^)[ \t]*\/\/[^\n]*\n|\/\/[^\n]*','', self.code)
                '''
                Elimate comments
                '''
                #self.code=re.sub(r'#[\s\S]*\n','',self.code)
                '''
                Ignore include/define
                '''
                #print (self.code)
                #self.funclist=self.getfunclist()#Finish the method
                #print(self.funclist)
                declaration=self.pattern.findall(self.code)#A list contains all declaraation:[(all,type,var)]
                #print(declaration)
                declare={}#A dict{varible:type}
                assign=[]#[[left,right],...]
                
                
                for dec in declaration:#Sort
                    ty=dec[1]
                    var=dec[2]
                    '''
                    Assignmennt stage
                    '''
                    declare[var]=ty
                triargs=re.findall(r"(strncat|strncpy|memcpy) *\(([\*a-zA-Z1-9_0]*\s*),([\*a-zA-Z1-9_0]*\s*),([\*a-zA-Z1-9_0]*\s*)\)",self.code)#Automatic parameter resolution
                twiargs=re.findall(r"(strcpy|strcat) *\(([\*a-zA-Z1-9_0]*\s*),([\*a-zA-Z1-9_0]*\s*)\)",self.code)
                if triargs is not None:#sub:('strncat', 'kksk', 'pdse', 'rous')
                    #print(triargs)
                    
                    for sub in triargs:
                        strlist=[]
                        strlist.append(sub[1])
                        strlist.append(sub[2])
                        strlist.append(sub[3])
                        #Now strlist should have 3 members
                        if declare[strlist[2]] !='unsigned' and declare[strlist[2]] !='unsigned int':
                            """
                            Error occurred
                            """
                            
                            self.scrtext=self.scrtext+"Error occurred in "+sub[0]+"->"+",".join(strlist)+"\n"
                if twiargs is not None:
                    #print (twiargs)
                    
                    for sub in twiargs:#sub:('strncat',  'pdse', 'rous')
                        strlist=[]
                        strlist.append(sub[1])
                        strlist.append(sub[2])
                        #Now strlist should have 2 members
                        if declare[strlist[1]] !='unsigned' and declare[strlist[1]] !='unsigned int':
                            """
                            Error occurred
                            """
                            self.scrtext=self.scrtext+"Error occurred in "+sub[0]+"->"+",".join(strlist)+"\n" 
                if self.scrtext=="The following vulnerabilities may exist:\n":
                    self.scrtext= self.scrtext+"None\n"
                self.toolbox.textupdate(self.tokentext,self.scrtext)
            else:
                self.toolbox.textupdate(self.tokentext,"[ERROR] No code process\n")
        else:
            self.toolbox.textupdate(self.tokentext,"[ERROR] Invalid path\n")
        self.path=""#Reset
    def filesort(self):
        if self.path !="":
            os.system("mkdir -p ../tool3")
            os.system("mkdir -p ../tool3/temp")
            now=int(round(time.time()*1000))
            current_time=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(now/1000))#To name file
            command="cp -i "+self.path+" ../tool3/temp/"+current_time+".c"
            os.system(command)
            self.path="../tool3/temp/"+current_time+".c"




class multi():
    def __init__(self,oops):
        self.oops=oops
        self.toolbox=tkintertoolbox()
    def deploy4multi(self):
        
        self.filesort4multi()
        print(self.ooops)
        self.pattern=re.compile("((short int|unsigned int|int|short|long|char|float|double)\s*\** +([a-zA-Z1-9_0]+)(?=;))")
        #self.path="intsigntest.c"
        self.scrtext="The following vulnerabilities may exist:\n"#显示文案

        if self.ooops != "":#ooops is redirected full path
            fp=open(self.ooops)#C
            self.code = fp.read()
            #print (self.code)
            if self.code is not None:
                #self.code=re.sub(r'((?<=\n)|^)[ \t]*\/\*.*?\*\/\n?|\/\*.*?\*\/|((?<=\n)|^)[ \t]*\/\/[^\n]*\n|\/\/[^\n]*','', self.code)
                '''
                Elimate comments
                '''
                #self.code=re.sub(r'#[\s\S]*\n','',self.code)
                '''
                Ignore include/define
                '''
                #print (self.code)
                #self.funclist=self.getfunclist()#Finish the method
                #print(self.funclist)
                declaration=self.pattern.findall(self.code)#A list contains all declaraation:[(all,type,var)]
                #print(declaration)
                declare={}#A dict{varible:type}
                assign=[]#[[left,right],...]
                
                
                for dec in declaration:#Sort
                    ty=dec[1]
                    var=dec[2]
                    '''
                    Assignmennt stage
                    '''
                    declare[var]=ty
                triargs=re.findall(r"(strncat|strncpy|memcpy) *\(([\*a-zA-Z1-9_0]*\s*),([\*a-zA-Z1-9_0]*\s*),([\*a-zA-Z1-9_0]*\s*)\)",self.code)#Automatic parameter resolution
                twiargs=re.findall(r"(strcpy|strcat) *\(([\*a-zA-Z1-9_0]*\s*),([\*a-zA-Z1-9_0]*\s*)\)",self.code)
                if triargs is not None:#sub:('strncat', 'kksk', 'pdse', 'rous')
                    #print(triargs)
                    
                    for sub in triargs:
                        strlist=[]
                        strlist.append(sub[1])
                        strlist.append(sub[2])
                        strlist.append(sub[3])
                        #Now strlist should have 3 members
                        if declare[strlist[2]] !='unsigned' and declare[strlist[2]] !='unsigned int':
                            """
                            Error occurred
                            """
                            
                            self.scrtext=self.scrtext+"Error occurred in "+self.oops+"\t"+sub[0]+"->"+",".join(strlist)+"\n"
                if twiargs is not None:
                    #print (twiargs)
                    
                    for sub in twiargs:#sub:('strncat',  'pdse', 'rous')
                        strlist=[]
                        strlist.append(sub[1])
                        strlist.append(sub[2])
                        #Now strlist should have 2 members
                        if declare[strlist[1]] !='unsigned' and declare[strlist[1]] !='unsigned int':
                            """
                            Error occurred
                            """
                            self.scrtext=self.scrtext+"Error occurred in "+self.oops+"\t"+sub[0]+"->"+",".join(strlist)+"\n" 
                if self.scrtext=="The following vulnerabilities may exist:\n":
                    self.scrtext= self.oops+":\n"+self.scrtext+"None\n"
                    return self.scrtext
                else:
                    self.scrtext= self.oops+":\n"+self.scrtext
                    return self.scrtext
                #self.toolbox.textupdate(self.tokentext,self.scrtext)
            else:
                return self.scrtext
                #self.toolbox.textupdate(self.tokentext,"[ERROR] No code process\n")
        else:
            return "[ERROR] Invalid path\n"
            #self.toolbox.textupdate(self.tokentext,"[ERROR] Invalid path\n")
    def filesort4multi(self):
        if self.oops !="":
            os.system("mkdir -p ../tool4")
            os.system("mkdir -p ../tool4/temp")
            
            now=int(round(time.time()*1000))
            current_time=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(now/1000))#To name file
            command="cp -i "+self.oops+" ../tool4/temp/"+current_time+".c"
            os.system(command)
            self.ooops="../tool4/temp/"+current_time+".c"