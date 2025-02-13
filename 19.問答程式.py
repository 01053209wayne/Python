# 問答程式 (Quiz Program)
from question import Question  # 從 question 模組引入 Question 類別，只引入所需部分

# 題目列表，每個題目都是一個字串，包含問題和選項
test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",  # 第一題
    "1公斤是多少公克?\n(a) 10\n(b) 100\n(c) 1000\n\n",  # 第二題
    "香蕉是甚麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"  # 第三題
]

# 建立題目物件，每個 Question 物件包含問題內容與正確答案
questions = [
    Question(test[0], "c"),  # 第一題，正確答案是 c (4)
    Question(test[1], "b"),  # 第二題，正確答案是 b (100)
    Question(test[2], "b")   # 第三題，正確答案是 b (黃色)
]

# 定義執行測驗的函式
def run_test(questions):
    score = 0  # 記錄使用者得分

    # 逐一詢問每個題目
    for question in questions:
        answer = input(question.description)  # 顯示題目，讓使用者輸入答案
        if answer == question.answer:  # 檢查使用者的回答是否正確
            score += 1  # 答對加 1 分
    
    # 顯示最終得分
    print("你得到 " + str(score) + " 分")

# 執行測驗函式
run_test(questions)
