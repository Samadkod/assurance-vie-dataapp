# 📊 Pilotage Data Assurance Vie – Application Streamlit

Projet personnel développé dans le cadre de ma candidature à un poste de **Data Analyst** dans le secteur de l’assurance. Cette application simule une mission réelle de pilotage de portefeuille assurance vie, avec une forte dimension métier, visualisation, qualité des données et recommandations activables.

---

## 🎯 Objectifs du projet

- 🔹 Suivre les **indicateurs clés** : encours, nombre de contrats, âge moyen
- 🛠️ Implémenter un **système de contrôle qualité** : valeurs manquantes, doublons
- 💡 Identifier les **clients à risque ou à valoriser**
- 📈 Permettre un **pilotage fluide par les métiers**, sans compétences techniques

---

## 🚀 Démo en ligne

📎 [Accéder à l'application Streamlit](https://assurance-vie-dataapp-6mfedjpgebfw4o5gmbiokf.streamlit.app)

---

## 📸 Captures d'écran

<table>
  <tr>
    <td><img src="https://samadkod.github.io/assets/assurance_kpi.png" width="400"></td>
    <td><img src="https://github.com/Samadkod/assurance-vie-dataapp/commit/795263bca79e32bbb5787a8741fb3284b99cfce2" width="400"></td>
  </tr>
  <tr>
    <td align="center">Indicateurs clés</td>
    <td align="center">Répartition des contrats</td>
  </tr>
</table>

---

## 🧠 Cas métier simulé

Cette application simule une mission au sein d’une direction Actuariat / Data chez **SPIRICA** ou tout acteur de l’assurance.  
Elle intègre une logique métier simple :

- 🔴 **À relancer** : Contrat en attente + faible montant
- 🟠 **À surveiller** : Contrat actif + âge élevé
- 🟡 **À valoriser** : Ancienneté forte + encours faible

Toutes les données sont **fictives** et **générées à des fins pédagogiques**.

---

## 🛠️ Stack technique

| Outil            | Usage                               |
|------------------|--------------------------------------|
| Python / Pandas  | Manipulation, nettoyage des données |
| Plotly Express   | Visualisations interactives         |
| Streamlit        | Interface utilisateur               |
| CSS / config.toml| Thème et style personnalisés        |
| Git & GitHub     | Versioning, partage et déploiement  |

---

## 📁 Structure du projet

📂 assurance-vie-dataapp
├── app_spirica.py ← code de l'application
├── clients_spirica.csv ← données simulées
├── styles.css ← style personnalisé
├── .streamlit/
│ └── config.toml ← thème Streamlit
└── README.md

---

## 📥 Fonctionnalités clés

✅ KPIs interactifs  
✅ Visualisation filtrable par équipe  
✅ Contrôle qualité intégré  
✅ Recommandations conditionnelles (couleurs, export CSV)  
✅ Déploiement en ligne (Streamlit Cloud)

---

## 🙋‍♂️ À propos

👤 Réalisé par **Samadou KODON**  
🌐 [Portfolio](https://samadkod.github.io) | 🧠 [GitHub](https://github.com/Samadkod) | 💼 [LinkedIn](https://www.linkedin.com/in/skodon)

> *Ce projet fait partie de ma démarche active pour intégrer une équipe Data dans l’assurance ou la finance. N'hésitez pas à me contacter !*

---

