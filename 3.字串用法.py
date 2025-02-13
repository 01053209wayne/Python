#字串的用法
print("hello \nwayne")#換行
print("hello\"wayne")
print("hello" + "wayne")
x='hello'
print(x+"wayne")

#字串函式(操作在字串的變數上)
print(x.lower())#小寫
print(x.upper())#大寫
print(x.islower())#確認小寫
print(x.isupper())#確認大寫
print(x.lower().islower())#變小寫再確認小寫
print(x[0])#位置函數-----從0開始數
print(x.index("h"))#找字串的位置
print(x.replace("h","w"))#替換字串