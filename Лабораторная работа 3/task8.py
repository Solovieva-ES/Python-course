money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
different = 0
while money_capital + salary >= spend:
    spend = spend * 1.05
    money_capital += (salary - spend)
    month += 1

print(month)
