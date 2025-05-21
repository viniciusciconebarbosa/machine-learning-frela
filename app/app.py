from flask import Flask, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Função auxiliar para carregar e preparar os dados
def treinar_modelo():
    df = pd.read_csv('alunos_academia_200_com_email.csv')

    # Renomeando colunas para remover acentos
    df = df.rename(columns={
        'Gênero': 'Genero',
        'Frequência_Semanal': 'Frequencia_Semanal',
        'Presenças_Último_Mês': 'Presencas_Ultimo_Mes'
    })

    # Codificação de variáveis categóricas
    le_genero = LabelEncoder()
    le_objetivo = LabelEncoder()
    le_plano = LabelEncoder()

    df['Genero'] = le_genero.fit_transform(df['Genero'])
    df['Objetivo'] = le_objetivo.fit_transform(df['Objetivo'])
    df['Plano'] = le_plano.fit_transform(df['Plano'])

    # Separando as variáveis
    # Remove 'Email' da lista de colunas usadas para treinar o modelo
    X = df.drop(columns=['ID', 'Nome', 'Email', 'Churn'])
    y = df['Churn']

    # Treinamento do modelo
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X, y)

    # Previsão de probabilidade
    df['Prob_Churn'] = modelo.predict_proba(X)[:, 1]

    # Seleciona alunos com alta probabilidade de churn mas ainda ativos
    em_risco = df[(df['Churn'] == 0) & (df['Prob_Churn'] >= 0.25)]
    
    # Retorna todos os campos do CSV mais a probabilidade de churn
    colunas = ['ID', 'Nome', 'Email', 'Idade', 'Genero', 'Altura', 'Peso', 'IMC', 
               'Objetivo', 'Frequencia_Semanal', 'Tempo_de_Assinatura', 'Plano', 
               'Presencas_Ultimo_Mes', 'Prob_Churn']
    
    return em_risco[colunas].sort_values(by='Prob_Churn', ascending=False)

@app.route('/alunos-em-risco', methods=['GET'])
def alunos_em_risco():
    try:
        em_risco = treinar_modelo()
        return jsonify(em_risco.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

