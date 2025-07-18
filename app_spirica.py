import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="SPIRICA - Pilotage Data Assurance Vie", layout="wide")

# Bandeau de présentation
st.title("📊 SPIRICA - Tableau de bord Assurance Vie")
st.markdown("""
Bienvenue dans cette application interactive de pilotage des données, développée dans le cadre d’un projet personnel inspiré des problématiques métier d’un Data Analyst en assurance vie chez SPIRICA.

### 🎯 Objectifs du projet :
- Suivre les indicateurs clés de gestion (encours, âges, contrats)
- Contrôler la qualité des données clients
- Identifier des profils à surveiller ou à relancer
- Proposer un outil simple, efficace et activable pour les équipes métier

Toutes les données sont fictives et simulées à des fins pédagogiques.
""")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("clients_spirica.csv")

df = load_data()

# Section : KPIs
st.header("🔹 Indicateurs Clés")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre de clients", len(df))
col2.metric("Encours total (€)", f"{df['Montant_Placé (€)'].sum():,.0f}")
col3.metric("Montant moyen (€)", f"{df['Montant_Placé (€)'].mean():,.0f}")
col4.metric("Âge moyen", f"{df['Age'].mean():.1f} ans")

# Section : Visualisation
st.header("📈 Répartition des montants placés")
fig1 = px.histogram(df, x="Montant_Placé (€)", nbins=30, color="Statut_Contrat",
                    title="Distribution des montants par statut de contrat")
st.plotly_chart(fig1, use_container_width=True)

# Section : Analyse par équipe
st.header("👥 Analyse par responsable")
selected_team = st.selectbox("Sélectionner une équipe métier :", df["Responsable"].unique())
filtered_df = df[df["Responsable"] == selected_team]

col5, col6 = st.columns(2)
with col5:
    st.write(f"Montant total géré par {selected_team}")
    st.metric(label="Encours (€)", value=f"{filtered_df['Montant_Placé (€)'].sum():,.0f}")

with col6:
    fig2 = px.pie(filtered_df, names="Statut_Contrat", title="Répartition des contrats")
    st.plotly_chart(fig2, use_container_width=True)

# Section : Qualité des données
st.header("✅ Contrôle qualité")
col7, col8 = st.columns(2)
with col7:
    st.write("🔍 Valeurs manquantes")
    st.dataframe(
        df.isnull().sum()
        .reset_index()
        .rename(columns={"index": "Colonne", 0: "Nombre de valeurs manquantes"})
    )

with col8:
    st.write("🧬 Doublons détectés")
    st.metric("Doublons exacts", df.duplicated().sum())

# Section : Recommandations
st.header("💡 Recommandations : Clients à surveiller ou relancer")
df_alert = df[(df["Montant_Placé (€)"] < 5000) | (df["Age"] > 75)]
st.dataframe(df_alert[["ClientID", "Nom", "Prénom", "Age", "Montant_Placé (€)", "Statut_Contrat"]])

# Section : Export
st.download_button("📥 Télécharger la liste des clients à surveiller", 
                   data=df_alert.to_csv(index=False), 
                   file_name="clients_a_surveiller.csv",
                   mime="text/csv")

# Pied de page
st.markdown("---")
st.markdown("Projet réalisé par **Samadou KODON** – [Portfolio](https://samadkod.github.io/) | [GitHub](https://github.com/Samadkod)")
