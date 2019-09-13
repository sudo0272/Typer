from getch import getch
import sys

target = open('source.txt', 'r')

for i in target.readlines():
    for j in i:
        getch()

        sys.stdout.write(j)
        sys.stdout.flush()
