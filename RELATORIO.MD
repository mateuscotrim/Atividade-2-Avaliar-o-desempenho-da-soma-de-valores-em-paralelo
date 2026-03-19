# Relatório – Soma Paralela de Valores com multiprocessing

**Disciplina:** PROGRAMAÇÃO CONCORRENTE E DISTRIBUÍDA  
**Aluno(s):** MATEUS RECALDE DA FONSECA COTRIM
**Professor:** RAFAEL MARCONI RAMOS
**Data:** 18/03/2026

---

# 1. Descrição do Problema

O programa lê um arquivo de texto com milhões de números inteiros, um por linha, e calcula a soma de todos eles. A ideia foi primeiro fazer isso de forma normal (serial), um número de cada vez, e depois tentar fazer mais rápido dividindo o trabalho entre vários processos ao mesmo tempo (paralelo).

- **O que o programa faz?** Soma todos os números de um arquivo de texto.
- **Quantos dados foram usados?** Dois arquivos: um com 1 milhão de números e outro com 10 milhões.
- **Como foi paralelizado?** O arquivo foi dividido em pedaços, cada processo ficou responsável por somar um pedaço, e no final os resultados foram somados juntos.
- **Complexidade:** O(n) — quanto mais números, mais tempo leva, de forma proporcional.

---

# 2. Ambiente Experimental

Essas são as configurações do computador usado para rodar os testes (retiradas do Gerenciador de Tarefas do Windows):

| Item                        | Descrição                              |
|-----------------------------|----------------------------------------|
| Processador                 | Intel Core i5-12500                    |
| Número de núcleos           | 6                                      |
| Memória RAM                 | 16 GB (10 GB em uso durante os testes) |
| Sistema Operacional         | Windows 11                             |
| Linguagem utilizada         | Python                                 |
| Biblioteca de paralelização | multiprocessing                        |
| Compilador / Versão         | Python 3.13                            |

---

# 3. Metodologia de Testes

Para medir o tempo de cada execução, usamos a função `time.perf_counter()` do Python, que mede o tempo com bastante precisão. Ela é chamada antes de começar a soma e depois que termina, e a diferença entre os dois valores é o tempo de execução.

Rodamos o programa uma vez para cada configuração (1, 2, 4, 8 e 12 processos) e anotamos o tempo.

### Configurações testadas

- 1 processo — versão serial (sem paralelismo)
- 2 processos
- 4 processos
- 8 processos
- 12 processos

### Como o experimento foi feito

Rodamos tudo na mesma máquina, sem fechar outros programas. O tempo inclui tudo: dividir o arquivo, criar os processos, somar os pedaços e juntar os resultados no final.

---

# 4. Resultados Experimentais

## Exemplo 1 – 1 Milhão de Números (soma = −88)

| Nº Processos | Tempo de Execução (s) |
|:------------:|:---------------------:|
| 1 (serial)   | 0,0893                |
| 2            | 0,1199                |
| 4            | 0,1005                |
| 8            | 0,1030                |
| 12           | 0,1315                |

## Exemplo 2 – 10 Milhões de Números (soma = 5.384)

| Nº Processos | Tempo de Execução (s) |
|:------------:|:---------------------:|
| 1 (serial)   | 0,9593                |
| 2            | 0,6419                |
| 4            | 0,3826                |
| 8            | 0,3079                |
| 12           | 0,3104                |

---

# 5. Cálculo de Speedup e Eficiência

### Speedup

O Speedup mostra quantas vezes o programa paralelo foi mais rápido que o serial.

```
Speedup(p) = T(1) / T(p)
```

- **T(1)** = tempo da execução serial (1 processo)
- **T(p)** = tempo com p processos

### Eficiência

A Eficiência mostra o quanto cada processo está sendo bem aproveitado. O valor ideal é 1,0 (100%).

```
Eficiência(p) = Speedup(p) / p
```

---

# 6. Tabela de Resultados
 
## Exemplo 1 – 1 Milhão de Números
 
| Processos | Tempo (s) | Speedup | Eficiência (%) |
|:---------:|:---------:|:-------:|:--------------:|
| 1         | 0,0893    | 1,00    | 100,0%         |
| 2         | 0,1199    | 0,74    | 37,2%          |
| 4         | 0,1005    | 0,89    | 22,2%          |
| 8         | 0,1030    | 0,87    | 10,8%          |
| 12        | 0,1315    | 0,68    | 5,7%           |
 
## Exemplo 2 – 10 Milhões de Números
 
| Processos | Tempo (s) | Speedup | Eficiência (%) |
|:---------:|:---------:|:-------:|:--------------:|
| 1         | 0,9593    | 1,00    | 100,0%         |
| 2         | 0,6419    | 1,49    | 74,7%          |
| 4         | 0,3826    | 2,51    | 62,7%          |
| 8         | 0,3079    | 3,12    | 38,9%          |
| 12        | 0,3104    | 3,09    | 25,8%          |
 
