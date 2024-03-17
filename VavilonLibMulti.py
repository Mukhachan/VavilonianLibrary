from io import TextIOWrapper
import random
import threading
import multiprocessing
# import queue
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

title_dic = "абвгдеёжзийклмнопрстуфхчшщъыьэюя"
dic = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя.,:-;" '
cores = 1

def gen_title():
    lst = ''.join(random.choice(title_dic) for i in range(random.randrange(5, 20)))
    return lst
def gen_page(pg_len: int):
    lst = ''.join(random.choice(dic) for i in range(pg_len))
    return lst

def logic(f: TextIOWrapper, i: int):
    res = ''
    for i in range(1000):
        title = gen_title()
        pg = gen_page(1400)
        line = f'{title}@{pg}\n'
        if line not in f.readlines():
            res += line
    print(f'поток {i} завершается')
    f.write(res)


print("Старт")
start_time = datetime.now()  
results = []
threads = []
f = open('VavilonLib1.txt', mode='a+', encoding='utf8')

for i in range(cores):
    thrd = multiprocessing.Process(target=logic, kwargs={'f' : f, 'i': i})
    threads.append(thrd)
    thrd.start()
    print(f"+ поток №{i}")

print(threads)

for thread in threads:
    print(f"- поток №{i}")
    thread.join()
    # return_value = thread.result()
    # results.append(return_value)


# f.write(wrt)
f.close()
# x+=1

execution_time = datetime.now() - start_time 
print(execution_time)        
