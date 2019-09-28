import Bugdetectionuniversalframe
import os
import re
class overflowdetection(Bugdetectionuniversalframe.uniframe):
    def __init__(self):
        Bugdetectionuniversalframe.uniframe.__init__(self)



    def deploy(self):#Re-write deploy method
        flag=0
        self.filesort()
        if self.path != "":
            command=" splint +weak +bounds -hints -varuse +posixlib "+self.path
            os.system(command)
            r= os.popen(command)
            textlist=r.readlines()
            final=""
            for text in textlist:
            #print(text) # 打印cmd输出结果
                final=final+text
                if re.search(r"out-of-bounds|buffer overflow",text):

                    flag=1
            if flag:
                final=final+"\n Looks like there is a stack overflow vulnerability."
            else:
                final="Seems no overflow  vulnerability."
            self.toolbox.textupdate(self.tokentext,final)

