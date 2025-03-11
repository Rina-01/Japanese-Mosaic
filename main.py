import numpy as np

from JMFilePrepare import JMFilePrepare
from JapaneseMosaic import JapaneseMosaic


dir_name = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"

# file_name = input("Введите имя файла: ")
file_name = '10-15 1'


my_file = JMFilePrepare(dir_name, file_name)
print(my_file.run())


test = JapaneseMosaic()
a = test.task_load(dir_name + "\\task_files\\" + file_name + ".npy")
print(a)

if a != 'Успешно':
    exit()

test.print()

