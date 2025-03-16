import numpy as np


# символы для отображения матриц
FULL = chr(9608)
KREST = chr(9587)
NOTHING = ' '

# символы для отображения границ
HOR = chr(9472)
VER = chr(9474)
RHA = chr(9488)
RLA = chr(9496)
LLA = chr(9492)
LHA = chr(9484)

DEL = '     '


class JapaneseMosaic():
    def __init__(self, test_mode=True):
        self.n = 0
        self.m = 0
        self.test_mode = test_mode
        self.i = 0
        self.j = 0

    
    def sol_load(self, file_name):
        try:
            self.sol = np.load(file_name)
        except:
            return 'Ошибка при открытии файла'
        
        if self.n == 0:
            self.n = len(self.sol)
            self.m = len(self.sol[0])
        else:
            if self.n != len(self.sol) or self.m != len(self.sol[0]):
                self.sol_init()
                self.run_init()
                return 'Ошибка, размеры матриц не совпадают'
        
        return 'Успешно'
    
    def task_load(self, file_name):
        try:
            self.task = np.load(file_name)
        except:
            return 'Ошибка при открытии файла'
        
        if self.n == 0:
            self.n = len(self.task)
            self.m = len(self.task[0])
            self.sol_init()
            self.run_init()
        else:
            if self.n != len(self.sol) or self.m != len(self.sol[0]):
                return 'Ошибка, размеры матриц не совпадают'
                
        return 'Успешно'

    def sol_init(self):
        self.sol = np.zeros((self.n, self.m), int)
        for i in range(self.n):
            self.sol[i][0] = self.sol[i][self.m-1] = 10
        
        for j in range(self.m):
            self.sol[0][j] = self.sol[self.n-1][j] = 10
    
    
    def hand_init(self, task, solution, ni, nj):
        self.task = task
        self.sol = solution.copy()
        self.n = len(self.task)
        self.m = len(self.task[0])
        self.i = ni
        self.j = nj
        
    
    def save(self, file_name):
        try:
            np.save(file_name, self.sol)
        except FileNotFoundError:
            return 'Путь для сохраенния файла не найден'
        except:
            return 'Ошибка при сохранении файла'
        return 'Решение сохранено'

    
    def printsol(self):                 # print sol 
        print(LHA + HOR * (self.m - 2) + RHA)
        for i in range(1, self.n-1):
            s = VER
            for j in range(1, self.m-1):
                if self.sol[i][j] == 1:
                    s += FULL
                elif self.sol[i][j] == 10:
                    s += KREST
                else:
                    s += NOTHING
            s += VER
            print(s)
        print(LLA + HOR * (self.m - 2) + RLA)
    
    def printst(self):                  # print sol + task 
        print(LHA + HOR * (self.m - 2) + RHA  + DEL + LHA + HOR * (self.m - 2) + RHA)
        for i in range(1, self.n-1):
            s = VER
            for j in range(1, self.m-1):
                if self.sol[i][j] == 1:
                    s += FULL
                elif self.sol[i][j] == 10:
                    s += KREST
                else:
                    s += NOTHING
            s += VER
        
            s += DEL
            
            s += VER
            for j in range(1, self.m-1):
                if self.task[i][j] == -5:       # ничего нет
                    s += NOTHING
                elif self.task[i][j] > 0:       # число
                    s += str(self.task[i][j])
                else:                           # было число
                    s += str(- self.task[i][j] - 10)
            s += VER
            print(s)
        print(LLA + HOR * (self.m - 2) + RLA + DEL + LLA + HOR * (self.m - 2) + RLA)
    
    
    def full(self):
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.sol[i][j] == 0:
                    return False
        return True
    
    def empty(self):
        if self.full():
            return (0, 0)
            
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.sol[i][j] == 0:
                    return (i, j)
        
       
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

    def check(self):
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if self.task[i][j] > 0:
                    k, z = divmod(self.sum(i, j), 10)
                    if z > self.task[i][j] or 9 - k < self.task[i][j]:
                        return (i, j)
        return (0, 0)
        
    
    def run_init(self):                 # первичная обработка 
        # обработка 0 и 9
        for i in range(2, self.n - 2):
            for j in range(2, self.m - 2):
                if self.task[i][j] == 0:
                    self.fill(i, j, 10)
                    # self.task[i][j] = - self.task[i][j] - 10
                if self.task[i][j] == 9:
                    self.fill(i, j, 1)
                    # self.task[i][j] = - self.task[i][j] - 10
        
        # обработка различных ситуации
        
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

        # ситуация 3
        for i in range(2, self.n - 2):
            for j in range(2, self.m - 2):
                if self.task[i][j] > 0:
                    if self.task[i][j] - 5 == self.task[i-1][j+1]:    # право верх
                        if self.test_mode:
                            print(3, i, j, 1)
                        self.sol[i+1][j-1] = self.sol[i+1][j] = self.sol[i+1][j+1] = 1
                        self.sol[i][j-1] = self.sol[i-1][j-1] = 1
                        self.sol[i-2][j] = self.sol[i-2][j+1] = self.sol[i-2][j+2] = 10
                        self.sol[i-1][j+2] = self.sol[i][j+2] = 10
                    if self.task[i][j] - 5 == self.task[i+1][j+1]:    # право низ
                        if self.test_mode:
                            print(3, i, j, 2)
                        self.sol[i-1][j-1] = self.sol[i-1][j] = self.sol[i-1][j+1] = 1
                        self.sol[i][j-1] = self.sol[i+1][j-1] = 1
                        self.sol[i+2][j] = self.sol[i+2][j+1] = self.sol[i+2][j+2] = 10
                        self.sol[i+1][j+2] = self.sol[i][j+2] = 10
                    if self.task[i][j] - 5 == self.task[i-1][j-1]:    # лево верх
                        if self.test_mode:
                            print(3, i, j, 3)
                        self.sol[i-1][j+1] = self.sol[i][j+1] = self.sol[i+1][j+1] = 1
                        self.sol[i+1][j-1] = self.sol[i+1][j] = 1
                        self.sol[i][j-2] = self.sol[i-1][j-2] = self.sol[i-2][j-2] = 10
                        self.sol[i-2][j-1] = self.sol[i-2][j] = 10
                    if self.task[i][j] - 5 == self.task[i+1][j-1]:    # лево низ
                        if self.test_mode:
                            print(4, i, j, 4)
                        self.sol[i-1][j+1] = self.sol[i][j+1] = self.sol[i+1][j+1] = 1
                        self.sol[i-1][j-1] = self.sol[i-1][j] = 1
                        self.sol[i][j-2] = self.sol[i+1][j-2] = self.sol[i+2][j-2] = 10
                        self.sol[i+2][j-1] = self.sol[i+2][j] = 10
                    
        # ситуация 4
        for i in range(2, self.n - 2):
            for j in range(2, self.m - 2):
                if self.task[i][j] == 8:
                    if self.task[i-2][j+1] == 1:    # 1
                        if self.test_mode:
                            print(4, i, j, 1)
                        self.sol[i-1][j-1] = 1
                        self.sol[i][j-1] = self.sol[i][j] = self.sol[i][j+1] = 1
                        self.sol[i+1][j-1] = self.sol[i+1][j] = self.sol[i+1][j+1] = 1
                        self.sol[i-3][j] = self.sol[i-3][j+1] = self.sol[i-3][j+2] = 10
                        self.sol[i-2][j] = self.sol[i-2][j+1] = self.sol[i-2][j+2] = 10
                        self.sol[i-1][j+2] = 10
                    if self.task[i-1][j+2] == 1:    # 2
                        if self.test_mode:
                            print(4, i, j, 2)
                        self.sol[i-1][j-1] = self.sol[i][j-1] = self.sol[i+1][j-1] = 1
                        self.sol[i-1][j] = self.sol[i][j] = self.sol[i+1][j] = 1
                        self.sol[i+1][j+1] = 1
                        self.sol[i-2][j+1] = 10
                        self.sol[i][j+2] = self.sol[i-1][j+2] = self.sol[i-2][j+2] = 10
                        self.sol[i][j+3] = self.sol[i-1][j+3] = self.sol[i-2][j+3] = 10
                    if self.task[i+1][j+2] == 1:    # 3
                        if self.test_mode:
                            print(4, i, j, 3)
                        self.sol[i-1][j-1] = self.sol[i][j-1] = self.sol[i+1][j-1] = 1
                        self.sol[i-1][j] = self.sol[i][j] = self.sol[i+1][j] = 1
                        self.sol[i-1][j+1] = 1
                        self.sol[i+2][j+1] = 10
                        self.sol[i][j+2] = self.sol[i+1][j+2] = self.sol[i+2][j+2] = 10
                        self.sol[i][j+3] = self.sol[i+1][j+3] = self.sol[i+2][j+3] = 10
                    if self.task[i+2][j+1] == 1:    # 4
                        if self.test_mode:
                            print(4, i, j, 4)
                        self.sol[i-1][j-1] = self.sol[i-1][j] = self.sol[i-1][j+1] = 1
                        self.sol[i][j-1] = self.sol[i][j] = self.sol[i][j+1] = 1
                        self.sol[i+1][j-1] = 1
                        self.sol[i+1][j+2] = 10
                        self.sol[i+2][j] = self.sol[i+2][j+1] = self.sol[i+2][j+2] = 10
                        self.sol[i+3][j] = self.sol[i+3][j+1] = self.sol[i+3][j+2] = 10
                    if self.task[i+2][j-1] == 1:    # 5
                        if self.test_mode:
                            print(4, i, j, 5)
                        self.sol[i-1][j-1] = self.sol[i-1][j] = self.sol[i-1][j+1] = 1
                        self.sol[i][j-1] = self.sol[i][j] = self.sol[i][j+1] = 1
                        self.sol[i+1][j+1] = 1
                        self.sol[i+1][j-1] = 10
                        self.sol[i+2][j-1] = self.sol[i+2][j] = self.sol[i+2][j+1] = 10
                        self.sol[i+3][j-1] = self.sol[i+3][j] = self.sol[i+3][j+1] = 10
                    if self.task[i+1][j-2] == 1:    # 6
                        if self.test_mode:
                            print(4, i, j, 6)
                        self.sol[i-1][j+1] = self.sol[i][j+1] = self.sol[i+1][j+1] = 1
                        self.sol[i-1][j] = self.sol[i][j] = self.sol[i+1][j] = 1
                        self.sol[i-1][j-1] = 1
                        self.sol[i+2][j-1] = 10
                        self.sol[i+2][j-2] = self.sol[i+1][j-2] = self.sol[i][j-2] = 10
                        self.sol[i+2][j-3] = self.sol[i+1][j-3] = self.sol[i][j-3] = 10
                    if self.task[i-1][j-2] == 1:    # 7
                        if self.test_mode:
                            print(4, i, j, 7)
                        self.sol[i-1][j+1] = self.sol[i][j+1] = self.sol[i+1][j+1] = 1
                        self.sol[i-1][j] = self.sol[i][j] = self.sol[i+1][j] = 1
                        self.sol[i+1][j-1] = 1
                        self.sol[i-2][j-1] = 10
                        self.sol[i-2][j-2] = self.sol[i-1][j-2] = self.sol[i][j-2] = 10
                        self.sol[i-2][j-3] = self.sol[i-1][j-3] = self.sol[i][j-3] = 10
                    if self.task[i-2][j-1] == 1:    # 8
                        if self.test_mode:
                            print(4, i, j, 8)
                        self.sol[i][j-1] = self.sol[i][j] = self.sol[i][j+1] = 1
                        self.sol[i+1][j-1] = self.sol[i+1][j] = self.sol[i+1][j+1] = 1
                        self.sol[i-1][j+1] = 1
                        self.sol[i-1][j-2] = 10
                        self.sol[i-3][j] = self.sol[i-3][j-1] = self.sol[i-3][j-2] = 10
                        self.sol[i-2][j] = self.sol[i-2][j-1] = self.sol[i-2][j-2] = 10
        
    def run(self):                      # основной алгоритм 
        fl = True
        while fl:
            fl = False

            # обработка на число свободных клеток
            for i in range(1, self.n - 1):
                for j in range(1, self.m - 1):
                    if self.task[i][j] > 0:
                        k, z = divmod(self.sum(i, j), 10)
                        if k + z == 9:                  # все клетки обработаны
                            # self.task[i][j] = - self.task[i][j] - 10
                            continue
                        if z == self.task[i][j]:        # всё что должно быть закрашено уже закрашено
                            self.fill(i, j, 10)
                            # self.task[i][j] = - self.task[i][j] - 10
                            fl = True
                        if 9 - k == self.task[i][j]:    # всё что свободно должно быть закрашено
                            self.fill(i, j, 1)
                            # self.task[i][j] = - self.task[i][j] - 10
                            fl = True

            if fl and not(self.full()) and self.test_mode:
                self.printst()
        
        if self.full() and self.check():
            return 'Задача успешно решена'
        
        return 'Решение не найдено'
