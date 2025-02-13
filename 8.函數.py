#function
#分成定義與呼叫

#1定義
def hello():
    print("hello")
#2呼叫
hello()

#1定義+變數
def hello(name,age):
    print("hello"+name+"你今年"+str(age)+"歲")
#2呼叫+變數
hello("帥哥",24)

#2個數字相加的函數
def summ(x,y):
    #print(x+y)
    #回傳的概念 
    return x+y     #直接取代函數
summ(1,2)          #函數運算後輸出不能再處理了
print(summ(1,2)+6) #return是為了對回傳後值繼續運算處理

#考題1
def summ(x,y):
    return 10      
value= summ(1,2)   
print(value)  #答案10

#考題2
def summ(x,y):
    print(x+y)
    return None#相當於沒有打出return
value=summ(1,2)   
print(value)   #答案為none 因為沒有回傳為預設成none成none
#函式碰到return就會被終止 