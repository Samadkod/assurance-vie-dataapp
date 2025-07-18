import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SPIRICA - Pilotage Assurance Vie", layout="wide")

st.title("📊 SPIRICA - Tableau de bord Data Assurance Vie")
st.markdown("Application de visualisation, contrôle qualité et recommandations client.")

# Configuration de la page
st.set_page_config(
    page_title="SPIRICA - Pilotage Data Assurance Vie",
    layout="wide",
    page_icon="📊"
)

# 💡 Ajout du logo fictif Crédit Agricole (SPIRICA = filiale)
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Credit_Agricole.svg/512px-Credit_Agricole.svg.png",
    width=100
)

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
>>>>>>> 6cc0cc2ee0ecada6c4e32de4bd7322d5eb816c5e
@st.cache_data
def load_data():
    return pd.read_csv("clients_spirica.csv")

df = load_data()

<<<<<<< HEAD
# Section 1 : KPIs
st.subheader("🔹 Indicateurs Clés")
=======
# Appliquer la feuille de style CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Section : KPIs
st.header("🔹 Indicateurs Clés")
>>>>>>> 6cc0cc2ee0ecada6c4e32de4bd7322d5eb816c5e
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre de clients", len(df))
col2.metric("Encours total (€)", f"{df['Montant_Placé (€)'].sum():,.0f}")
col3.metric("Montant moyen (€)", f"{df['Montant_Placé (€)'].mean():,.0f}")
col4.metric("Âge moyen", f"{df['Age'].mean():.1f} ans")

<<<<<<< HEAD
# Section 2 : Visualisation interactive
st.subheader("📈 Répartition des montants placés")
=======
# Section : Visualisation
st.header("📈 Répartition des montants placés")
>>>>>>> 6cc0cc2ee0ecada6c4e32de4bd7322d5eb816c5e
fig1 = px.histogram(df, x="Montant_Placé (€)", nbins=30, color="Statut_Contrat",
                    title="Distribution des montants par statut de contrat")
st.plotly_chart(fig1, use_container_width=True)

<<<<<<< HEAD
# Section 3 : Analyse par équipe
st.subheader("👥 Analyse par responsable")
selected_team = st.selectbox("Sélectionner une équipe :", df["Responsable"].unique())
=======
# Section : Analyse par équipe
st.header("👥 Analyse par responsable")
selected_team = st.selectbox("Sélectionner une équipe métier :", df["Responsable"].unique())
>>>>>>> 6cc0cc2ee0ecada6c4e32de4bd7322d5eb816c5e
filtered_df = df[df["Responsable"] == selected_team]

col5, col6 = st.columns(2)
with col5:
    st.write(f"Montant total géré par {selected_team}")
    st.metric(label="Encours (€)", value=f"{filtered_df['Montant_Placé (€)'].sum():,.0f}")

with col6:
<<<<<<< HEAD
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
=======
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
st.header("💡 Recommandations : Clients à surveiller ou valoriser")

df_alert = df.copy()

# Extraction des colonnes utiles
df_alert = df_alert[["ClientID", "Nom", "Prénom", "Age", "Ancienneté (années)", "Montant_Placé (€)", "Statut_Contrat"]]

# Filtrage des cas intéressants
df_alert = df_alert[
    ((df_alert["Montant_Placé (€)"] < 10000) & (df_alert["Statut_Contrat"] == "En attente")) |
    ((df_alert["Age"] > 75) & (df_alert["Statut_Contrat"] == "Actif")) |
    ((df_alert["Ancienneté (années)"] > 10) & (df_alert["Montant_Placé (€)"] < 20000))
]

# Fonction métier de mise en forme
def highlight_recommandation(row):
    if row["Montant_Placé (€)"] < 10000 and row["Statut_Contrat"] == "En attente":
        return ['background-color: #f8d7da; font-weight: bold'] * len(row)  # Rouge clair
    elif row["Age"] > 75 and row["Statut_Contrat"] == "Actif":
        return ['background-color: #fff3cd; font-weight: bold'] * len(row)  # Orange clair
    elif row["Ancienneté (années)"] > 10 and row["Montant_Placé (€)"] < 20000:
        return ['background-color: #e2e3ff; font-weight: bold'] * len(row)  # Jaune clair
    else:
        return [''] * len(row)

# Affichage stylé
st.dataframe(df_alert.style.apply(highlight_recommandation, axis=1))

# Section : Export
st.download_button("📥 Télécharger la liste des clients à surveiller", 
                   data=df_alert.to_csv(index=False), 
                   file_name="clients_a_surveiller.csv",
                   mime="text/csv")

# Pied de page
st.markdown("---")
st.markdown('<div class="highlight-box">📌 Relancer en priorité les clients "En attente" avec faible montant.</div>', unsafe_allow_html=True)
st.markdown("Projet réalisé par **Samadou KODON** – [Portfolio](https://samadkod.github.io/) | [GitHub](https://github.com/Samadkod)")
>>>>>>> 6cc0cc2ee0ecada6c4e32de4bd7322d5eb816c5e
