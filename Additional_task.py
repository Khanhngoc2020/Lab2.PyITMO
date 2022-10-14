import os
import sys
from time import sleep

arr_xy = [[0 for col in range(23)] for row in range(9)]
BRIGHTPINK = '\u001b[48;5;217;5m'
BRIGHTGRAY = '\u001b[48;5;241;5m'
END = '\u001b[0m'

for i in range(8):
    for j in range(23):
            arr_xy[i][0] = 1
            arr_xy[4][1] = 1
            arr_xy[i][2] = 1
            if j == 4 and i != 1:
                arr_xy[i][4] = 1
            arr_xy[i][7] = 1
            if  j == 8:
                if i == 0 or i == 1:
                    arr_xy[i][8] = 1
            arr_xy[2][9] = 1
            arr_xy[i][10] = 1
            arr_xy[i][12] = 1
            if j == 13:
                if i == 0 or i == 5 or i == 7:
                    arr_xy[i][j] = 1
            if j == 14:
                if i == 0 or i == 5 or i == 6 or i == 7:
                    arr_xy[i][j] = 1
            if j == 15:
                if i == 5:
                    arr_xy[i][j] = 1
            arr_xy[i][16] = 1
            if j == 17:
                if i == 0 or i == 7:
                    arr_xy[i][j] = 1
            arr_xy[i][18] = 1
            arr_xy[i][20] = 1
            if j == 21:
                if i == 0 or i == 7:
                    arr_xy[i][j] = 1
            if j == 22:
                if i == 0 or i == 7:
                    arr_xy[i][j] = 1

def color (arr_in):
    for i in range(9):
        line = '  '
        for j in range(23):
            if arr_in[i][j] == 1:
                if i == 0 and j == 8:
                    line += BRIGHTPINK  + ' ' + END + ' '
                elif i == 5 and j == 13:
                    line += ' ' + BRIGHTPINK  + ' ' + END
                elif i == 5 and j == 15:
                    line += BRIGHTPINK  + ' ' + END +  ' '
                else:
                    line += BRIGHTPINK + '  ' + END
            elif arr_in[i][j] == 0: line += '  '
        line += END
        print(line)

for i in range(3):
        color(arr_xy)
        sleep(0.5)
        os.system('cls')
        sleep(0.5)
