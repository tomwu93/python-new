# 請使用者輸入身高(cm)與體重(kg)，計算並印出 BMI 值與體位判斷
height = float(input("請輸入身高（cm）："))
weight = float(input("請輸入體重（kg）："))

# 體重除以身高的平方（需先將公分轉為公尺）
bmi = weight / (height / 100) ** 2

# 依 BMI 數值分類體位（標準）
if bmi < 18.5:
    category = "過輕"
elif 18.5 <= bmi < 24:
    category = "正常"
elif 24 <= bmi < 27:
    category = "過重"
else:
    category = "肥胖"

# 印出結果
print("BMI 值為：{:.2f}".format(bmi))
print("體位為：{}".format(category))
