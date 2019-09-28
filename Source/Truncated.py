import Bugdetectionuniversalframe
import os
import re


class inttruncationdetection(Bugdetectionuniversalframe.uniframe):
    def __init__(self):
        Bugdetectionuniversalframe.uniframe.__init__(self)



    def deploy(self):#Re-write deploy method
        flag=0
        self.filesort()
        if self.path != "":
            command=" splint +weak -hints -varuse +posixlib "+self.path
            os.system(command)
            r= os.popen(command)
            textlist=r.readlines()
            final=""
            for text in textlist:
            #print(text) # 打印cmd输出结果

                if re.search(r"Assignment",text):
                    final=final+text
                    flag=1
            if flag:
                final=final+"\n Looks like there is a truncated vulnerability."
            else:
                final="Seems no truncated vulnerability."
            self.toolbox.textupdate(self.tokentext,final)

