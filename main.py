import os

from JMFilePrepare import JMFilePrepare
from JapaneseMosaic import JapaneseMosaic


DIR_NAME = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"

# file_name = input("Введите имя файла: ")
file_name = '10-15 1'


if os.path.exists(DIR_NAME + "\\logs\\" + file_name + " logs.txt"):
    os.remove(DIR_NAME + "\\logs\\" + file_name + " logs.txt")

logs = open(DIR_NAME + "\\logs\\" + file_name + " logs.txt", 'w', encoding='utf-8')


my_file = JMFilePrepare(DIR_NAME, file_name)
print(my_file.run(), file=logs)


test = JapaneseMosaic(logs)
a = test.task_load(DIR_NAME + "\\task_files\\" + file_name + ".npy")
print('Загрузка задания: ' + a, file=logs)

if a != 'Успешно':
    logs.close()
    exit()

print('Результат выполнения: ' + test.run(), file=logs)
test.printsol()

os.remove(DIR_NAME + "\\task_files\\" + file_name + ".npy")

logs.close()