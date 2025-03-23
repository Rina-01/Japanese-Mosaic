import os, sys

from JMFilePrepare import JMFilePrepare
from JapaneseMosaic import JapaneseMosaic


DIR_NAME = os.path.abspath(os.path.dirname(__file__))

file_name = input("Введите имя файла: ")


if os.path.exists(DIR_NAME + "\\logs\\" + file_name + " logs.txt"):
    os.remove(DIR_NAME + "\\logs\\" + file_name + " logs.txt")

logs = open(DIR_NAME + "\\logs\\" + file_name + " logs.txt", 'w', encoding='utf-8')



if os.path.exists(DIR_NAME + "\\task_files\\" + file_name + ".npy"):
    os.remove(DIR_NAME + "\\task_files\\" + file_name + ".npy")

my_file = JMFilePrepare(DIR_NAME, file_name)
a = my_file.run()
print('Файл обработан: ' + a, file=logs)

if a != 'Успешно':
    print(a)
    logs.close()
    exit()



stek = []
index = 0

stek.append(JapaneseMosaic(log=logs))
res = stek[0].task_load(DIR_NAME + "\\task_files\\" + file_name + ".npy")
print('', file=logs)
print('Загрузка задания: ' + res, file=logs)

if res != 'Успешно':
    print(res)
    logs.close()
    exit()


res = stek[0].run()
print('Первичная обработка + запуск: ' + res, file=logs)

if res != 'Задача успешно решена':
    print('', file=logs)
    print('Цикл:', file=logs)
    res = 'success'


    def work(i, j, c):
        global index
        global stek
        
        index += 1
        stek.append(JapaneseMosaic(log=logs))
        stek[index].hand_init(task=stek[0].task, solution=stek[index-1].sol, ni=i, nj=j, nc=c)
        
        print(index, i, j, '  ', stek[index].sol[i][j], c, file=logs)
        stek[index].sol[i][j] = c
        
        go = stek[index].run()
        pr = stek[index].check()
        
        if go == 'Задача успешно решена' and pr[0] == 0:
            return 'Задача успешно решена'
        
        if pr[0] == 0:
            return 'success'
        
        return 'error'


    while res != 'Задача успешно решена' and index != -1:
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
if res == 'Задача успешно решена':
    print('Задача успешно решена')
    stek[index].printsol(sys.stdout)
    print('Задача успешно решена', file=logs)
    stek[index].printsol()
    stek[index].save(DIR_NAME + "\\sol_files\\" + file_name)
else:
    print('Решение не найдено')
    print('Решение не найдено', file=logs)

logs.close()
