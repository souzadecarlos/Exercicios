
# Your job in this problem is to read a number that is a column of an array where an operation will be performed,
# an uppercase character, indicating the operation to be performed and all elements of a bidimentional array M[12][12].
# Then, you have to calculate and print the sum or average of all elements within the green area according to the case.
# The following figure illustrates the case when is entered the number 5 to the array column,
# showing all elements that must be considered in the operation.

# Input
# The first line of the input contains a simple integer C (0 ≤ C ≤ 11) indicating the column to be
# considered in the operation. The second line of the input contains a single uppercase character T ('S' or 'M'),
# indicating the operation Sum or Average (Média in portuguese) to be performed with the elements of the array.
# Follow 144 floating-point numbers of the array.

C = int(input())
T = str(input())
matriz = []
calc = []


for j in range(0,12):
    linha = []
    for i in range (0,12):
        a = float(input())
        linha.append(a)
    matriz.append(linha)

for i in range(0,12):
    calc.append(matriz[i][C])

if T == 'S':
    print('{0:.1f}'.format(sum(calc)))
if T == 'M':
    print('{0:.1f}'.format(sum(calc)/len(calc)))
