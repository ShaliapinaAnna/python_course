import time
n = int(input('Введите число: '))
while n >= 0:
    time.sleep(n)
    n = int(input('Введите число: '))
    if n < 0:
        break
