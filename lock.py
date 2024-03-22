# 该项目旨在提供对称加密并以.code格式记录文本信息
import hashlib
from decimal import Decimal, getcontext
# 公钥处理
def key(k):
    sha3_224=hashlib.sha3_224()
    sha3_224.update(k.encode('utf-8'))
    sha3_224.hexdigest() #56位16进制数
    return int(sha3_224.hexdigest(),16)#被开根数
def sqrt(x,prec):# 实验证明，x的大小对运行时间几乎没有影响，prec的大小则有显著影响;prec与耗时的关系可见Figure_1.png
    getcontext().prec=prec+33 #设置小数点后精度,prec>=1,perc若小于34，则在计算中会出现科学计数法表示的情况，所以给prec加上33
    _y=list(str(Decimal(x).sqrt()))
    if '.' in _y:_y.remove('.') #去除小数点
    return _y
def coding(word,key):
    prec=len(word)
    encode=[]
    for i in range(len(word)):
        encode.append(ord(word[i])+int(sqrt(key,prec)[i]))
    return encode
def decode(word,key):
    prec = len(word)
    encode=[]
    for i in range(len(word)):
        encode.append(chr(ord(word[i])-int(sqrt(key,prec)[i])))
    return encode

def numtohex(num):
    num=hex(num)[2:]    #转换为十六进制字符
    num='0'*(6-len(num))+num   #补齐位数
    return num

while 1:
    command=input('-->')
    if command=='\exit':break
    if command=='encode':
        k=input('key-->')
        while 1:
            word=input('encode-->')
            if word=='\exit':break
            path='coding.code'
            with open(path,'w') as file:pass    #新建coding.code或把原有的coding.code变为空文件
            with open(path,'a') as file:
                for i in range(len(word)):
                    file.write(numtohex(coding(word,key(k))[i]))    #写入密文
            print('done')
    if command=='decode':
        k=input('key-->')
        path=input('path-->')
        with open(path, 'r') as file:
            word = file.read()
        spilt=[]
        for i in range(1,int(len(word)/6+1)):
            spilt.append(chr(int(word[(i-1)*6:i*6],16)))    #分割文件内容，6个字符为一组，并转为十进制后再转为字符串
        spilt=''.join(spilt)
        for j in range(len(spilt)):
            print(decode(spilt,key(k))[j],end='')
        print()
