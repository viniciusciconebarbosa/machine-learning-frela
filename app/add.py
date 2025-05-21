import pandas as pd

# Carrega o CSV existente
df = pd.read_csv('alunos_academia_200.csv')

# Cria e-mails fictícios com base no nome
df['Email'] = df['Nome'].str.lower().str.replace(" ", "_") + "@exemplo.com"

# Reorganiza as colunas (opcional)
cols = df.columns.tolist()
cols.insert(2, cols.pop(cols.index('Email')))
df = df[cols]

# Salva o novo CSV
df.to_csv('alunos_academia_200_com_email.csv', index=False)