---

# 7. Gráfico de Tempo de Execução

![alt text](<img/Tempo - Ex. 01.png>)

*(Gráfico de Tempo de Execução do exemplo 01 disponível na pasta **img** no arquivo `/img/Tempo - Ex. 01.png`)*


![alt text](<img/Tempo - Ex. 02.png>)

*(Gráfico de Tempo de Execução do exemplo 02 disponível na pasta **img** no arquivo `/img/Tempo - Ex. 02.png`)*

No arquivo com 1 milhão de números, o tempo paralelo foi sempre maior que o serial — ou seja, usar mais processos deixou o programa mais lento. Já com 10 milhões de números, o tempo caiu bastante ao adicionar processos, chegando ao melhor resultado com 8 processos.

---

# 8. Gráfico de Speedup

![alt text](<img/SpeedUP - Ex. 01.png>)

*(Gráfico de Speedup do exemplo 01 disponível na pasta **img** no arquivo `/img/SpeedUP - Ex. 01.png`)*


![alt text](<img/SpeedUP - Ex. 02.png>)

*(Gráfico de Speedup do exemplo 02 disponível na pasta **img** no arquivo `/img/SpeedUP - Ex. 02.png`)*

O gráfico mostra a linha do speedup ideal (linear) e o speedup real obtido. Com 10 milhões de números e 8 processos, conseguimos um speedup de 3,12×, bem abaixo do ideal de 8×. Com 1 milhão de números, o speedup ficou abaixo de 1,0 em todos os casos.

---

# 9. Gráfico de Eficiência

![alt text](<img/Eficiencia - Ex. 01.png>)

*(Gráfico de Eficiência do exemplo 01 disponível na pasta **img** no arquivo `/img/Eficiencia - Ex. 01.png`)*


![alt text](<img/Eficiencia - Ex. 02.png>)

*(Gráfico de Eficiência do exemplo 02 disponível na pasta **img** no arquivo `/img/Eficiencia - Ex. 02.png`)*

A eficiência caiu conforme aumentamos o número de processos. O melhor resultado foi 74,7% com 2 processos no arquivo de 10 milhões. Com 12 processos, a eficiência caiu para 25,8%, mostrando que a maior parte do tempo estava sendo "desperdiçada" com o custo de coordenar os processos.

---

# 10. Análise dos Resultados

**O speedup foi próximo do ideal?**  
Não. Com 8 processos, o ideal seria um speedup de 8×, mas conseguimos apenas 3,12× no arquivo de 10 milhões. No arquivo de 1 milhão, o programa ficou mais lento do que rodando sozinho.

**A aplicação escalou bem?**  
Mais ou menos. Com 10 milhões de números, o tempo foi caindo até 8 processos. Com 12 processos, praticamente não houve melhora — o tempo foi quase o mesmo que com 8.

**Em qual ponto a eficiência começou a cair?**  
Já com 2 processos a eficiência caiu para 74,7%, e continuou caindo a cada configuração nova.

**O número de processos passou o número de núcleos físicos?**  
Sim. O processador tem 6 núcleos físicos. Quando usamos 8 ou 12 processos, o computador tem que "revezar" os processos nos mesmos núcleos, o que gera um custo extra e diminui o ganho.

**Por que o programa ficou mais lento com mais processos no arquivo de 1 milhão?**  
Com poucos dados, o tempo gasto para criar os processos e dividir o arquivo foi maior do que o tempo que seria economizado com o paralelismo. É como contratar várias pessoas para resolver um problema simples — o tempo de explicar o que cada um vai fazer acaba sendo maior que o problema em si.

**Por que com 10 milhões funcionou melhor?**  
Com mais dados, o trabalho de cada processo é grande o suficiente para compensar o custo de criação e comunicação. O ganho do paralelismo supera o overhead.

---

# 11. Conclusão

O paralelismo com `multiprocessing` só valeu a pena quando o volume de dados era grande (10 milhões de números). Com 1 milhão, o programa serial foi mais rápido em todos os casos.

O melhor resultado foi com **8 processos**, chegando a 3,12× mais rápido que o serial no arquivo de 10 milhões. Usar 12 processos não trouxe nenhuma melhora — o que faz sentido, já que a máquina só tem 6 núcleos físicos.

A principal limitação foi que o programa passa muito tempo **lendo o arquivo do disco**, e isso não fica mais rápido só porque tem mais processos — pelo contrário, vários processos tentando ler ao mesmo tempo podem até atrapalhar um ao outro.

Se fosse para melhorar, as principais mudanças seriam:
- Carregar o arquivo inteiro na memória RAM antes de dividir entre os processos
- Usar bibliotecas como `numpy` que leem e somam dados muito mais rápido
- Usar arquivos em formato binário em vez de texto, para evitar converter cada linha em número

No geral, o experimento mostrou na prática que **mais processos nem sempre significa mais velocidade** — depende muito do tamanho do problema e do tipo de tarefa sendo executada.
