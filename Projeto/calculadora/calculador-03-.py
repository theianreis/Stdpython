def soma(a, b):
    return a + b 

def subtracao(a, b):
    return a - b    

def multiplicacao(a, b):    
    return a * b

def divisao(a, b):  
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def executar_operacao(numero1, operacao, numero2):
    """Executa a operação selecionada"""
    if operacao == '+':
        return soma(numero1, numero2)
    elif operacao == '-':
        return subtracao(numero1, numero2)
    elif operacao == '*':
        return multiplicacao(numero1, numero2)
    elif operacao == '/':
        return divisao(numero1, numero2)
    else:
        return "Operação inválida"

def calculadora():
    """Calculadora com operações encadeadas e função clean"""
    display = 0
    operacao_pendente = None
    numero_anterior = None
    nova_entrada = True
    
    print("\n" + "="*50)
    print("   CALCULADORA - Operações Encadeadas")
    print("="*50)
    print("\nOperadores: + - * /")
    print("Comandos: C (limpar) | = (resultado) | Q (sair)")
    print("="*50 + "\n")
    
    while True:
        
        print(f"\n[DISPLAY: {display}]")
        
        if nova_entrada:
            entrada = input("\nDigite um número: ").strip()
        else:
            entrada = input("\nDigite a próxima operação (+, -, *, /): ").strip()
        
     
        if entrada.upper() == 'C':
            display = 0
            operacao_pendente = None
            numero_anterior = None
            nova_entrada = True
            print("\n Display limpo")
            continue
        
        if entrada.upper() == 'Q':
            print("\n Calculadora encerrada. Até logo")
            break
        
    
        if nova_entrada:
            try:
                display = float(entrada)
                numero_anterior = display
                nova_entrada = False
                print(f" Número inserido: {display}")
            except ValueError:
                print(" Inválido! Digite um número válido.")
                continue
        else:
            if entrada in ['+', '-', '*', '/']:
                if numero_anterior is not None and operacao_pendente is not None:
                    display = executar_operacao(numero_anterior, operacao_pendente, display)
                    print(f"\n Resultado parcial: {display}")
                
                operacao_pendente = entrada
                numero_anterior = display
                nova_entrada = True
                print(f" Operação selecionada: {entrada}")
            
    
            elif entrada == '=':
                if operacao_pendente is not None and numero_anterior is not None:
                    display = executar_operacao(numero_anterior, operacao_pendente, display)
                    print(f"\n" + "="*50)
                    print(f"RESULTADO FINAL: {display}")
                    print("="*50)
                    operacao_pendente = None
                    numero_anterior = None
                    nova_entrada = True
                else:
                    print(" Nenhuma operação para calcular")
            
            else:
                print(" Comando inválido Use: +, -, *, /, =, C ou Q")

if __name__ == "__main__":
    calculadora()