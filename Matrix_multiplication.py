print("Введите количество строк и столбцов первой матрицы через пробел" )
size1=input()
size1=size1.split()
matrix1=[]
print("Построчно через пробел введите элементы первой матрицы")
for i in range (int(size1[0])):
    line=input()
    line=line.split()
    matrix1.append(line)

print("Введите количество строк и столбцов второй матрицы через пробел" )
size2=input()
size2=size2.split()
matrix2=[]
print("Построчно через пробел введите элементы второй матрицы")
for j in range (int(size2[0])):
    line=input()
    line=line.split()
    matrix2.append(line)

if (size1[1]!=size2[0]):
    print("Невозможно произвести действие")
    exit(0)

for k in range (int(size1[0])):
    line=''
    for t in range (int(size2[1])):
        res=0
        for g in range (int(size1[1])):
            res+=float(matrix1[k][g])*float(matrix2[g][t])
        line+=str(res)
        if t!=(int(size2[1])-1):
            line+=' '
    print(line)
            