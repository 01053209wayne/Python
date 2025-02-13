#檔案讀取

#open("檔案路徑",mode="開啟模式")

#檔案路徑分2種
#1.絕對路徑:ex C:/Users/wayne/Desktop/python/111.txt
#2.相對路徑:ex 111.txt

#開啟模式有3種
#1 model ="r" 讀取
#2 model ="W" 覆寫
#3 model ="a" 原先資料加東西


file = open("C:/Users/wayne/Desktop/python/111.txt",mode="r")
#print(file.read())#讀取後印出來所有內容
#for line in file :#每行印出來
#  print(line)


file = open("C:/Users/wayne/Desktop/python/111.txt",mode="w")
file.write("hello")
print(file.write("hello"))

file = open("111.txt",mode="a",encoding="utf-8")
file.write("\n帥哥")
print(file.write("\n帥哥"))

with open("111.txt",mode="a",encoding="utf-8") as file:
    file.write("\n你好啊")
