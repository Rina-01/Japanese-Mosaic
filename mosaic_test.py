chr(9632)
chr(9608)
chr(9747)
chr(32)

s = chr(9474) + chr(9608) * 2 + chr(9587) * 2 + chr(9608) * 2 + chr(9587) * 2 + chr(9474)
s

print(chr(9472),chr(9474), chr(9484),chr(9488), chr(9492),chr(9496))

for a in range(9470,9500):
    print(a, chr(a))

n = 5
m = 3

s = chr(9484) + chr(9472) * m + chr(9488)
s = chr(9492) + chr(9472) * m + chr(9496)


ss = 34
res = divmod(ss, 10)
res
a,b = divmod(ss, 10)


for a in (False, True):
    for b in (False, True):
        print(int(a), int(b), int(a and not(b)))



import numpy as np
from JapaneseMosaic import JapaneseMosaic

dir_name = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"
file_name = '10-15 1'

test = JapaneseMosaic()
test.task_load(dir_name + "\\task_files\\" + file_name + ".npy")
test.printsol()




import numpy as np
dir_name = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"
file_name = 'test-sit 2'

  
def sum(i, j):
    if i*j == 0 or i == n-1 or j == m-1:
        return 0
    return sol[i-1][j-1] + sol[i-1][j] + sol[i-1][j+1] + sol[i][j-1] + sol[i][j] + sol[i][j+1] + sol[i+1][j-1] + sol[i+1][j] + sol[i+1][j+1]

def fill(i, j, c):
    if sol[i-1][j-1] == 0:
        sol[i-1][j-1] = c
    if sol[i-1][j] == 0:
        sol[i-1][j] = c
    if sol[i-1][j+1] == 0:
        sol[i-1][j+1] = c
    
    if sol[i][j-1] == 0:
        sol[i][j-1] = c
    if sol[i][j] == 0:
        sol[i][j] = c
    if sol[i][j+1] == 0:
        sol[i][j+1] = c
    
    if sol[i+1][j-1] == 0:
        sol[i+1][j-1] = c
    if sol[i+1][j] == 0:
        sol[i+1][j] = c
    if sol[i+1][j+1] == 0:
        sol[i+1][j+1] = c
    
def printsol():
    print(chr(9484) + chr(9472) * (m - 2) + chr(9488))
    for i in range(1, n-1):
        s = chr(9474)
        for j in range(1, m-1):
            if sol[i][j] == 1:         # закрашенное
                s += chr(9608)
            elif sol[i][j] == 10:      # крест
                s += chr(9587)
            else:
                s += ' '
        s += chr(9474)
        print(s)
    print(chr(9492) + chr(9472) * (m - 2) + chr(9496))

def printst():
    print(chr(9484) + chr(9472) * (m - 2) + chr(9488) + '     ' + chr(9484) + chr(9472) * (m - 2) + chr(9488))
    for i in range(1, n-1):
        s = chr(9474)
        for j in range(1, m-1):
            if sol[i][j] == 1:         # закрашенное
                s += chr(9608)
            elif sol[i][j] == 10:      # крест
                s += chr(9587)
            else:
                s += ' '
        s += chr(9474)
        
        s += '     ' 
        s += chr(9474)
        for j in range(1, m-1):
            if task[i][j] == -5:        # ничего нет
                s += '_'
            elif task[i][j] > 0:        # число
                s += str(task[i][j])
            else:                       # было число
                s += str(-task[i][j] - 10)
        s += chr(9474)
        print(s)
    print(chr(9492) + chr(9472) * (m - 2) + chr(9496) + '     ' + chr(9492) + chr(9472) * (m - 2) + chr(9496))
    

task = np.load(dir_name + "\\task_files\\" + file_name + ".npy")
n = len(task)
m = len(task[0])

sol = np.zeros((n, m), int)
for i in range(n):
    sol[i][0] = sol[i][m-1] = 10
for j in range(m):
    sol[0][j] = sol[n-1][j] = 10



# первичная обработка

