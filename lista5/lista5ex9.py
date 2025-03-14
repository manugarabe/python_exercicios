altura = float(input('Insira a altura: '))
peso = float(input('Insira o peso: '))

imc = peso / (altura**2)

if imc >= 0 and imc <=19:
    print('Muito magro')
    
elif imc >= 20 and imc <=25:
 print('Normal')

elif imc >= 26 and imc <= 30:
   print('Sobrepeso')

elif imc >= 31 and imc <= 40:
   print('Obeso')

elif imc >= 41:
   print('Obesidade grave')