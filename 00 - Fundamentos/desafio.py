menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Função para realizar depósito
def depositar(saldo, extrato):
    valor = float(input("Informe o valor de depósito: ")) # Captura valor de deposito
    if valor > 0:
        saldo += valor  # Atualiza o saldo com o valor do depósito
        extrato += f"Depósito: R$ {valor:.2f}\n" # Adciona o depósito ao extrato
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar saque
def sacar(saldo, limite, numero_saques, LIMITE_SAQUE, extrato):
    valor = float(input("Informe o valor do saque: ")) #Captura o valor do saque
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print(f"Operação falhou! O valor do saque execede o limite de R$ {limite}.") 
    elif numero_saques >= LIMITE_SAQUE:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor # Atualiza o saldo decontando o valor do saque
        extrato += f"Saque: R$ {valor:.2f}\n" # Adicona o saque ao extrato
        numero_saques += 1 # Incrementar o contador de saques
        print("Saque realizado com sucesso!")
    else:
        print("Operacação falhou! O valor informado é inválido.")
    return saldo, numero_saques, extrato

# Função para exibir extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}") # Exibe o saldo atual
    print("==========================================")
    
# Loop principal que mantém o programa em execução
while True:

    opcao = input(menu)

    # Chama a função de depósito
    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    # Chama a função de saque
    elif opcao == "s":
        saldo, numero_saques, extrato = sacar(saldo, limite, numero_saques, LIMITE_SAQUES, extrato)

# Chama a função de exibir extrato
    elif opcao == "e":
        exibir_extrato(saldo, extrato)
        
# Finalização de programa
    elif opcao == "q":
        print("Obrigado por usar o sistema bancário!")
        break

# Tratamento de entradas inválidas
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
