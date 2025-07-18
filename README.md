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
    <td><img src="https://samadkod.github.io/assets/assurance_pie.png" width="400"></td>
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

