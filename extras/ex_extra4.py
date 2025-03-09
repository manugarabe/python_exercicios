import math
x = int(input('Insira o primeiro valor '))
y = int(input('Insira o segundo valor '))
mv1 = (x + y + (math.fabs(x)-(math.fabs(y))))/2
print(mv1)