while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numero_1 = float(numero_1)
    numero_2 = float(numero_2)

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operador_permitidos = '+-/*'

    if operador not in operador_permitidos:
        print('Operador inválido.')

    elif len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    elif operador is '+':
        soma = numero_1 + numero_2
        print (f' A somatória de {numero_1} + {numero_2} é {soma}')
    
    elif operador is '-':
        subtracao = numero_1 - numero_2
        print (f' A subtração de {numero_1} - {numero_2} é {subtracao}')

    elif operador is '/':
        divisao = numero_1 + numero_2
        print (f' A divisão de {numero_1} / {numero_2} é {divisao}')

    elif operador is '*':
        multi = numero_1 + numero_2
        print (f' A multiplicação de {numero_1} * {numero_2} é {multi}')
        

    sair = input ('Quer sair: [s]im: ').lower().startswith('s')

    if sair is True:
        break
