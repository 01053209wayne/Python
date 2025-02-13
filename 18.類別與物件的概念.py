# 定義類別
class Phone:
    # 建立手機物件的模板
    def __init__(self, os, number, is_waterproof):
        self.os = os  # 記錄手機的作業系統
        self.number = number  # 記錄手機的編號
        self.is_waterproof = is_waterproof  # 記錄是否防水
#物件函式
    # 定義判斷是否為 iOS 的方法
    def is_ios(self):
        if self.os == "ios":
            return True
        return False

    # 加法運算方法（修正為物件方法）
    def add(self, number1, number2):
        return number1 + number2

# 建立手機物件
phone1 = Phone("ios", 123, True)

# 正確呼叫 add 方法
print(phone1.add(5, 6))  # 輸出應該是 11
