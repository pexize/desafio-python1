from colorama import Fore, Style

# Variáveis globais
saldo = 0
extrato = []  # Lista para armazenar o histórico de transações
contador_saque = 0
LIMITE_SAQUES = 3
LIMITE_SAQUE_MAXIMO = 500  # Limite máximo por saque

def exibir_menu():
    # Função para criar o menu com o layout específico
    print(f"{Fore.YELLOW}+--------------------------------------+{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|    Bem-vindo ao Banco GoldSnake!     |{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}+--------------------------------------+{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}|           " + Fore.CYAN + "MENU PRINCIPAL             " + Style.RESET_ALL + Fore.YELLOW + "|")
    print(f"{Fore.YELLOW}|            " + Fore.BLUE + "1 - Extrato               " + Style.RESET_ALL + Fore.YELLOW + "|")
    print(f"{Fore.YELLOW}|            " + Fore.GREEN + "2 - Depósito              " + Style.RESET_ALL + Fore.YELLOW + "|")
    print(f"{Fore.YELLOW}|            " + Fore.RED + "3 - Saque                 " + Style.RESET_ALL + Fore.YELLOW + "|")
    print(f"{Fore.YELLOW}|            " + Fore.MAGENTA + "4 - Sair                  " + Style.RESET_ALL + Fore.YELLOW + "|")
    print(f"{Fore.YELLOW}+--------------------------------------+{Style.RESET_ALL}")

def main():
    global saldo, extrato, contador_saque

    while True:
        exibir_menu()

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print(f"{Fore.RED}❌ Opção inválida! Digite um número.{Style.RESET_ALL}")
            continue

        if opcao == 1:
            # Exibir extrato
            print(f"{Fore.YELLOW}📄 Seu extrato:{Style.RESET_ALL}")
            if not extrato:
                print(f"{Fore.YELLOW}⚠️ Nenhuma transação registrada.{Style.RESET_ALL}")
            else:
                for transacao in extrato:
                    print(transacao)
            print(f"{Fore.YELLOW}Saldo atual: " + Fore.GREEN + f"R${saldo:.2f}{Style.RESET_ALL}")

        elif opcao == 2:
            # Realizar depósito
            print(f"{Fore.YELLOW}Você escolheu a opção de depósito, quanto deseja depositar?{Style.RESET_ALL}")
            try:
                deposito = float(input())
                if deposito > 0:
                    saldo += deposito
                    extrato.append(f"{Fore.YELLOW}✅ Depósito: " + Fore.GREEN + f" R$ {deposito:.2f}{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}✅ Você depositou " + Fore.GREEN + f"R$ {deposito:.2f}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}❌ O valor do depósito deve ser positivo.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Valor inválido! Digite um número.{Style.RESET_ALL}")

        elif opcao == 3:
            # Realizar saque
            print(f"{Fore.YELLOW}Você escolheu a opção de saque, quanto deseja sacar?{Style.RESET_ALL}")
            try:
                saque = float(input())
                if saque > saldo:
                    print(f"{Fore.RED}⚠️ Saldo insuficiente!{Style.RESET_ALL}")
                elif saque <= 0:
                    print(f"{Fore.RED}❌ O valor do saque deve ser positivo.{Style.RESET_ALL}")
                elif saque > LIMITE_SAQUE_MAXIMO:
                    print(f"{Fore.RED}❌ O valor máximo por saque é R$ {LIMITE_SAQUE_MAXIMO:.2f}.{Style.RESET_ALL}")
                elif contador_saque >= LIMITE_SAQUES:
                    print(f"{Fore.RED}🚫 Limite de saques diários atingido.{Style.RESET_ALL}")
                else:
                    saldo -= saque
                    contador_saque += 1
                    extrato.append(f"{Fore.YELLOW}💸 Saque: {Fore.RED}R$ {saque:.2f}{Style.RESET_ALL}")
                    print(f"{Fore.YELLOW}💸 Saque de {Fore.RED}R$ {saque:.2f}{Fore.YELLOW} realizado com sucesso!{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}❌ Valor inválido! Digite um número.{Style.RESET_ALL}")

        elif opcao == 4:
            # Sair do sistema
            print(f"{Fore.YELLOW}👋 Obrigado por usar o Banco GoldSnake. Até logo!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}❌ Opção inválida!{Style.RESET_ALL}")

if __name__ == '__main__':
    main()