import random

def gerar_arquivo(nome_arquivo, n_linhas):
    soma_total = 0

    with open(nome_arquivo, "w") as f:
        for _ in range(n_linhas):
            valor = random.choice([-1, 0, 1])
            soma_total += valor
            f.write(f"{valor}\n")

    return soma_total


if __name__ == "__main__":
    n = 1000000  # número de linhas (exemplo: 1 milhão)
    #n = 10000000  # número de linhas (exemplo: 1 milhão)
    #n = 1000000000  # número de linhas (exemplo: 1 trilhão)
    
    arquivo = "numero1.txt"

    soma = gerar_arquivo(arquivo, n)

    print(f"Arquivo gerado: {arquivo}")
    print(f"Número de linhas: {n}")
    print(f"Soma total dos valores: {soma}")