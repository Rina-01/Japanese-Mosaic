import os

from JapaneseMosaic import JapaneseMosaic

DIR_NAME = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"
FILE_NAME = '10-15 3'

stek = []
index = 0

if os.path.exists(DIR_NAME + "\\logs\\" + FILE_NAME + " logs.txt"):
    os.remove(DIR_NAME + "\\logs\\" + FILE_NAME + " logs.txt")

logs = open(DIR_NAME + "\\logs\\" + FILE_NAME + " logs.txt", 'w', encoding='utf-8')


stek.append(JapaneseMosaic(logs))
a = stek[0].task_load(DIR_NAME + "\\task_files\\" + FILE_NAME + ".npy")
print('Загрузка задания: ' + a, file=logs)

if a != 'Успешно':
    logs.close()
    exit()

a = stek[0].run()
print('Первичная обработка + запуск: ' + a, file=logs)

if a == 'Задача успешно решена':
    stek[0].printsol()
    logs.close()
    exit()


print('', file=logs)
print('Цикл:', file=logs)

def work(i, j, c):
    global index
    global stek
    
    index += 1
    stek.append(JapaneseMosaic(logs))
    stek[index].hand_init(task=stek[0].task, solution=stek[index-1].sol, ni=i, nj=j, nc=c)
    
    print(index, i, j, '  ', stek[index].sol[i][j], c, file=logs)
    stek[index].sol[i][j] = c
    
    go = stek[index].run()
    pr = stek[index].check()
    
    if go == 'Задача успешно решена' and pr[0] == 0:
        print(go, file=logs)
        stek[index].printsol()
        return 'full_success'
    
    if pr[0] == 0:
        return 'success'
    
    return 'error'


res = 'success'

while res != 'full_success' and index != -1:
    if res == 'success':
        i, j = stek[index].empty()
        print('Пробуем дальше с', i, j, file=logs)
        res = work(i, j, 1)
    else:
        print('Возвращаемся к', index-1, file=logs)
        i = stek[index].i
        j = stek[index].j
        c = stek[index].c
        index -= 1
        uuu = stek.pop()
        if c == 1:
            print('Пробуем', i, j, file=logs)
            res = work(i, j, 10)
        else:
            continue
    

print('', file=logs)
print('Итог: ', index, file=logs)

for n in range(index+1):
    print(n, file=logs)
    print(stek[n].i, stek[n].j, stek[n].c, file=logs)
    stek[n].printsol()
    print('', file=logs)

logs.close()