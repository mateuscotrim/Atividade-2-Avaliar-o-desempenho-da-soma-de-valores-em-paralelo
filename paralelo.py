import time
import multiprocessing
import os

def soma_chunk(args):
    arquivo, inicio_byte, fim_byte = args
    total = 0
    with open(arquivo, 'rb') as f:
        f.seek(inicio_byte)
        dados = f.read(fim_byte - inicio_byte)
    for linha in dados.decode('utf-8').splitlines():
        linha = linha.strip()
        if linha:
            total += int(linha)
    return total

def dividir_arquivo(arquivo, num_processos):
    tamanho = os.path.getsize(arquivo)
    tamanho_chunk = tamanho // num_processos
    chunks = []

    with open(arquivo, 'rb') as f:
        inicio = 0
        for i in range(num_processos):
            if i == num_processos - 1:
                fim = tamanho
            else:
                f.seek(inicio + tamanho_chunk)
                f.readline()  # avança até o final da linha
                fim = f.tell()
            chunks.append((arquivo, inicio, fim))
            inicio = fim

    return chunks

def soma_paralela(arquivo, num_threads):
    chunks = dividir_arquivo(arquivo, num_threads)

    inicio = time.perf_counter()

    with multiprocessing.Pool(processes=num_threads) as pool:
        resultados = pool.map(soma_chunk, chunks)

    total = sum(resultados)
    fim = time.perf_counter()
    tempo = fim - inicio

    return total, tempo

if __name__ == "__main__":
    configuracoes = [
        ("numero1.txt", "1 milhão"),
        ("numero2.txt", "10 milhões"),
    ]
    threads_lista = [2, 4, 8, 12]

    for arquivo, descricao in configuracoes:
        print(f"\n{'='*50}")
        print(f"Arquivo: {arquivo} ({descricao} de números)")
        print(f"{'='*50}")
        for n in threads_lista:
            soma, tempo = soma_paralela(arquivo, n)
            print(f"Threads: {n:2d} | Soma: {soma:10d} | Tempo: {tempo:.4f}s")