# Inicializando a contagem de números primos
contador_primos = 0

# Loop de 1 a 100
for num in range(1, 101):
    # Números menores que 2 não são primos
    if num < 2:
        continue

    # Verifica se o número é primo
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    # Se for primo, exibe e incrementa a contagem
    if primo:
        print(num)
        contador_primos += 1

# Exibe a quantidade de números primos encontrados
print(f"Quantidade de números primos entre 1 e 100: {contador_primos}")