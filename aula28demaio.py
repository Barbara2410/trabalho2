def calcular_notas(valor):
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = {}

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            quantidade_notas[nota] = quantidade
        valor %= nota

    return quantidade_notas

def exibir_resultado(quantidade_notas):
    print("\nNotas a serem entregues:")
    for nota, quantidade in quantidade_notas.items():
        print(f"R${nota},00: {quantidade} {'nota' if quantidade == 1 else 'notas'}")

def main():
    print("Bem-vindo ao Caixa Eletrônico!")
    while True:
        try:
            valor = int(input("Digite o valor a ser sacado (R$10 a R$600): R$"))
            if 10 <= valor <= 600:
                break
            else:
                print("Valor fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    quantidade_notas = calcular_notas(valor)
    exibir_resultado(quantidade_notas)

if __name__ == "__main__":
    main()
