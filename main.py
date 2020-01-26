from getch import getch
import sys
import os

target = open('source.txt', 'r')

os.system('clear')

for i in target.readlines():
    for j in [i[k:k + 4] for k in range(0, len(i), 4)]:
        getch()

        sys.stdout.write(j)
        sys.stdout.flush()
