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

print("Процент книг с ценой выше  150руб: ",percentGreaterThan, "%")
print("Процент книг с ценой меньше или равной 150руб: ", percentLessOrEqual, "%")
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





