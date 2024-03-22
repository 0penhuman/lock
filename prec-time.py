from decimal import Decimal, getcontext
import time
import matplotlib.pyplot as plt
import numpy as np
'''显而易见，用decimal求平方根时，耗时和精度呈非线性关系，且斜率随prec的增大而增大'''
def sqrt(x,prec):
    getcontext().prec=prec
    _y=list(str(Decimal(x).sqrt()))
    if '.' in _y:_y.remove('.')
    return _y
y=[]
t=[]
for i in range(1,1000):
    begin=time.time()
    sqrt(2,i)
    end=time.time()
    y.append(end-begin)
    t.append(i)
t=np.array(t)
y=np.array(y)
# 创建坐标轴
plt.figure(figsize=(8,6))  # 设置图形大小
plt.plot(t, y, '-')  # 绘制数据点并用实线连接，'o'表示圆形标记

# 添加标题和坐标轴标签
plt.title("prec--time")
plt.xlabel("prec")
plt.ylabel("time")

# 添加网格
plt.grid(True)

# 显示图形
plt.show()
