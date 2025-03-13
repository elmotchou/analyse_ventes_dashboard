# Dashboard Analyse des Tendances de Vente et Comportements d’Achat

##  Description
Ce projet est une application interactive développée avec Streamlit, permettant d’analyser et de visualiser les tendances de vente et le comportement des clients.
## Objectifs
•	Suivre l’évolution des ventes sur une période donnée.
	•	Analyser les délais de livraison et les tendances d’expédition.
	•	Visualiser les performances commerciales avec des graphiques interactifs.
	•	Comprendre le comportement des clients à travers l’analyse des commandes.

## Fonctionnalités
 Indicateurs clés : Affichage du total des ventes et des statistiques générales.
 Filtrage dynamique : Sélection de la période, de la région et de la catégorie de produits.
 Analyse des produits et clients : Identification des produits les plus vendus et des clients les plus rentables.
 Corrélation des variables : Visualisation des liens entre ventes et délais de livraison.
 Suivi des tendances des ventes : Courbes dynamiques pour observer l’évolution des ventes par mois.
 Répartition géographique : Analyse des ventes par région et par état.
 Impact du délai de livraison : Étude de l’effet du temps de livraison sur le chiffre d’affaires.
 Export des données : Téléchargement des données filtrées sous format CSV.
pip install streamlit pandas plotly

## Structure du projet
Le projet est organisé de la manière suivante :

📁 Projet Data Analyse  
│-- 📜 dashboard.py        # Code du tableau de bord Streamlit  
│-- 📄 train.csv           # Dataset des ventes  
│-- 📜 README.md           # Documentation du projet 

## Installation et Prérequis
📌 1. Prérequis
Avant de commencer, assure-toi d'avoir installé Python 3.7+ et les bibliothèques nécessaires.

📌 2. Installation des dépendances
Exécute la commande suivante pour installer les bibliothèques requises :
pip install streamlit pandas matplotlib seaborn plotly

## Utilisation du projet
📌 1. Cloner le projet
Si tu veux récupérer ce projet depuis GitHub, utilise la commande :
git clone https://github.com/ton-utilisateur/nom-du-projet.git
cd nom-du-projet

📌 2. Lancer l'application
Exécute la commande suivante pour démarrer le tableau de bord interactif :
streamlit run dashboard.py

Une fois la commande exécutée, le dashboard s’ouvrira dans ton navigateur.

## 📊 Aperçu du Tableau de Bord
Le tableau de bord est structuré en plusieurs sections :

1️⃣ Indicateurs Clés
Affichage du total des ventes et des statistiques générales.
Suppression des valeurs aberrantes pour garantir une analyse propre.
2️⃣ Analyse des Produits et Clients
Top 10 des produits les plus vendus 
Top 10 des clients les plus rentables 
Produits les moins vendus 
Clients les plus fréquents 
3️⃣ Visualisation des Tendances
📈 Évolution des ventes mensuelles
📌 Répartition des ventes par catégorie
📊 Corrélation entre ventes et délai de livraison
4️⃣ Analyse Régionale
Répartition des ventes par région 
Comparaison des ventes entre plusieurs régions
Impact de la région sur la rentabilité des produits
5️⃣ Filtrage Dynamique
Filtrage par période (date de début et de fin) 
Filtrage par catégorie de produit 
Filtrage par région et état 
Filtrage par tranche de prix 
6️⃣ Téléchargement des Données
Un bouton de téléchargement permet d’exporter les données filtrées au format CSV.
