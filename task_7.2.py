import time
t1 = time.time()
a = 0
for i in range(10):
    a += i
t2 = time.time()
all_time = t2 - t1
data = time.strftime('%H_%M_%S %d_%m_%Y')
with open(str(data) + '.txt', 'w') as file:
    file.write(str(all_time))
