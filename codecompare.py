import re#正则表达式相关
import os
import fileselect
# See https://blog.csdn.net/riag/article/details/3479143
# See also https://codeday.me/bug/20180522/170612.html
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
	mid=open('tmp/temp.c','w+')
	mid.write(base)
	textlist = os.popen("a.out<tmp/temp.c").readlines()
	with os.popen('./a.out<sample.c', 'r') as f:
		text=( f.read())#text is tokens' string
	#print(text) # 打印cmd输出结果
	return text

def mainprocess(self):
	selection0=fileselect.fileselect("Select Template file");#样本文件
	selection1=fileselect.fileselect("Select Sample file");#待测试文件
	templatefilename=selection0.fileselect()
	'''
	开始处理模板文件
	'''
	temp=self.tokendealing(templatefilename)
	