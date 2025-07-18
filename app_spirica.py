
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SPIRICA - Pilotage Assurance Vie", layout="wide")

st.title("📊 SPIRICA - Tableau de bord Data Assurance Vie")
st.markdown("Application de visualisation, contrôle qualité et recommandations client.")

@st.cache_data
def load_data():
    return pd.read_csv("clients_spirica.csv")

df = load_data()

# Section 1 : KPIs
st.subheader("🔹 Indicateurs Clés")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre de clients", len(df))
col2.metric("Encours total (€)", f"{df['Montant_Placé (€)'].sum():,.0f}")
col3.metric("Montant moyen (€)", f"{df['Montant_Placé (€)'].mean():,.0f}")
col4.metric("Âge moyen", f"{df['Age'].mean():.1f} ans")

# Section 2 : Visualisation interactive
st.subheader("📈 Répartition des montants placés")
fig1 = px.histogram(df, x="Montant_Placé (€)", nbins=30, color="Statut_Contrat",
                    title="Distribution des montants par statut de contrat")
st.plotly_chart(fig1, use_container_width=True)

# Section 3 : Analyse par équipe
st.subheader("👥 Analyse par responsable")
selected_team = st.selectbox("Sélectionner une équipe :", df["Responsable"].unique())
filtered_df = df[df["Responsable"] == selected_team]

col5, col6 = st.columns(2)
with col5:
    st.write(f"Montant total géré par {selected_team}")
    st.metric(label="Encours (€)", value=f"{filtered_df['Montant_Placé (€)'].sum():,.0f}")

with col6:
    st.write("Clients par statut")
    fig2 = px.pie(filtered_df, names="Statut_Contrat", title="Répartition des contrats")
    st.plotly_chart(fig2, use_container_width=True)

# Section 4 : Contrôle qualité
st.subheader("✅ Contrôle qualité des données")
col7, col8 = st.columns(2)
with col7:
    st.write("🔍 Valeurs manquantes")
    st.dataframe(df.isnull().sum())

with col8:
    st.write("🧬 Doublons potentiels")
    st.write(f"{df.duplicated().sum()} doublons détectés")

# Section 5 : Recommandations clients
st.subheader("💡 Recommandations clients à surveiller")
df_alert = df[(df["Montant_Placé (€)"] < 5000) | (df["Age"] > 75)]
st.dataframe(df_alert[["ClientID", "Nom", "Prénom", "Age", "Montant_Placé (€)", "Statut_Contrat"]])

st.markdown("---")
st.markdown("Projet personnel réalisé par **Samadou KODON** pour démontrer l’intérêt d’un pilotage des données dans le secteur de l’assurance vie.")
