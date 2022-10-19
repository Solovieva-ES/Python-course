salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
grow = 1.03
need_money = 0  # количество денег, чтобы прожить 10 месяцев

different = spend - salary
need_money += different
i = 1
while i <= 9:
    spend = spend * 1.03
    different = spend - salary
    need_money += different
    i += 1
print(round(need_money))
