print('='* 50 + ' Запрос 1 ' + '='*50)

GREEN = '\u001b[42m'
YELLOW ='\u001b[43m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
BRIGHtPINK = '\u001b[48;5;217m'
BRIGHTGRAY = '\u001b[48;5;241m'
END = '\u001b[0m'

def flag_sz():
    for i in range(3):
        print(GREEN + '  ' * 6 + YELLOW + '  ' * 8 + END )
    for j in range(3):
        print(GREEN + '  ' * 6 + RED + '  ' * 8 + END)

flag_sz()
print('='* 50 + ' Запрос 2 ' + '='*50)

for i in range(8):
    print(WHITE + " "*(14-2*i) + BLACK  + " " * (4 + 4*i) + WHITE + " " * (28 - 4 * i) + BLACK  + " " * (4 + 4*i) + WHITE + " " * (14 - 2*i) +  END)
for i in range(8):
    print(WHITE + " " * (2*i) + BLACK  + " " * (32 - 4*i) + WHITE + " " * (4*i) + BLACK + " " * (32 - 4*i) +  WHITE + " " * (2*i)  +  END )


print('='* 50 + ' Запрос 3 ' + '='*50)

array_graphic = [[0 for row in range(10)] for col in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i + 1
print(result)

def arr_init(arr_in, ste):
    for i in range(9):
        for j in range(10):
            if j == 0:
                arr_in[i][j] = round((ste * (9 - i)),1)
    return arr_in
#
def arr_fill(arr_fi, re, ste):
    for i in range(9):
        for j in range(10):
            if i != 8:
                if abs(arr_fi[i][0] - re[j]) < ste:
                    arr_fi[i][j+1] = 1
                if i == 8:
                    arr_fi[9][j] = j
    return arr_fi

def graphic_color(color):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(color[i][j])
            if color[i][j] == 0:
                line += '  '
            if color[i][j] == 1 and i != 8 and j != 1:
                line += RED + '  ' + WHITE
            if color[i][j] == 1 and i == 8 and j == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0 1 2 3 4 5 6 7 8 9' + END)

arr_init(array_graphic,1)
arr_fill(array_graphic, result, 1)
graphic_color(array_graphic)

for i in range(10):
        print(array_graphic[i])

print('='* 50 + ' Запрос 4 ' + '='*50)

book = open('booksnew.csv','r', encoding='windows-1251')
header = book.readline()
lineBook = list(book)

count1 = 0
count2 = 0
for line in lineBook:
    lineB = line.split(';')
    floatPrice = float(lineB[7])
    if floatPrice <= 150.0:
        count1 += 1
    if floatPrice > 150.0:
        count2 +=1
percentLessOrEqual = round((count1 * 100)/len(lineBook),0)
percentGreaterThan = round((count2 * 100)/len(lineBook),0)

print("Процент книг с ценой меньше или равной 150руб: ",percentGreaterThan, "%")
print("Процент книг с ценой выше 150руб: ", percentLessOrEqual, "%")
def arr_y(arr_in, ste):
    for i in range(7):
        for j in range(7):
            if j == 0:
                arr_in[i][0] = round(ste*(7-i))
    return arr_in

def arr_fill(arr_fi, re, ste):
    for i in range(7):
        for j in range(2):
            if j == 0:
                if arr_fi[i][0] - re[j] < ste:
                    for k in range(6):
                        if k == 0 or k == 2 or k == 3 or k == 4 or k == 5:
                            arr_fi[i][k+1] = 0
                        else: arr_fi[i][k+1] = 1
            if j == 1:
                if arr_fi[i][0] - re[j] < ste:
                    for k in range(6):
                        if k == 0 or k == 2 or k == 3 or k == 5:
                            arr_fi[i][k + 1] = 0
                        else: arr_fi[i][k + 1] = 1

    return arr_fi

def graphicColor(arr_i):
    for i in range(7):
        line = ''
        for j in range(7):
            if j == 0:
                line += BRIGHTGRAY + str(arr_i[i][j])
            if arr_i[i][j] == 0:
                line += '  '
            elif arr_i[i][j] == 1:
                line += BRIGHtPINK + '  ' + BRIGHTGRAY
        line += END
        print(line)
    print(WHITE + '0 <=150  >150 ' + END)


arr_xy = [[0 for col in range(7)] for row in range(7)]
result = [0 for i in range(0)]

result.append(percentLessOrEqual)
result.append(percentGreaterThan)
arr_y(arr_xy,10)
arr_fill(arr_xy, result,10)
graphicColor(arr_xy)

for i in range(7):
    print(arr_xy[i])

print('='* 50 + 'Допзадание' + '='*50)












