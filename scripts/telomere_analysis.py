# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 13:58:30 2025

@author: jpaiva
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# DADOS SIMULADOS (vamos fingir que veio do seu dataset)
# 5 pacientes, 4 medições cada ao longo do tempo
np.random.seed(42)  # para resultados consistentes

data = []
for patient in range(5):
    telomere_start = np.random.uniform(7.5, 8.5)
    for week in [0, 4, 8, 12]:
        telomere_length = telomere_start - (week * 0.03) + np.random.normal(0, 0.1)
        data.append({'patient': f'P{patient}', 'week': week, 'telomere_length': telomere_length})

df = pd.DataFrame(data)
print("Dados de telômeros simulados:")
print(df.head(10))

# Salva para usar depois
df.to_csv('C:\\Users\\jpaiva\\OneDrive - ANP\\Área de Trabalho\\BioInfo\\bio-data-analyzer\\telomere_data.csv', index=False)
print("\n✅ Dados salvos em 'telomere_data.csv'")

def calculate_aging_rate(df):
    """Calcula taxa de encurtamento telomérico por paciente"""
    rates = []
    for patient in df['patient'].unique():
        patient_data = df[df['patient'] == patient].sort_values('week')
        if len(patient_data) > 1:
            rate = (patient_data['telomere_length'].iloc[-1] - patient_data['telomere_length'].iloc[0]) / (patient_data['week'].iloc[-1] - patient_data['week'].iloc[0])
            rates.append({'patient': patient, 'aging_rate_kb_per_week': rate})
    return pd.DataFrame(rates)

# E fazer gráfico simples
def plot_telomere_decay(df):
    plt.figure(figsize=(10, 6))
    for patient in df['patient'].unique():
        patient_data = df[df['patient'] == patient].sort_values('week')
        plt.plot(patient_data['week'], patient_data['telomere_length'], marker='o', label=patient)
    plt.xlabel('Semanas')
    plt.ylabel('Comprimento Telomérico (kb)')
    plt.title('Encurtamento Telomérico ao Longo do Tempo')
    plt.legend()
    plt.savefig('data/telomere_decay_plot.png')  # Salva na pasta data/
    plt.show()