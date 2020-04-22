# 某數 n 是否為質數
n = 41
check = True
for i in range(2, n//2+1):
    # 印出執行過程 Log
    print("%d mod %d 餘數 %d" % (n, i, n % i))
    if n % i == 0:
        check = False
        break

print(n, check)
