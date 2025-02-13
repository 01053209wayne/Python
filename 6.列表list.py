#列表用法(中括號)
#用來管理資料
score1 = 90
score2 = 80
score3 = 70 
score4 = 60
score5 = 50
scores=[50,60,70,80,90]
print(scores)
print('第4個數字為'+str(scores[3]))
print('從0~1數字為'+str(scores[0:2]))
print(scores[:2])#01
scores[0]=40
print(scores)


friend1="小黑"
friend1="小白"
friends=["小黑","小白"]
print(friends)

#函數
scores.extend(friends)#合併列表
print(scores)
scores.append(30)#放到最後
print(scores)
scores.insert(2,30)#插入中間
print(scores)
scores.remove(90)#移除90
print(scores)
scores.clear()#清空
print(scores)




x=[1,3,2,5,7]
x.sort()#排序
print(x)
x.pop()#移除最後一個數
print(x)
x.reverse()#反轉列表
print(x)
print(x.index(2))#回傳位置
print(x.count(1))#數有幾個數字