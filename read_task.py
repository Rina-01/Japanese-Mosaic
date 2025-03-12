import numpy as np


dir_name = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"
char_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# file_name = input("Введите имя файла: ")
file_name = '10-15 1'


try:
    task_file = open(dir_name + "\\tasks\\" + file_name + ".txt", 'r')
except OSError:
    exit()
    print('Файл не найден или не может быть открыт')
except:
    exit()
    print('Ошибка при открытии файла')


task = []

for line in task_file:
    task_line = []
    task_line.append(-5)
    for i in range(len(line)):
        if line[i] == ' ':
            task_line.append(-5)
        elif line[i] in char_nums:
            task_line.append(int(line[i]))
        elif line[i] == '\n':
            continue
        else:
            print('Неправильный символ в файле')
            task_file.close()
            exit()
    task_line.append(-5)
    task.append(task_line)

task_file.close()

task

m = len(task[0])

j = 0
for row in task:
    print(j+1, len(row))
    j = j + 1


task = [ [-5] * m ] + task

task.append( [-5] * m )

tnptask = np.array(task, dtype=int)
tnptask

np.save(dir_name + "\\task_files\\" + file_name, tnptask)


t1 = np.load(dir_name + "\\task_files\\" + file_name + ".npy")
t1

