def calcular_notas(valor, saldo_disponivel):
    notas = [100, 50, 20, 10, 5, 2]
    quantidade_notas = {}

    if valor > saldo_disponivel:
        return "Saldo insuficiente. Não é possível realizar o saque."

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            quantidade_notas[nota] = quantidade
        valor %= nota

    if valor > 0:
        return "Valor não pode ser sacado com as notas disponíveis."

    return quantidade_notas

def exibir_resultado(quantidade_notas):
    if isinstance(quantidade_notas, str):
        print(quantidade_notas)
    else:
        print("\nNotas a serem entregues:")
        for nota, quantidade in quantidade_notas.items():
            print(f"R${nota},00: {quantidade} {'nota' if quantidade == 1 else 'notas'}")

def main():
    saldo_disponivel = 1000  # Saldo disponível no caixa eletrônico
    print(f"Saldo disponível: R${saldo_disponivel},00")

    while True:
        try:
            valor = int(input("Digite o valor a ser sacado (R$10 a R$600): R$"))
            if 10 <= valor <= 600:
                break
            else:
                print("Valor fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    resultado = calcular_notas(valor, saldo_disponivel)
    exibir_resultado(resultado)

if __name__ == "__main__":
    main()
