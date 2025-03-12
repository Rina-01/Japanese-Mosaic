import numpy as np

class JapaneseMosaic():
    def __init__(self, test_mode=True):
        # self.status = 'success'
        self.test_mode = test_mode

    
    def task_load(self, file_name):
        try:
            self.task = np.load(file_name)
        except:
            return 'Ошибка при открытии файла'
            
        self.n = len(self.task)
        self.m = len(self.task[0])
        
        self.sol = np.zeros((self.n, self.m), int)
        for i in range(self.n):
            self.sol[i][0] = self.sol[i][self.m-1] = 10
        
        for j in range(self.m):
            self.sol[0][j] = self.sol[self.n-1][j] = 10
        
        return 'Успешно'
    
    def printsol(self):                 # print sol 
        print(chr(9484) + chr(9472) * (self.m - 2) + chr(9488))
        for i in range(1, self.n-1):
            s = chr(9474)
            for j in range(1, self.m-1):
                if self.sol[i][j] == 1:         # закрашенное
                    s += chr(9608)
                elif self.sol[i][j] == 10:      # крест
                    s += chr(9587)
                else:
                    s += ' '
            s += chr(9474)
            print(s)
        print(chr(9492) + chr(9472) * (self.m - 2) + chr(9496))
    
    def printst(self):                  # print sol + task
        print(chr(9484) + chr(9472) * (self.m - 2) + chr(9488)  + '     ' + chr(9484) + chr(9472) * (self.m - 2) + chr(9488))
        for i in range(1, self.n-1):
            s = chr(9474)
            for j in range(1, self.m-1):
                if self.sol[i][j] == 1:         # закрашенное
                    s += chr(9608)
                elif self.sol[i][j] == 10:      # крест
                    s += chr(9587)
                else:                           # 
                    s += ' '
            s += chr(9474)
        
            s += '     ' 
            s += chr(9474)
            for j in range(1, self.m-1):
                if self.task[i][j] == -5:       # ничего нет
                    s += '_'
                elif self.task[i][j] > 0:       # число
                    s += str(self.task[i][j])
                else:                           # было число
                    s += str(- self.task[i][j] - 10)
            s += chr(9474)
            print(s)
        print(chr(9492) + chr(9472) * (self.m - 2) + chr(9496) + '     ' + chr(9492) + chr(9472) * (self.m - 2) + chr(9496))
        
    
    def full(self):
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.task[i][j] > 0:
                    return False
        return True
       
    def sum(self, i, j):
        if i*j == 0 or i == self.n-1 or j == self.m-1:
            return 0
        return self.sol[i-1][j-1] + self.sol[i-1][j] + self.sol[i-1][j+1] + self.sol[i][j-1] + self.sol[i][j] + self.sol[i][j+1] + self.sol[i+1][j-1] + self.sol[i+1][j] + self.sol[i+1][j+1]

    def fill(self, i, j, c):
        if self.sol[i-1][j-1] == 0:
            self.sol[i-1][j-1] = c
        if self.sol[i-1][j] == 0:
            self.sol[i-1][j] = c
        if self.sol[i-1][j+1] == 0:
            self.sol[i-1][j+1] = c
        
        if self.sol[i][j-1] == 0:
            self.sol[i][j-1] = c
        if self.sol[i][j] == 0:
            self.sol[i][j] = c
        if self.sol[i][j+1] == 0:
            self.sol[i][j+1] = c
        
        if self.sol[i+1][j-1] == 0:
            self.sol[i+1][j-1] = c
        if self.sol[i+1][j] == 0:
            self.sol[i+1][j] = c
        if self.sol[i+1][j+1] == 0:
            self.sol[i+1][j+1] = c

        
    def run_init(self): 
        # обработка 0 и 9
        for i in range(2, self.n - 2):
            for j in range(2, self.m - 2):
                if self.task[i][j] == 0:
                    self.fill(i, j, 10)
                    self.task[i][j] = - self.task[i][j] - 10
                if self.task[i][j] == 9:
                    self.fill(i, j, 1)
                    self.task[i][j] = - self.task[i][j] - 10
        
        # обработка на различные ситуации
        # ситуация 1
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.task[i][j] > 0:
                    if self.task[i][j] - 3 == self.task[i-1][j]:    # верх
                        if self.test_mode:
                            print(1, i, j, 1)
                        self.sol[i-2][j-1] = self.sol[i-2][j] = self.sol[i-2][j+1] = 10
                        self.sol[i+1][j-1] = self.sol[i+1][j] = self.sol[i+1][j+1] = 1
                    if self.task[i][j] - 3 == self.task[i+1][j]:    # низ
                        if self.test_mode:
                            print(1, i, j, 2)
                        self.sol[i-1][j-1] = self.sol[i-1][j] = self.sol[i-1][j+1] = 1
                        self.sol[i+2][j-1] = self.sol[i+2][j] = self.sol[i+2][j+1] = 10
                    if self.task[i][j] - 3 == self.task[i][j+1]:    # право
                        if self.test_mode:
                            print(1, i, j, 3)
                        self.sol[i-1][j-1] = self.sol[i][j-1] = self.sol[i+1][j-1] = 1
                        self.sol[i-1][j+2] = self.sol[i][j+2] = self.sol[i+1][j+2] = 10
                    if self.task[i][j] - 3 == self.task[i][j-1]:    # лево
                        if self.test_mode:
                            print(1, i, j, 4)
                        self.sol[i-1][j+1] = self.sol[i][j+1] = self.sol[i+1][j+1] = 1
                        self.sol[i-1][j-2] = self.sol[i][j-2] = self.sol[i+1][j-2] = 10

        # ситуация 2
        for i in range(2, self.n - 2):
            for j in range(2, self.m - 2):
                if self.task[i][j] == 8 or self.task[i][j] == 7:
                    if self.task[i][j] - 6 == self.task[i-2][j]:    # верх
                        if self.test_mode:
                            print(2, i, j, 1)
                        self.sol[i][j-1] = self.sol[i][j] = self.sol[i][j+1] = 1
                        self.sol[i+1][j-1] = self.sol[i+1][j] = self.sol[i+1][j+1] = 1
                        self.sol[i-3][j-1] = self.sol[i-3][j] = self.sol[i-3][j+1] = 10
                        self.sol[i-2][j-1] = self.sol[i-2][j] = self.sol[i-2][j+1] = 10
                    if self.task[i][j] - 6 == self.task[i+2][j]:    # низ
                        if self.test_mode:
                            print(2, i, j, 2)
                        self.sol[i-1][j-1] = self.sol[i-1][j] = self.sol[i-1][j+1] = 1
                        self.sol[i][j-1] = self.sol[i][j] = self.sol[i][j+1] = 1
                        self.sol[i+2][j-1] = self.sol[i+2][j] = self.sol[i+2][j+1] = 10
                        self.sol[i+3][j-1] = self.sol[i+3][j] = self.sol[i+3][j+1] = 10
                    if self.task[i][j] - 6 == self.task[i][j+2]:    # право
                        if self.test_mode:
                            print(2, i, j, 3)
                        self.sol[i-1][j-1] = self.sol[i][j-1] = self.sol[i+1][j-1] = 1
                        self.sol[i-1][j] = self.sol[i][j] = self.sol[i+1][j] = 1
                        self.sol[i-1][j+2] = self.sol[i][j+2] = self.sol[i+1][j+2] = 10
                        self.sol[i-1][j+3] = self.sol[i][j+3] = self.sol[i+1][j+3] = 10
                    if self.task[i][j] - 6 == self.task[i][j-2]:    # лево
                        if self.test_mode:
                            print(2, i, j, 4)
                        self.sol[i-1][j+1] = self.sol[i][j+1] = self.sol[i+1][j+1] = 1
                        self.sol[i-1][j] = self.sol[i][j] = self.sol[i+1][j] = 1
                        self.sol[i-1][j-2] = self.sol[i][j-2] = self.sol[i+1][j-2] = 10
                        self.sol[i-1][j-3] = self.sol[i][j-3] = self.sol[i+1][j-3] = 10

        
    def run(self):
        # первичная обработка
        self.run_init()
        
        fl = True
        while fl:
            fl = False

            # обработка на число свободных клеток
            for i in range(1, self.n - 1):
                for j in range(1, self.m - 1):
                    if self.task[i][j] > 0:
                        k, z = divmod(self.sum(i, j), 10)
                        if k + z == 9:                  # все клетки обработаны
                            self.task[i][j] = - self.task[i][j] - 10
                            continue
                        if z == self.task[i][j]:        # всё что должно быть закрашено уже закрашено
                            self.fill(i, j, 10)
                            self.task[i][j] = - self.task[i][j] - 10
                            fl = True
                        if 9 - k == self.task[i][j]:    # всё что свободно должно быть закрашено
                            self.fill(i, j, 1)
                            self.task[i][j] = - self.task[i][j] - 10
                            fl = True

            if fl and self.test_mode:
                self.printst()
        
        self.printsol()
        
        res = self.full()
        if res:
            return 'Задача успешно решена'

        return 'Решение не найдено'
