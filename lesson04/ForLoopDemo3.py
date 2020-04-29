e1 = {'name': 'John', 'salary': 50000}
e2 = {'name': 'Mary', 'salary': 60000}
e3 = {'name': 'Bob', 'salary': 70000}

emps = [e1, e2, e3]

print(emps)
# 求薪資總和
sum = 0
for emp in emps:
    sum = sum + emp['salary']
print(sum)

salary = []                         # 建立一個 salary 數組
for emp1 in emps:
    salary.append(emp1['salary'])   # 將 salary 內容放入數組中
print(salary)
print(max(salary))
print(min(salary))
