#for 迴圈

# for 變數 in 字串或列表 :
#            執行程式碼

#1
for letter in "小白你好":
    print(letter) #字串依序放入變數
#2  
for num in [0,1,2,3,4]:
    print(num)    #數字依序放入變數
#3----與2相同
for num in range(5):
    print(num)
#4 for迴圈的函數(次方)  
def power(n1,n2):
    result = n1
    for index in range(n2-1) : #跑5次
        result = result * n1
    return result
print(power(2,5))