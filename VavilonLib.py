import random
from datetime import datetime
from config import title_dic, dic, filename

def gen_title():
    lst = ''.join(random.choice(title_dic) for i in range(random.randrange(5, 20)))
    return lst
def gen_page(pg_len: int):
    lst = ''.join(random.choice(dic) for i in range(pg_len))
    return lst

def main():
    print("Старт")
    while True:
        # start_time = datetime.now()        
        pages = []
        with open(filename, mode='a+', encoding='utf8', buffering=8192) as f:
            for i in range(1000):
                title = gen_title()
                pg = gen_page(1400)
                line = f'{title}@{pg}\n'
                if line not in f.readlines():
                    pages.append(line)
            f.write("".join(pages))
            f.close()
        # execution_time = datetime.now() - start_time 
        # print(execution_time)
        # break
     
main()