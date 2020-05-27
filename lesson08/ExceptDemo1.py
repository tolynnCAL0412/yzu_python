x = 10
y = int(input('請輸入數字:'))
try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print('有錯誤發生', e)
    print(e.__class__.__name__)
