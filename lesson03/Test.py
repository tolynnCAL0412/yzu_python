# Test8 (雞兔同籠)
n = 83
f = 240

c = 0
r = 0

r = (f - (n * 2)) / 2
r1 = (f - (n * 2)) // 2
c = n - r

print("雞有 %d 隻, 兔子有 %d 隻" % (c, r))
print("雞有 " + str(c) + " 隻, 兔子有 " + str(r) + " 隻")
print("雞有 " + str(c) + " 隻, 兔子有 " + str(r1) + " 隻")


# Test5
x = 6/2*(1+2)
print(x)


# Test6
x = True
y = False
z = False
if x or y and z:
    print("yes")
else:
    print("no")


# Test7
x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
