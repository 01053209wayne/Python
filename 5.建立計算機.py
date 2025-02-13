#建立簡單計算機

#input預設成字串
x1=input('請輸入第一個數字:')
x2=input('請輸入第二個數字:')
ans=x1+x2
print("沒有轉成數字:"+ans)

#int可以將字串轉成數字
ans1=int(x1)+int(x2)
print("有轉成數字:"+str(ans1))

#float浮點數相加的話1.
ans2=float(x1)+float(x2)
print("有小數點的相加:"+str(ans2))