import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib

# 1. Carregando os dados
df = pd.read_csv('dados_academia.csv')

# 2. Preprocessamento
label_encoder = LabelEncoder()
df['Gênero'] = label_encoder.fit_transform(df['Gênero'])
df['Objetivo'] = label_encoder.fit_transform(df['Objetivo'])
df['Plano'] = label_encoder.fit_transform(df['Plano'])

# 3. Separando variáveis
X = df.drop(columns=['ID', 'Nome', 'Churn'])
y = df['Churn']

# 4. Dividindo dados para treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Treinando o modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_train, y_train)

# 6. Avaliação (opcional)
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

# 7. Prevendo probabilidade para todos os alunos
df['Prob_Churn'] = modelo.predict_proba(X)[:, 1]

# 8. Selecionando possíveis canceladores (ainda ativos mas com alta probabilidade de churn)
possiveis_canceladores = df[(df['Churn'] == 0) & (df['Prob_Churn'] >= 0.7)]

# 9. Mostrando os alunos em risco
print("Alunos ativos com alto risco de cancelamento:")
print(possiveis_canceladores[['ID', 'Nome', 'Prob_Churn']]).o_churn.pkl
