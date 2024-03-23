# 因为密文中不可能出现000000，所以可以把000000当作空白信息以忽略
import math
from PIL import Image
#不能用R=G=B=[]，会使得输出结果一致，python不是按顺序运行的吗，为什么会这样？
R=[]
G=[]
B=[]
def factorization(n):   #将一个整数近似分解为两个尽量接近的整数的积
    a=b=int(math.sqrt(n))
    error=float('inf')
    if a**2==int(n):return a,b
    else:
        i=0
        while error>0:
            i+=1
            if i%2:a+=1
            else:b+=1
            error = n - a * b
        return a,b

with open('coding.code','r') as code:
    word=code.read()
l=len(word)

for i in range(0,l,2):
    if i%6==0:R.append(int(word[i]+word[i+1],16))
    elif i%6==2:G.append(int(word[i]+word[i+1],16))
    elif i%6==4:B.append(int(word[i]+word[i+1],16))
w,h=factorization(len(B))   #计算应该生成多大的图像
image = Image.new('RGB', factorization(len(B)))
print(R)
print(G)
print(B)
print(l/6)
print(w,'*',h)
rgb=[]
i=0
for i in range(0,len(B)):
    rgb.append((R[i],G[i],B[i]))
i=0
for i in range(1,w*h-len(rgb)+1):
    rgb.append((0,0,0))
rgb=tuple(rgb)
print(rgb)
print(len(rgb))
for y in range(0,h):
    for x in range(0,w):
        print(x,y)
        image.putpixel((x,y),rgb[x+w*y])  # 顺序：从左往右,从上往下
image.show()
image.save('pngfromcode.png')