[TOC]

# Splint
## Install

**Attention: Need  -xvf splint-3.1.2.src.tgz or  cause Error.**

Need command `Make` aviliable first.
```shell
tar -xvf splint-3.1.2.src.tgz

cd splint-3.1.2

./configure --prefix=/usr/local/splint

# To avoid permission denied in make process, use sudo


sudo make && sudo make install 
```

## Deploy

1. Open `~./bashrc`
2. Add following instruction:
```
export LARCH_PATH=/usr/local/splint/share/splint/lib
export LCLIMPORTDIR=/usr/local/splint/share/splint/import
export PATH=/usr/local/splint/bin:$PATH 
```
3. Enable new bashrc,use`source ~/.bashrc`
4.  Finished.

## Parameter scheme
Here are some useful Parameter

+:open
-:close

varuse: If check the use of variable

showcol:If Show column?

?

When detecting *stack overflow*,use parameter like:
`+bounds`

When *format string overflow*,use:
`-weak +ignoresigns + formatconst +formattype`

Add `-linelen %d` to sort the format of output

This tool can be used in the following bugs:
- stack overflow
- Format string
- Empty pointer

Reference:https://blog.csdn.net/xiaowang1379214245/article/details/82688802

## Command Example
### Stack overflow
```
splint +weak +bounds -hints +ignoresigns stackof0.c
```
Output:
```
Splint 3.1.2 --- 09 Sep 2019

stackof0.c: (in function func)
stackof0.c:10:2: Possible out-of-bounds store: strcpy(buf, in)
    Unable to resolve constraint:
    requires maxRead(in @ stackof0.c:10:14) <= 9
     needed to satisfy precondition:
    requires maxSet(buf @ stackof0.c:10:9) >= maxRead(in @ stackof0.c:10:14)
     derived from strcpy precondition: requires maxSet(<parameter 1>) >=
    maxRead(<parameter 2>)
```
### Format overflow
```
asr@ubuntu-18-04-3-lts-course-design:~/Documents/COURSEDESIGNTEST/Source$ splint -weak +ignoresigns +formatconst +formattype '/home/asr/Documents/COURSEDESIGNTEST/test/Formattest.c' 
Splint 3.1.2 --- 09 Sep 2019

Command Line: Setting +formattype redundant with current value
../test/Formattest.c: (in function main)
../test/Formattest.c:5:30: Format argument 3 to printf (%s) expects char * gets
                              int: b
  Type of parameter is not consistent with corresponding code in format string.
  (Use -formattype to inhibit warning)
   ../test/Formattest.c:5:21: Corresponding format code

Finished checking --- 1 code warning
```
**Very important:when use re.findall,see https://blog.csdn.net/tp7309/article/details/72823258**