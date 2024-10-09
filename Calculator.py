def calculator():
    """
    Calculadora simples para o Hiwo.
    """

    while True:
        operacao = input("Digite a operação (+, -, *, /) ou 's' para sair: ")

        if operacao.lower() == 's':
            break

        if operacao in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Digite números válidos.")
                continue

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                    continue
                else:
                    resultado = num1 / num2

            print(f"Resultado: {resultado}")

        else:
            print("Operação inválida!")