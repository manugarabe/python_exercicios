idade = int(input('Insira a idade: '))
tempo = int(input('Insira o tempo de serviço em anos: '))

if idade >= 65 or tempo >= 30 or idade >=60 and tempo >= 25:
    print("Está apto para se aposentar.")
else: 
    print('Não está apto para se aposentar.')