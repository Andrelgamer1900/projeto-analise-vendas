import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuração de estilo
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Criando diretório para imagens
os.makedirs('img', exist_ok=True)

# 1. Dados de Funil de Vendas (Simulados com base na estrutura da query)
data_funnel = {
    'mês': ['2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06'],
    'leads': [1200, 1500, 1100, 1800, 2000, 1700],
    'vendas': [150, 210, 140, 280, 320, 250]
}
df_funnel = pd.DataFrame(data_funnel)
df_funnel['conversão (%)'] = (df_funnel['vendas'] / df_funnel['leads']) * 100

# Gráfico de Funil (Leads vs Vendas)
fig, ax1 = plt.subplots()
sns.barplot(x='mês', y='leads', data=df_funnel, color='skyblue', label='Leads', ax=ax1)
ax2 = ax1.twinx()
sns.lineplot(x='mês', y='vendas', data=df_funnel, marker='o', color='darkblue', label='Vendas', ax=ax2)
ax1.set_title('Funil de Vendas: Leads vs Vendas Mensais')
plt.savefig('img/funil_vendas.png', bbox_inches='tight')
plt.close()

# 2. Top 5 Estados (Simulados)
data_states = {
    'estado': ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Paraná', 'Santa Catarina'],
    'vendas': [450, 320, 280, 210, 190]
}
df_states = pd.DataFrame(data_states)
plt.figure()
sns.barplot(x='vendas', y='estado', data=df_states, palette='viridis')
plt.title('Top 5 Estados por Volume de Vendas')
plt.savefig('img/top_estados.png', bbox_inches='tight')
plt.close()

# 3. Vendas por Marca (Simulados)
data_brands = {
    'marca': ['Fiat', 'Volkswagen', 'Chevrolet', 'Toyota', 'Hyundai'],
    'vendas': [120, 110, 95, 80, 75]
}
df_brands = pd.DataFrame(data_brands)
plt.figure()
plt.pie(df_brands['vendas'], labels=df_brands['marca'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribuição de Vendas por Marca (Top 5)')
plt.savefig('img/vendas_marca.png', bbox_inches='tight')
plt.close()

print("Visualizações geradas com sucesso na pasta 'img/'")
