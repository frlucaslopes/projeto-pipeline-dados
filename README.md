![CI](https://github.com/frlucaslopes/projeto-pipeline-dados/actions/workflows/ci.yml/badge.svg)

# Pipeline de Dados com Python, Pandas e CI/CD

Projeto de pipeline de dados que realiza ingestão, transformação e cálculo de métricas de faturamento, com testes automatizados e integração contínua.

Simula um pipeline de dados de ambiente produtivo, aplicando boas práticas de engenharia como testes automatizados e integração contínua.

## Tecnologias
- Python
- Pandas
- Pytest
- Git
- GitHub Actions

## Fluxo do Pipeline
1. Leitura de dados (CSV)
2. Transformação dos dados
3. Cálculo de faturamento
4. Validação com testes automatizados
5. Execução via CI/CD

## Testes
Testes automatizados garantem que o cálculo de faturamento esteja correto, validando cenários de entrada e saída.

## CI/CD
Pipeline automatizado utilizando GitHub Actions:

- Instala dependências
- Executa testes automaticamente a cada push

## Exemplo de saída
| preco | quantidade | faturamento |
|-------|-----------|------------|
| 10    | 2         | 20         |
| 20    | 3         | 60         |

## Estrutura do Projeto
projeto_pipeline/
│
├── src/
│   └── pipeline.py
│
├── tests/
│   └── test_pipeline.py
│
├── data/
│   └── vendas.csv
│
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml

teste