# обработка 0 и 9
for i in range(2, n - 2):
	for j in range(2, m - 2):
		if task[i][j] == 0:
			fill(i, j, 10)
			task[i][j] = -task[i][j] - 10
		if task[i][j] == 9:
			fill(i, j, 1)
			task[i][j] = -task[i][j] - 10


# обработка на различные ситуации

# ситуация 1
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if task[i][j] > 0:
            if task[i][j] - 3 == task[i-1][j]:    # верх
                print(i, j, 1)
                sol[i-2][j-1] = sol[i-2][j] = sol[i-2][j+1] = 10
                sol[i+1][j-1] = sol[i+1][j] = sol[i+1][j+1] = 1
                printsol()
            if task[i][j] - 3 == task[i+1][j]:    # низ
                print(i, j, 2)
                sol[i-1][j-1] = sol[i-1][j] = sol[i-1][j+1] = 1
                sol[i+2][j-1] = sol[i+2][j] = sol[i+2][j+1] = 10
                printsol()
            if task[i][j] - 3 == task[i][j+1]:    # право
                print(i, j, 3)
                sol[i-1][j-1] = sol[i][j-1] = sol[i+1][j-1] = 1
                sol[i-1][j+2] = sol[i][j+2] = sol[i+1][j+2] = 10
                printsol()
            if task[i][j] - 3 == task[i][j-1]:    # лево
                print(i, j, 4)
                sol[i-1][j+1] = sol[i][j+1] = sol[i+1][j+1] = 1
                sol[i-1][j-2] = sol[i][j-2] = sol[i+1][j-2] = 10
                printsol()

printst()

# ситуация 2
for i in range(2, n - 2):
    for j in range(2, m - 2):
        if task[i][j] == 8 or task[i][j] == 7:
            if task[i][j] - 6 == task[i-2][j]:    # верх
                print(i, j, 1)
                sol[i][j-1] = sol[i][j] = sol[i][j+1] = 1
                sol[i+1][j-1] = sol[i+1][j] = sol[i+1][j+1] = 1
                sol[i-3][j-1] = sol[i-3][j] = sol[i-3][j+1] = 10
                sol[i-2][j-1] = sol[i-2][j] = sol[i-2][j+1] = 10
                printsol()
            if task[i][j] - 6 == task[i+2][j]:    # низ
                print(i, j, 2)
                sol[i-1][j-1] = sol[i-1][j] = sol[i-1][j+1] = 1
                sol[i][j-1] = sol[i][j] = sol[i][j+1] = 1
                sol[i+2][j-1] = sol[i+2][j] = sol[i+2][j+1] = 10
                sol[i+3][j-1] = sol[i+3][j] = sol[i+3][j+1] = 10
                printsol()
            if task[i][j] - 6 == task[i][j+2]:    # право
                print(i, j, 3)
                sol[i-1][j-1] = sol[i][j-1] = sol[i+1][j-1] = 1
                sol[i-1][j] = sol[i][j] = sol[i+1][j] = 1
                sol[i-1][j+2] = sol[i][j+2] = sol[i+1][j+2] = 10
                sol[i-1][j+3] = sol[i][j+3] = sol[i+1][j+3] = 10
                printsol()
            if task[i][j] - 6 == task[i][j-2]:    # лево
                print(i, j, 4)
                sol[i-1][j+1] = sol[i][j+1] = sol[i+1][j+1] = 1
                sol[i-1][j] = sol[i][j] = sol[i+1][j] = 1
                sol[i-1][j-2] = sol[i][j-2] = sol[i+1][j-2] = 10
                sol[i-1][j-3] = sol[i][j-3] = sol[i+1][j-3] = 10
                printsol()


# цикл

fl = False      # флаг, что была закрашена хотя бы одна клетка

# обработка на число свободных клеток
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if task[i][j] > 0:
            k, z = divmod(sum(i, j), 10)
            if k + z == 9:
                continue
            if z == task[i][j]:    # всё что должно быть закрашено уже закрашено
                fill(i, j, 10)
                task[i][j] = -task[i][j] - 10
                fl = True
            if 9 - k == task[i][j]:    # всё что свободно должно быть закрашено
                fill(i, j, 1)
                task[i][j] = -task[i][j] - 10
                fl = True

if fl:
    printsol()

