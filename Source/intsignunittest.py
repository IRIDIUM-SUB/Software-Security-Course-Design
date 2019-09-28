
import re
import string
class intwidth():
    def __init__(self):
        self.path="intsigntest.c"
        self.scrtext="The following vulnerabilities may exist:\n"#显示文案
        self.decpattern=re.compile("((short int|unsigned int|int|short|long|char|float|double)\s*\** +([a-zA-Z1-9_0]+)(?=;))")
    def deploy(self):
        #self.filesort()
        
        if self.path != "":
            fp=open(self.path)#C
            self.code = fp.read()
            print (self.code)
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
                declaration=self.decpattern.findall(self.code)#A list contains all declaraation:[(all,type,var)]
                print(declaration)
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
                    print(triargs)
                    
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
                    print (twiargs)
                    
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
                print(self.scrtext)
            else:
                print("[ERROR] No code process\n")
        else:
            print("[ERROR] Invalid path\n")
    def getfunclist(self):  # 搜索所有的函数名称
        text=self.code
        namelist = []
        namelist_temp = []
        for line in text.splitlines():
            if line.find('(') == -1:
                continue
            i = 0
            while i < len(line):
                i = line.find('(', i)
                if i == -1:
                    break
                pos1 = line.rfind('(', 0, i)
                pos2 = line.rfind(' ', 0, i)
                if pos2 == i - 1:
                    pos2 = -1  # 对于if、while等系统函数，函数名和小括号之间有空格
                pos3 = line.rfind('\t', 0, i)
                pos4 = line.rfind('=', 0, i)
                pos5 = line.rfind('+', 0, i)
                pos6 = line.rfind('-', 0, i)
                pos7 = line.rfind('*', 0, i)
                pos8 = line.rfind('/', 0, i)
                pos = max(pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8)
                if re.search('[a-zA-Z_][a-zA-Z_0-9]*', line[pos + 1:i]) is not None:
                    namelist.append(line[pos + 1:i])
                i += 1
        for name in namelist:
            namelist_temp.append(name.strip())
        namelist = namelist_temp.copy()
        return list(set(namelist))
rcr=intwidth()
rcr.deploy()

'''
Test finished in 19/9/12
'''