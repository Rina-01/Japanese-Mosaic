import numpy as np
from JapaneseMosaic import JapaneseMosaic

dir_name = r"C:\Users\irina.mashkova\Documents\GitHub\Japanese-Mosaic"
file_name = '10-15 1'

test = JapaneseMosaic()
test.task_load(dir_name + "\\task_files\\" + file_name + ".npy")
test.print()


chr(9632)
chr(9608)
chr(9747)
chr(32)


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