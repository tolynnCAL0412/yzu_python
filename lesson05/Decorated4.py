def login(func, password):
    def check():
        if password == 1234:
            print("登入成功")
            func()
        else:
            print("登入失敗")
            return None
    return check

@login(None, password=1234)
def report():
    print("密件: 今日頭條....")

report()
