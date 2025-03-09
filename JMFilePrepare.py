import numpy as np

CHAR_NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class JMFilePrepare():
    def __init__(self, dir_name, file_name):
        self.dir = dir_name
        self.fn = file_name
        self.task = []
        self.status = 'success'
    
    def print(self):
        for row in self.task:
            print(row)
    
    def open(self):
        try:
            self.task_file = open(self.dir + "\\tasks\\" + self.fn + ".txt", 'r')
        except FileNotFoundError:
            self.status = 'Файл не найден или не может быть открыт'
        except:
            self.status = 'Ошибка при открытии файла'
    
    def validation(self):
        m = len(self.task[0])
        for row in self.task:
            if len(row) != m:
                self.status = 'Разная длина строк в файле'
                return
        
    def save(self):
        try:
            np.save(self.dir + "\\task_files\\" + self.fn, self.task)
        except FileNotFoundError:
            self.status = 'Путь для сохраенния файла не найден'
        except:
            self.status = 'Ошибка при сохранении файла'
    
    def run(self):
        self.open()
        if self.status != 'success':
            return
        
        for line in self.task_file:
            task_line = []
            for i in range(len(line)):
                if line[i] == ' ':
                    task_line.append(-1)
                elif line[i] in CHAR_NUMS:
                    task_line.append(int(line[i]))
                elif line[i] == '\n':
                    continue
                else:
                    self.status = 'Неправильный символ в файле'
                    self.task_file.close()
                    exit()
            self.task.append(task_line)
        
        self.validation()
        if self.status != 'success':
            return
        
        self.save()
        if self.status != 'success':
            return
        
        return 'Файл обработан успешно'

