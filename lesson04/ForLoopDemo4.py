e1 = {'name': 'John', 'salary': 50000, 'program': ['Java', 'Python']}
e2 = {'name': 'Mary', 'salary': 60000, 'program': ['VB', 'Python']}
e3 = {'name': 'Bob', 'salary': 70000, 'program': ['C#']}

emps = [e1, e2, e3]
# 求會 Python 的人名

# 我的解法
names = []
for emp in emps:
    for i in emp['program']:
        if i == "Python":
            names.append(emp['name'])
print(names)

# 老師的解法
names = []
lan = 'Python'
for emp in emps:
    for p in emp['program']:
        if p == lan:
            names.append(emp['name'])
print(names)
