# Dashboard d'Analyse des Tendances de Vente et Comportements d’Achat

##  Description
Ce projet est une application interactive développée avec Streamlit, permettant d’analyser et de visualiser les tendances de vente et le comportement des clients.
## Objectifs
-	Suivre l’évolution des ventes sur une période donnée.
-	Analyser les délais de livraison et les tendances d’expédition.
- Visualiser les performances commerciales avec des graphiques interactifs.
-	Comprendre le comportement des clients à travers l’analyse des commandes.
## Technologies utilisées
-	Python : Traitement des données et développement de l’application.
-	Streamlit : Création d’une interface interactive.
- Pandas : Manipulation des données.
- Matplotlib & Seaborn : Visualisation statistique.
- Plotly : Graphiques interactifs.
  ## Structure du projet
  📦 Projet_Analyse_Ventes
 - ┣ 📜 dashboard.py                 # Script principal de l'application
 - ┣  📜 train.csv                   # Fichier des ventes à analyser
 - ┣ 📜 README.md                     # Documentation du projet

 ## Installation et Exécution
   ### 1/ Prérequis
   Avant d’exécuter le projet, assure-toi d’avoir Python installé, puis installe les bibliothèques nécessaires :
   pip install streamlit pandas matplotlib seaborn plotly
   ### 2/ Lancer l'application
   Utilise la commande suivante pour exécuter l’application Streamlit :
   streamlit run dashboard.py
   L’interface s’ouvrira dans ton navigateur avec les visualisations des tendances de vente.
# 📊 Fonctionnalités du Dashboard
 ## Analyse temporelle des ventes
  - Visualisation de l’évolution des ventes par période.
  - Impact des jours de la semaine sur le volume des commandes.
	## Analyse des délais de livraison
  -	Temps moyen entre la commande et l’expédition. 
  - Influence de la date de commande sur les délais de livraison.
  ## Analyse des revenus et du comportement client
  - Segmentation des ventes par catégorie de produits.
  - Identification des clients à forte valeur.
# Auteur
Abdellah EL MOTCHOU
