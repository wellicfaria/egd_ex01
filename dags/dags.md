# Airflow e Dags

Se você desenvolve suas DAGs em um diretório separado e quer que elas apareçam na interface do Airflow, você pode copiá-las para o diretório example_dags que fica dentro da instalação do Airflow.

## Passos

1. `Desenvolva sua DAG`: Crie e teste sua DAG no diretório que você normalmente usa para desenvolvimento, por exemplo /workspaces/egd_ex01/dags/.

2. `Copie para o diretório example_dags`: Execute o seguinte comando para copiar os arquivos da DAG para o diretório example_dags:

```bash
cp /workspaces/egd_ex01/dags/* /usr/local/lib/python3.8/site-packages/airflow/example_dags/
```
Voce deve fazer isso `sempre que atualizar sua dag`. Se não, sua alteração nao acontererá. 

3. `Verifique na Interface`: Abra a interface web do Airflow (http://localhost:8055) e sua DAG deve agora aparecer na lista de DAGs disponíveis.

4. `Ative a DAG`: Para executar a DAG, você precisará ativá-la a partir da interface web.

## Observações Importantes

Este método pode ser útil para fins de teste ou desenvolvimento, mas não é a abordagem recomendada para um ambiente de produção.
Seguindo esses passos, suas DAGs deverão aparecer na interface do Airflow.