import Bugdetectionuniversalframe
import re
import string
class intwidth(Bugdetectionuniversalframe.uniframe):
    def __init__(self):
        Bugdetectionuniversalframe.uniframe.__init__(self)
    def deploy(self):
        self.filesort(self)
        functionblocks=self.getfunctionblock()#Return a list#TODO:finish this function
        self.errorlist=[]
        for func in functionblocks:
            declaration=func.match(r"(((short |unsigned )?int)|short|long|char|float|double)\s*\** +[a-zA-Z1-9_0]+")#A list contains all declaraation
            declare={}#A dict{varible:type}
            assign=[]#[[left,right],...]
            for dec in declaration:#Sort
                    ty=dec.match(r"(((short |unsigned )?int)|short|long|char|float|double)\s*\**(?= )")[0]#A one-member list
                    var=dec.match(r"[a-zA-Z1-9_0]+")[0]# Same as above
                    '''
                    Assignmennt stage
                    '''
                    if ty=="long"or ty=="double":
                        length=8
                        elif ty=="float" or ty=="unsigned int"or ty=="int":
                            length=4
                            elif ty=="short int"or ty=="short":
                                length=2
                                elif ty=="char":
                                    length=1
                                    else:
                                        length=0
                    declare[var]=length
            Assignment=func.match(r"\**[a-zA-Z1-9_0]+\s*=\s*[a-zA-Z1-9_0]+;")#A list contains all Assignment
            for ass in Assignment:#Sort out
                left=ass.match(r"\**[a-zA-Z1-9_0]+(?=\s*=\s*[a-zA-Z1-9_0]+)")[0]
                right=ass.match(r"(?=\**[a-zA-Z1-9_0]+)\s*=\s*[a-zA-Z1-9_0]+")[0]
                assign.append([left,right])
            '''
            When Truncated happens:
            long/double->float/unsigned int/int->short int->char
            8->4->2->1
            '''
            for op in assign:
                leftvar=op[0]
                rightvar=op[1]
                if declare[leftvar]<declare[rightvar]:
                    self.errorlist.append(op)#Potential vulnerability occurred here.
            if self.errorlist is not None:




