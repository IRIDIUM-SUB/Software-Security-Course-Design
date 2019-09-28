import Bugdetectionuniversalframe
import os
import re
class formatdetection(Bugdetectionuniversalframe.uniframe):
    def __init__(self):
        Bugdetectionuniversalframe.uniframe.__init__(self)



    def deploy(self):#Re-write deploy method
        flag=0
        self.filesort()
        if self.path != "":
            command="  splint -weak +ignoresigns +formatconst "+self.path
            os.system(command)
            r= os.popen(command)
            textlist=r.readlines()
            final=""
            for text in textlist:
            #print(text) # 打印cmd输出结果
                final=final+text
                if re.search(r"Type of parameter is not consistent with corresponding code in format string.",text):
                    flag=1
            if flag:
                final=final+"\n Looks like there is a format string vulnerability."
            else:
                final="Seems no format string vulnerability."
            self.toolbox.textupdate(self.tokentext,final)

