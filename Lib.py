from datetime import datetime
import multiprocessing
import random
from config import title_dic, dic, filename


def gen_title():
    lst = ''.join(random.choice(title_dic) for i in range(random.randrange(5, 20)))
    return lst
def gen_page(pg_len: int):
    lst = ''.join(random.choice(dic) for i in range(pg_len))
    return lst


def write_page_to_file(line):
    with open(filename, "r",  encoding='utf8', buffering=8192) as file:
        for i in range(1000):
            if line not in file.readlines():
                title = gen_title()
                pg = gen_page(1400)
                line+=f'{title}@{pg}\n'
    return line


if __name__ == "__main__":
    # Определение количества страниц
    cores = 6

    start_time = datetime.now()        
    print('Старт')
    for i in range(50):
        print('start', i, datetime.now())
        pages = [''] * cores
        print('pages: ', pages)        
        # Создание пула процессов
        pool = multiprocessing.Pool(processes=cores)

        # Многопроцессорная генерация и запись страниц
        page_numbers = range(1, cores+1)
        pages = list(pool.map(write_page_to_file, pages))
        # Закрытие пула процессов
        pool.close()
        pool.join()

        with open(filename, "a",  encoding='utf8', buffering=8192) as file:
            pages = "".join(pages)
            file.write(pages)

            
    execution_time = datetime.now() - start_time 
    print(execution_time)        