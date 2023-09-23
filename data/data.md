
# Data Folder

## Propósito

Esta pasta é o "armário" onde guardamos todos os tipos de dados usados no projeto. É aqui que ficam os arquivos que você vai usar para análises ou relatórios. Pense nela como uma "caixa" onde você guarda coisas importantes, similar a serviços na internet que fazem o mesmo, como o Amazon S3.

## Estrutura

Nós seguimos um modelo chamado Arquitetura Medalhão para organizar nossos dados. É como se tivéssemos diferentes "gavetas" para diferentes tipos de dados.


- `stage/`: Aqui ficam os dados iniciais, os "brutos". São como os ingredientes antes de cozinhar. Usamos principalmente arquivos no formato "parquet", particionado por data de extração.

- `bronze/`: Estes são dados que passaram por uma "limpeza" inicial. Imagine que você lavou as frutas antes de comê-las; é algo similar. Aqui vamos ter os dados transicionais. Ou seja, vamos conseguir olhar esse registro no tempo.  Usamos arquivos no formato "delta".

- `silver/`: Aqui estão os dados que já foram mais refinados. É como se você já tivesse cortado e temperado os ingredientes para cozinhar. Aqui vamos ter os dados tratados e prontos para ser utilizados.  Usamos arquivos no formato "delta".

- `gold/`: Estes são os dados "prontos para servir". Foram processados, analisados e estão prontos para serem usados em relatórios ou decisões importantes.  Usamos arquivos no formato "delta".





