from getch import getch
import sys
import os

target = open('source.txt', 'r')

os.system('clear')

for i in target.readlines():
    for j in i:
        getch()

        sys.stdout.write(j)
        sys.stdout.flush()
