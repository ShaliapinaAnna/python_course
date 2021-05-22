import time
d = int(input('Введите день своего рождения: '))
m = int(input('Введите месяц своего рождения: '))
y = int(input('Введите год своего рождения: '))
data = str(d) + '.' + str(m) + '.' + str(y)
data0 = time.strptime(data, "%d.%m.%Y")
data1 = time.mktime(data0)
today = time.time()
today_day = int(today - data1) // 86400
print('Ваше количество дней =' + str(today_day))
