n1 = int(input(' Digite o primeiro valor: '))
n2 = int(input(' Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print(''' Opções:
    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do programa 
    [6] Divisão''')
    opcao = int(input(' Digite sua opção: '))
    if opcao == 1:
        print(f' A soma dos valores é de {n1 + n2}! ')
    elif opcao == 2:
        print(f' A multiplicação entre o s valores é de {n1 * n2}! ')
    elif opcao == 3:
        if n1 < n2:
            print(f' {n2} é maior que {n1}! ')
        elif n1 > n2:
            print(f' {n1} é maior que {n2}! ')
        else:
            print(' Os valores são iguais! ')
    if opcao == 4:
        print(' Informe seus novos valores: ')
        n1 = int(input(' Digite seu novo primeiro valor: '))
        n2 = int(input(' Digite seu segundo valor: '))
    if opcao == 6:
        print(f'A divisão entre os valores é de {n1 / n2}')
print(' Você saiu do programa! ')
