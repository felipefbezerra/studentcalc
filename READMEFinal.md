# Sistema de Cálculo de Médias de Alunos

Este projeto é um script em Python que permite calcular a média de notas de alunos em uma turma, determinar a média geral da turma, e identificar os alunos com as maiores e menores médias.

## Funcionalidades

- Solicita ao usuário o número de alunos na turma (entre 2 e 7).
- Para cada aluno, o usuário insere o nome e duas notas.
- O programa calcula a média das notas para cada aluno.
- Determina e exibe a média geral da turma.
- Identifica e exibe o aluno com a maior média e o aluno com a menor média.

## Estrutura do Código

- **Função `calculate_average(notas)`**: Recebe uma lista com duas notas e retorna a média delas.
- **Lista `turma`**: Armazena os dados dos alunos, incluindo nome, notas e média.
- **Entrada de Dados**: O programa solicita ao usuário o número de alunos, valida o valor, e então coleta o nome e notas de cada aluno, garantindo que as notas estejam entre 0,0 e 10,0.
- **Cálculo da Média**: O programa calcula a média individual de cada aluno e também a média geral da turma.
- **Identificação de Extremos**: O programa determina qual aluno obteve a maior e a menor média na turma.

## Uso

1. Execute o script.
2. Insira o número de alunos na turma (mínimo de 2 e máximo de 7).
3. Para cada aluno, insira o nome e as duas notas, garantindo que as notas estejam entre 0,0 e 10,0.
4. O programa calculará e exibirá:
   - A média da turma.
   - O aluno com a maior média.
   - O aluno com a menor média.

## Dependências

- **Python 3.x**: Não há bibliotecas externas necessárias além do Python padrão.

## Exemplo de Execução

1. Ao iniciar o programa, será solicitado o número de alunos.
2. Após inserir o número de alunos, você deve fornecer o nome e as notas de cada aluno.
3. O programa processará os dados e exibirá a média da turma, além dos alunos com as maiores e menores médias.

## Considerações

- As notas devem ser valores numéricos entre 0,0 e 10,0.
- Certifique-se de inserir corretamente os dados, pois o programa exibirá mensagens de erro em caso de entradas inválidas.

### Exemplo de Saída:

```plaintext
Informe a quantidade de alunos (entre 2 e 7): 3
Informe o nome do aluno 1: João
Informe a primeira nota do aluno João: 8.5
Informe a segunda nota do aluno João: 9.0
Informe o nome do aluno 2: Maria
Informe a primeira nota do aluno Maria: 7.0
Informe a segunda nota do aluno Maria: 8.0
Informe o nome do aluno 3: Ana
Informe a primeira nota do aluno Ana: 9.5
Informe a segunda nota do aluno Ana: 9.0

A média da turma é: 8.67
A turma tem 3 alunos
O aluno que obteve a maior média foi Ana com 9.25
O aluno que obteve a menor média foi Maria com 7.50

```
#
# Como Executar

Para executar o programa, basta rodar o arquivo Python em um ambiente de execução.

```bash
python final_janela.py ou final.py
```
Aluno: Felipe Florentino Bezerra