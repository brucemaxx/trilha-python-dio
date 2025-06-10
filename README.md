# Trilha Python DIO
## Sistema Bancário em Python 🏦
Descrição Este é um projeto de um sistema bancário desenvolvido em Python, que permite aos usuários realizar operações simples como depósito, saque e exibição de extrato. Foi projetado como parte de um desafio para modernizar as operações bancárias com foco na simplicidade e eficiência.

## 📜 Funcionalidades
Depósito: Permite o depósito de valores positivos, atualizando o saldo e registrando no extrato.

Saque: Realiza saques limitados a 3 operações diárias, com um valor máximo de R$ 500,00 por saque. Valida saldo e limites antes da execução.

Extrato: Exibe todos os depósitos e saques realizados, com o saldo atual. Caso não existam movimentações, exibe a mensagem "Não foram realizadas movimentações."

## 🔧 Tecnologias Utilizadas
Linguagem: Python 

Funcionalidades: Uso de validações, controle por variáveis e funções modulares para organização do código.

## Estrutura do Projeto 
📂 Sistema Bancário
├── README.md           # Documentação do projeto
├── sistema_bancario.py # Código-fonte principal
##

## 📖 Como Usar
1. Clone o repositório:\
 git clone https://github.com/SEU_USUARIO/sistema-bancario.git

2. Acesse o diretório do projeto:\
 cd sistema-bancario  
3. Execute o programa:\
 python sistema_bancario.py
##

## 🚀 Exemplo de Uso
Menu inicial: \
[d] Depositar \
[s] Sacar \
[e] Extrato \
[q] Sair \
=> 
##
## Operação de Depósito:
Informe o valor do depósito: 100.50
Depósito realizado com sucesso!
##


## Operação de Saque:
Informe o valor do saque: 50
Saque realizado com sucesso!
#

## Operação de Extrato:
================ EXTRATO ================
\
Depósito: R$ 100.50\
Saque: R$ 50.00

Saldo: R$ 50.50
==========================================
