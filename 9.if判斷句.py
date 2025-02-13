# if判斷句

#if&else
x=True
if x :
   print("teue")
else :
    print('false')
#elif
y=input("請輸入考試成績:")   
score = int(y)
if score==100 :
    print("滿分")
elif score>=90 :
    print("90以上")
elif score>=80 :
    print("80以上")
elif score>=70 :
    print("70以上")
elif score>=60 :
    print('pass')
else:
    print("不及格")
#if +and
R=False
if score==100 and not(R):
    print("你沒騙人")
else:
    print("你說謊")
#if + or
if score==100 or score>=90:
    print("高分群")
else:
    print("低分群")
#判斷函數練習
def max_num(num1,num2,num3) :
    if num1>num2 and num1>num3 :
        return num1
    elif num2>num1 and num2>num3 :
        return num2
    elif num3>num1 and num3>num2 :
        return num3
    
print(max_num(1,3,5))