def leitura_num(mensagem):
      while True:
            try:
                  valor = float(input(mensagem))
                  return valor
            except ValueError:
                  print("Entrada inválida \n")

num1 = leitura_num('Digite o valor')
num2 = leitura_num('Digite o valor')

print("1 - Soma \n"
      "2 - Subtração \n"
      "3 - Multiplicação \n"
      "4 - Multiplicação \n"
      "5 - Sair")

operacao = input("Selecione um das operações: ")

if operacao == "1":
      print(f"{num1} + {num2} = {num1 + num2}")
elif operacao == "2":
      print(f"{num1} - {num2} = {num1 - num2}")
elif operacao == "3":
      print(f"{num1} * {num2} = {num1 * num2}")
elif operacao == "4":
      print(f"{num1} / {num2} = {num1 / num2}")
elif operacao == "5":
      print("Finalizando...")
else:print("Operação inválida")

