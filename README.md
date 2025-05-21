Este é um sistema que utiliza machine learning para identificar alunos de academia que estão em risco de cancelamento (churn).

## Descrição

O sistema analisa dados dos alunos e utiliza um modelo de Random Forest para prever a probabilidade de churn(Desistencia) por meio de um determinado banco de dados. Ele identifica alunos que ainda estão ativos mas apresentam alto risco de cancelamento.

## Funcionalidades

- Análise de dados dos alunos
- Previsão de probabilidade de churn
- API REST para consulta de alunos em risco
- Identificação de alunos com probabilidade de churn acima de 25%

## Requisitos

- Python 3.x
- Flask
- Pandas
- Scikit-learn

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install flask pandas scikit-learn
```

## Uso

1. Execute o servidor:
```bash
python app.py
```

2. Acesse a API em:
```
http://localhost:5000/alunos-em-risco
```

## Estrutura do Projeto

- `app.py`: Aplicação principal com a API e o modelo de machine learning
- `alunos_academia_200_com_email.csv`: Dataset com informações dos alunos (arquivo convertido)
- `alunos_academia_200.csv`: Dataset original dos alunos
- `add.py`: Script auxiliar para adicionar novos dados e converter arquivos

## Processo de Dados

O sistema trabalha com dois arquivos principais:
1. `alunos_academia_200.csv`: Arquivo original com os dados dos alunos
2. `alunos_academia_200_com_email.csv`: Arquivo convertido que é utilizado pelo `app.py`

O processo de conversão é realizado pelo script `add.py`, que:
- Lê o arquivo original
- Adiciona informações de email
- Gera o arquivo convertido que será utilizado pelo sistema

Para converter o arquivo, execute:
```bash
python add.py
```

## Endpoints da API

### GET /alunos-em-risco
Retorna uma lista de alunos em risco de churn, ordenados por probabilidade de cancelamento.

Resposta:
```json
[
  {
    "ID": 1,
    "Nome": "Nome do Aluno",
    "Email": "email@exemplo.com",
    "Idade": 25,
    "Genero": "M",
    "Altura": 1.75,
    "Peso": 70,
    "IMC": 22.86,
    "Objetivo": "Perda de Peso",
    "Frequencia_Semanal": 3,
    "Tempo_de_Assinatura": 6,
    "Plano": "Mensal",
    "Presencas_Ultimo_Mes": 8,
    "Prob_Churn": 0.35
  }
]
```

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Faça commit das suas alterações
4. Envie um pull request
