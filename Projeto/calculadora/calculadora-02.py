def leitura_de_valores(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor 
        except ValueError:
            print("Entrada inválida \n")


while True:
    num1 = leitura_de_valores("Digite um valor: ")
    num2 = leitura_de_valores("Digite outro valor: ")
    operador = input("Digite o operador (+, -, *, /): ")

    match operador:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: Divisão por zero não é permitida.")
                continue
        case _:
            print("Operador inválido.")
            continue
    print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando a calculadora. Até mais!")
        break   
    

