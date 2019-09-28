# Software-Security-Course-Design
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
