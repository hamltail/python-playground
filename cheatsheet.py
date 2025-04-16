# 🐍 Pythonミニチートシート

# 🔸 基本文法

# 変数
x = 10
name = "はむる"

# 条件分岐
if x > 5:
    print("xは5より大きい")

# 繰り返し
for i in range(3):
    print(i)

# 関数定義
def greet(name):
    return f"こんにちは、{name}さん！"

print(greet(name))

# リストと辞書
fruits = ["apple", "peach", "cherry"]
info = {"name": "はむる", "age": 99}

print(fruits)
print(info)

for fruit in fruits:
    print(fruit)

for key, value in info.items():
    print(f"{key}: {value}")

print("アレルギー一覧：", ", ".join(fruits))
print(f"名前：{info['name']} / 年齢：{info['age']}")


# 🔸 クラスとオブジェクト

class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"こんにちは、{self.name}さん！"

user = User("Hamru")
print(user.greet())


# 🔸 ファイル操作

# ファイルの読み書き
with open("wish.txt", "w") as f:
    f.write("Switch2が欲しい！")

with open("wish.txt", "r") as f:
    content = f.read()
    print(content)


# 🔸 エラー処理

try:
    result = 10 / 0
except ZeroDivisionError:
    print("ゼロ除算はできません")


# 🔸 モジュールの利用

import math
print(math.sqrt(16))

import datetime
now = datetime.datetime.now()
print(now)
