import time

def soma_serial(arquivo):
    inicio = time.perf_counter()
    
    total = 0
    with open(arquivo, 'r') as f:
        for linha in f:
            total += int(linha.strip())
    
    fim = time.perf_counter()
    tempo = fim - inicio
    
    return total, tempo

if __name__ == "__main__":

    arquivo = "numero1.txt"
    soma, tempo = soma_serial(arquivo)
    print(f"Arquivo: {arquivo}")
    print(f"Soma total: {soma}")
    print(f"Tempo serial: {tempo:.4f} segundos")

    print()

    arquivo = "numero2.txt"
    soma, tempo = soma_serial(arquivo)
    print(f"Arquivo: {arquivo}")
    print(f"Soma total: {soma}")
    print(f"Tempo serial: {tempo:.4f} segundos")