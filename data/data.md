
# Data Folder

## Propósito

Esta pasta serve como um local de armazenamento para todos os dados brutos e processados utilizados ou gerados pelo projeto. Ela atua como um "bucket" local, similar ao que você encontraria em serviços de armazenamento como o Amazon S3 ou o HDFS (Hadoop Distributed File System).

## Estrutura

Essa organização chamamos de [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture)


- `stage/`: Armazena os dados brutos, como arquivos parquet que são a entrada para os pipelines de dados.
- `bronze/`: Contém os dados transicional que foram processados pelo PySpark.
- `silver/`: Contém os dados as-is e tratados que foram processados e transformados pelo PySpark.
- `gold/`: Contém os dados prontos para usso, agregados e aplicados logica de negocios que foram processados e transformados pelo PySpark.





