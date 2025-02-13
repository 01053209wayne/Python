#如何使用數字
print(8//5)
print(8+8*5)
print((8+8)*5)

# 數字函式(操作在數字的變數上)
x=7
y=-7
print(x*5)
print(x%5)#取餘數
print(str(x))#數字轉字串
print("8"+str(x))#數字與字串不能相加
print(abs(y))#取絕對值
print(pow(2,4))#2的4次方
print(max(1,2,3,4,5,6,8,7))#回傳最大值
print(min(1,2,3,4,5,6,8,7))#回傳最小值
print(round(4.6))#四捨五入

#模組
from math import *
z=6.25
print(floor(z))#無條件捨去
print(ceil(z))#無條件進位
print(sqrt(z))#開根號