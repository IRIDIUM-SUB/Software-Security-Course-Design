# Software-Security-Course-Design
## 课程设计要求

1. R1	提供系统界面	所有功能要有图形界面展示,形成完整的软件系统.可以使用VS/QT/Python等工具实现.
2. R2	利用字符串匹配进行同源性检测	通过代码有效字符串对比匹配,分析样本之间的拷贝比率
3. R3	利用控制流程图CFG进行源代码同源性检测	通过提取代码的调用关系图,检测样本之间各个函数调用关系图是否相似,得出相似的概率
4. R4	栈缓冲区检测	根据栈缓冲区原理分析分配的栈数据区是否存在溢出的问题,给出可疑代码行数与列数.
5. R5	格式化字符串漏洞检测	根据格式化字符串漏洞原理分析使用的格式化函数是否存在溢出的问题,给出可疑代码行数与列数.
6. R6	提供样本库	提供漏洞检测与同源性检测样本库,样本数量不少于10个,每个代码行数不少于100行；每种漏洞至少一个.



以下为2选1:
1. A1	跨语言同源性检测验证	在软件版权保护中,有时候需要检测是否参考了有版权的代码,换用一种语言实现同样的功能,本功能可以通过CFG检测实现,但需要给出4个以上不用语言的同源性分析样本.
2. A2	支持分布式任务调度	需要设计一个主控,多个进程/主机并发检测.


以下为6选4:
1. B1	堆缓冲区检测	根据堆缓冲区原理分析分配的数据区是否存在溢出的问题,给出可疑代码行数与列数.
2. B2	整数宽度溢出检测	根据整数宽度溢出原理分析分配的数据是否存在溢出的问题,给出可疑代码行数与列数.
3. B3	整数运算溢出检测	根据整数运算溢出原理分析分配的数据是否存在溢出的问题,给出可疑代码行数与列数.
4. B4	整数符号溢出检测	根据整数符号溢出原理分析分配的数据是否存在溢出的问题,给出可疑代码行数与列数.
5. B5	空指针引用	根据课堂学习其它溢出原理是否存在空指针引用的问题,给出可疑代码行数与列数.
6. B6	竞争性条件	给出竞争性条件存在的代码位置.

以下2选1:
1. C1	同源性检测样本库	样本数大于等于50个,每个代码行数不少于100行,包含1-100行相同代码.
2. C2	漏洞检测样本库	样本数大于等于50个,每个代码行数不少于100行；每种漏洞至少一个.


## 开发测试环境
Ubuntu 18.04 LTS
## 第三方依赖
- `Tkinter`
- `CFLOW`
- `Splint`
- `Lex&Flex`

## 依赖安装
### Tkinter
Python3自带库.
### CFLOW
Linux下:
```
apt-get install cflow
```
### Splint
http://splint.org/

https://blog.csdn.net/pngynghay/article/details/18356475

**下载splint-3.1.2.src.tgz**
https://github.com/splintchecker/splint/releases/tag/splint-3_1_2

```
./configure --prefix=/usr/local/splint
# To avoid permission denied in make process, use sudo
sudo make && sudo make install 
```
```
export LARCH_PATH=/usr/local/splint/share/splint/lib
export LCLIMPORTDIR=/usr/local/splint/share/splint/import
export PATH=/usr/local/splint/bin:$PATH 
```
## Flex
https://blog.csdn.net/lishichengyan/article/details/79511161

```
sudo apt-get install flex bison
```
## 启动
```shell
cd <path>/Source
python3 Software_SEC_V2.0
```
