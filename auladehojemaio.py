def cadastrar_pessoas():
    pessoas = []
    while True:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade de {}: ".format(nome)))
        pessoas.append({"nome": nome, "idade": idade})

        continuar = input("Deseja continuar cadastrando? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    return pessoas

def exibir_resultados(pessoas):
    if pessoas:
        total_pessoas = len(pessoas)
        media_idade = sum(p['idade'] for p in pessoas) / total_pessoas
        pessoa_mais_velha = max(pessoas, key=lambda p: p['idade'])

        print("\nResultados:")
        print(f"Total de pessoas cadastradas: {total_pessoas}")
        print(f"Média de idade: {media_idade:.2f} anos")
        print(f"Pessoa mais velha: {pessoa_mais_velha['nome']} ({pessoa_mais_velha['idade']} anos)")
    else:
        print("Nenhuma pessoa foi cadastrada.")

def main():
    pessoas = cadastrar_pessoas()
    exibir_resultados(pessoas)

if __name__ == "__main__":
    main()