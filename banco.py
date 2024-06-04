def mostrar_saldo():
    print(f'Seu saldo é de R$ {saldo:.2f}')

def deposito():
   quantia = float(input('Digite o Valor a ser depositado: '))
   
   if quantia < 0:
       print('Isso não é uma entrada válida!')
   else:
       return quantia

def saque():
    quantia = float(input('Digite o Valor a ser sacado: '))
   
    if quantia > saldo:
       print('Dinheiro insuficiente para realizar o saque. digite um valor menor!')
    elif quantia < 0:
       print('O valor deve ser maior do que R$0.00')
    else:
        return quantia

saldo = 0
funcional = True

while funcional:
    print('MENU DO PROGRAMA')
    print('1. VER EXTRATO')
    print('2. DEPOSITAR VALOR')
    print('3. SACAR VALOR')
    print('4. SAIR')
    
    opcao = input('Escolha uma opção de 1 a 4: ')
    if opcao == '1':
        mostrar_saldo()
    elif opcao == '2':
        saldo += deposito()
    elif opcao == '3':
        saldo -= saque()
    elif opcao == '4':
        funcional = False
    else:
        print('Entrada inválida, digite um valor de 1 a 4 especificado no menu!')
        
print("Obrigado e volte sempre!")
        