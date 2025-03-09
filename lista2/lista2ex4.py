t1 = float(input('Insira a nota da prova parcial 1: '))
ativ1 = float(input('Insira a nota das atividades de sala 1: '))
lab1 = float(input('Insira a nota das atividades de laboratório 1: '))
proj1 = float(input('Insira a nota do projeto de laboratório 1: '))
t2 = float(input('Insira a nota da prova parcial 2: '))
ativ2 = float(input('Insira a nota das atividades de sala 2: '))
lab2 =  float(input('Insira a nota das atividades de laboratório 2: '))
proj2 = float(input('Insira a nota do projeto de laboratório 2: '))

n1 = (t1*0.65) + (ativ1*0.05) + (lab1*0.1) + (proj1*0.2)
n2 = (t2*0.65) + (ativ2*0.05) + (lab2*0.1) + (proj2*0.2)
mi = (n1+n2)/2
rn1 = round(n1, 2)
rn2 = round(n2, 2)
rmi = round(mi, 2)

print('Nota N1: {}, Nota N2: {}, MI: {}'.format(rn1, rn2, rmi))

if mi >= 6:
    print('Aprovado!')
else:
    print('Reprovado.')