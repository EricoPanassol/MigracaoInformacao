# Migração de informação

## Disciplina: Métodos Numéricos
Estudo e construção de modelos matemáticos na solução de problemas computacionais. Utilização adequada da aritmética de ponto flutuante. Análise dos fundamentos matemáticos de algoritmos numéricos. Identificação dos problemas de implementações em ponto flutuante. Apresentação dos conceitos que sustentam algoritmos numéricos e aplicação desses conceitos para a computação numérica eficiente. Realização de computação científica através da programação de algoritmos numéricos.


### Trabalho 2
Seu segundo trabalho nesta disciplina consiste em estudar a migração de informações em um ambiente não-virtual. Em outras palavras, você deve modelar um bando de velhinhas fofoqueiras que moram no bairro e descobrir quantas informações cada uma delas recebe durante o dia. Depois de semanas observando as velhinhas do bairro do Limoeiro, você tem as seguintes informações:

1. As velhinhas contam suas fofocas apenas para um seleto número de amigas, diferente para cada uma delas;

2. As velhinhas tem 10% de probabilidade de esquecerem de contar sua fofoca quando encontram uma amiga (raro, mas acontece);

3. Cada velhinha recebe uma fofoca por dia (graças a fofocas.com.br);

4. A probabilidade de que uma velhinha conte a fofoca depende de quantas amigas ela tem: uma velhinha com duas amigas tem 50% de chance de contar para cada uma delas (descontada a
falta de memória), enquanto uma velhinha com 5 amigas tem 20% de chance (também descontada a falta de memória).

5. Pode ser que uma fofoca circule muito e volte até a velhinha que a originou, mas a esta altura ela já esqueceu tudo e continua passando esta "nova" fofo a adiante.

---

1 : 3 4 6 9 12 14 15

2 : 3 6 7 8 9 12 13 14 15

3 : 5 7 14

4 : 2 6 8 11 13 15

5 : 2 4 6 7 15

6 : 4 5 11

7 : 4 5 11 12 14

8 : 1 3 4 5 7 10 12 13 14 15

9 : 1 2 3 5 12 13 15

10 : 2 5 7 9 11 12 13 15

11 : 2 5 12 15

12 : 1 2 3 4 5 6 7 9 11 13

13 : 2 3 7 11 12 14

14 : 1 4 5 6 7 8

15 : 2 5 6 7 9 11 14

Para garantir o anonimato de cada velhinha de acordo com a LGPD cada uma delas é representada por um número inteiro. Sua missão é descobrir duas informações: qual velhinha terá recebido mais fofocas durante o dia e quantas fofocas serão. Acima você tem um exemplo de arquivo que conta sobre a vida de 15 velhinhas fofoqueiras, com cada velhinha e sua lista de amigas preferidas. Outros arquivos podem ter de ser testados, por isso prepare-se para números maiores! 

Ah, sim. Para garantir que seu programa pode ser rodado em qualquer outro bairro da cidade ele deve ser feito em Java, C, Python ou C++.