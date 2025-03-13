import os

from JMFilePrepare import JMFilePrepare
from JapaneseMosaic import JapaneseMosaic


DIR_NAME = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"

# file_name = input("Введите имя файла: ")
file_name = '10-15 1'


my_file = JMFilePrepare(DIR_NAME, file_name)
print(my_file.run())


test = JapaneseMosaic(test_mode=False)
a = test.task_load(DIR_NAME + "\\task_files\\" + file_name + ".npy")

if a == 'Успешно':
    a = test.run()
    print(a)
    test.printsol()
else:
    print(a)

os.remove(DIR_NAME + "\\task_files\\" + file_name + ".npy")
