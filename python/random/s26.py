
import os
import random
import time

files = os.listdir('somedir')
for file in files:
    file = os.path.join('somedir', file)
    print(time.ctime(os.path.getctime(file)))


# for i in range(3):
#     pf = open(f'somedir/bla{i}.txt', 'w')
#     pf.close()
#     time.sleep(random.random() * 10)
