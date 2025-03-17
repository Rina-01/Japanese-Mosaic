from JapaneseMosaic import JapaneseMosaic

DIR_NAME = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"
FILE_NAME = '10-15 3'

objs = []
index = 0

# COUNT = 0


def recursion(i, j, c):
    global index
    global objs
    
    # global COUNT
    # COUNT += 1
    # if COUNT > 100:
    #     return
    # print('COUNT =', COUNT)
    
    index += 1
    objs.append(JapaneseMosaic(test_mode=False))
    objs[index].hand_init(task=objs[0].task, solution=objs[index-1].sol, ni=i, nj=j)
    
    print(index, i, j, '  ', objs[index].sol[i][j], c)
    objs[index].sol[i][j] = c
    
    go = objs[index].run()
    
    if go == 'Задача успешно решена':
        print(go)
        objs[index].printsol()
        return
    
    pr = objs[index].check()
    
    if pr[0] == 0:
        ii, jj = objs[index].empty()
        print('Пробуем дальше с', ii, jj)
        recursion(ii, jj, 1)
        recursion(ii, jj, 10)
    else:
        print('Возвращаемся')
        objs.pop()
        index -= 1
        if c != 10:
            recursion(i, j, 10)



objs.append(JapaneseMosaic(test_mode=False))
a = objs[0].task_load(DIR_NAME + "\\task_files\\" + FILE_NAME + ".npy")
print(a)

if a != 'Успешно':
    exit()

a = objs[0].run()
a

if a == 'Задача успешно решена':
    objs[0].printsol()
else:
    i, j = objs[0].empty()
    recursion(i, j, 1)

print()
print('last -', objs[index].i, objs[index].j)
objs[index].printsol()

# a = objs[index].sol_load(DIR_NAME + "\\sol_files\\" + FILE_NAME + ".npy")
# a

# objs[index].save(DIR_NAME + "\\sol_files\\" + FILE_NAME)


