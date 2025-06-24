menu = """
============ MENU =============
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
===============================
=> """

saldo = 0
limite = 500
usuarios = [] # lista para armazenar os usuários
contas = [] # Armazena contas
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Função para realizar depósito
def depositar(saldo, extrato, /): # depósito com positional only
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
      print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# Função para realizar saque
def sacar (*, saldo, limite, numero_saques, LIMITE_SAQUES, extrato): # sacar com keyword only
    valor = float(input("informe o valor do saque: "))
    
    # Verifica a eligibilidade do saque
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")    
    elif valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente")
    elif valor > limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques diários excedidos.")
  
   
    # Se todas as verificações forem realizadas corretamente
    else:
        saldo -= valor # Atualiza o saldo descontando o valor do saque.
        extrato += f"Saque: R$ {valor:.2f}\n" # Adiciona o saque ao extrato.
        numero_saques += 1 # Atualiza o número de saques permitidos
    
        print("Saque realizado com sucesso!") # Mensagem de confirmação de saques
    return saldo, numero_saques, extrato

# Função para exibir extrato
def exibir_extrato(saldo, /, *, extrato, usuario, conta): # Exibe extrato com positional e keyword only
    print("\n================ DADOS DO CLIENTE ================")
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Endereço: {usuario['endereco']}")
    print(f"Agência: {conta['agencia']}")
    print(f"Número da Conta: {conta['numero']}")
    
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}") #Vai exibir o saldo atual.
    print("==========================================")

# Busca usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
        return None
    
# retorna uma lista de contas associadas a um CPF
def filtrar_contas_por_cpf(cpf, contas):
    contas_filtradas = []    
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            contas_filtradas.append(conta)
            return contas_filtradas

# Listar Contas Cadastradas
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada no sitema.")
        return
    
    print("\n============ LISTA DE CONTAS ============")
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Títular: {conta['usuario']['nome']}")
    print("===========================================")
    
# Criar um novo usuário (cliente)    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números): ").strip()
    if filtrar_usuario(cpf, usuarios):
        print("Usuário com este CPF já existe!")
        return
    
    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (dd-mm-aaaaa): ").strip()
    logradouro = input("Logradouro: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("UF: ").strip().upper()
    
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")
    
# Cria nova conta vinculada a um usuário existente
def criar_conta(*, agencia="0001", usuarios, contas):    
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return
    
    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato":"",
        "numero_saques": 0
    })
    print(f"Conta criada com sucesso! Agência: {agencia}, Número: {numero_conta}")
    
    

# Loop principal para manter o programa em execução
while True:

    opcao = input(menu)

    # Chama a função de depósito
    if opcao == "d":
        cpf = input("Informe o CPF do titular da conta para depósito: ").strip()
        contas_usuario = filtrar_contas_por_cpf(cpf, contas)
        
        if not contas_usuario:
            print("Nenhuma conta encontrada para este CPF.")
            print("Você pode criar uma conta para começar a depositar.")
            
        else:
            # Aqui escolhemos a primeira conta do CPF encontrado (poderia ter a opção de escolher se quiser)    
            print(f"Depositando na conta número {contas_usuario[0]['numero']}")
            saldo, extrato = depositar(saldo, extrato)
        
    # Chama a função de saque
    elif opcao == "s":
        cpf = input("Informe o CPF do titular da conta para saque: ").strip()
        
        if not cpf:
            print("Nenhum CPF informado.")
            print("Encerrando o sistema. Obrigado por utilizar nosso sistema!")
            break
        
        contas_usuario = filtrar_contas_por_cpf(cpf, contas) 
        
        # Verifica se existe conta senão houver encerra o programa
        if not contas_usuario: 
            print("Nenhuma conta encontrada para este CPF.")
            print("Você deve criar uma conta antes de realizar saques.")
            print("Obrigado por utilizar nosso sistema bancário!")
            continue
            
    
        print(f"Realizando saque da conta número {contas_usuario[0]['numero']}")
        saldo, numero_saques, extrato = sacar(
            saldo=saldo, 
            limite=limite,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES,
            extrato=extrato
        )
    
    # Chama a função de exibir o extrato
    elif opcao == "e":
        cpf = input("Informe o CPF do titular da conta: ").strip()
        contas_usuario = filtrar_contas_por_cpf(cpf, contas)
        
        if not contas_usuario:
            print("Nenhuma conta encontrada neste CPF.")
            print("Você deve criar uma conta para consultar o extrato.")
        else:
            # Se houver mais de uma conta, futuramente pode expandir para escolher;
            conta_selecionada = contas_usuario[0]
            usuario = conta_selecionada["usuario"]
            exibir_extrato(saldo ,extrato=extrato, usuario=usuario, conta=conta_selecionada)
    
    # Chama função de criar novo usuário    
    elif opcao == "nu":
        criar_usuario(usuarios)
            
    # Chama a função de criar nova conta
    elif opcao == "nc":
        criar_conta(usuarios=usuarios, contas=contas)
        
    # Chama a função de listar contas
    elif opcao == "lc":
        listar_contas(contas)
        
    # Finaliza o programa
    elif opcao == "q":
        print("Obrigado por usar o sistema bancário!")
        break


    # Trata de entradas inválidas    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")