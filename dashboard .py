#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

if not os.path.exists("Documents/projet data analyse/train.csv"):
    st.error("Le fichier train.csv est introuvable. Vérifiez son emplacement.")
    st.stop()


# Charger les données
df = pd.read_csv("Documents/projet data analyse/train.csv") 


# Convertir les dates
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True, errors="coerce")
df = df.dropna(subset=["Order Date", "Ship Date"])  # Supprime les lignes avec des dates incorrectes
df["Delivery Time"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Remplacement des valeurs manquantes dans Postal Code par la médiane
df["Postal Code"].fillna(df["Postal Code"].median(), inplace=True)



# Titre du Dashboard
st.title("📊 Tableau de bord - Analyse des Ventes")

# Indicateur clé : Total des ventes
total_sales = df["Sales"].sum()
st.metric(label="Total des ventes", value=f"${total_sales:,.2f}")

# Statistiques générales
st.subheader("📊 Statistiques générales")
st.write(df[["Sales", "Delivery Time"]].describe())

# Suppression des valeurs aberrantes pour éviter des erreurs dans l'analyse
df = df[df["Sales"] > 0]  # Suppression des ventes négatives
df = df[df["Delivery Time"] >= 0]  # Suppression des délais négatifs

# Filtre interactif : Sélection de la catégorie
category = st.selectbox("Sélectionner une catégorie", df["Category"].unique())
filtered_df = df[df["Category"] == category]

# Top 10 des produits les plus vendus
top_products = filtered_df["Product Name"].value_counts().head(10)
st.subheader("🏆 Top 10 des produits les plus vendus")
if not top_products.empty:
    st.bar_chart(top_products)
else:
    st.warning("Aucune donnée disponible pour cette catégorie.")

# Matrice de corrélation
st.subheader("📉 Corrélation entre les variables")
corr_matrix = df[["Sales", "Delivery Time"]].corr()

fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Top 10 des clients les plus rentables
st.subheader("💰 Top 10 des clients les plus rentables")
top_clients = df.groupby("Customer Name")["Sales"].sum().nlargest(10)
fig = px.bar(top_clients, x=top_clients.index, y=top_clients.values, 
             labels={'x': 'Client', 'y': 'Total des ventes'},
             title="Top 10 des clients les plus rentables")
st.plotly_chart(fig)

# Évolution des ventes par mois
df["Month"] = df["Order Date"].dt.to_period("M")  # Convertir la date en période mensuelle
sales_trend = df.groupby("Month")["Sales"].sum()

st.subheader("📈 Tendance des ventes mensuelles")
st.line_chart(sales_trend)

# Afficher l’évolution des ventes dans le temps
st.subheader("Évolution des ventes")
df_time = df.groupby("Order Date")["Sales"].sum()
st.line_chart(df_time)

# Impact des délais de livraison
st.subheader("📦 Impact du délai de livraison sur les ventes")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(data=df, x="Delivery Time", y="Sales", hue="Category", ax=ax)
plt.xlabel("Délai de Livraison (jours)")
plt.ylabel("Ventes ($)")
st.pyplot(fig)


# Filtrage par date
st.sidebar.header("Filtrer par période")
start_date = st.sidebar.date_input("Date de début", pd.to_datetime("2022-01-01"))
end_date = st.sidebar.date_input("Date de fin", pd.to_datetime("2022-12-31"))
df_filtered = df[(df["Order Date"] >= pd.to_datetime(start_date)) & (df["Order Date"] <= pd.to_datetime(end_date))]
# Éviter que l'utilisateur choisisse une mauvaise période
if start_date > end_date:
    st.error("⚠️ La date de début ne peut pas être après la date de fin.")
else:
    df_filtered = df[(df["Order Date"] >= pd.to_datetime(start_date)) & 
                      (df["Order Date"] <= pd.to_datetime(end_date))]


# Filtrage par région
st.sidebar.header("🌍 Filtrer par région")
selected_region = st.sidebar.selectbox("Choisir une région", df["Region"].unique())
df_region = df[df["Region"] == selected_region]

# Répartition des ventes par région
st.subheader("📍 Répartition des ventes par région")
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
st.bar_chart(sales_by_region)

# Ventes par état uniquement si la région est sélectionnée
sales_by_state = df_region.groupby("State")["Sales"].sum().reset_index()

if not sales_by_state.empty:
    st.subheader(f"📊 Ventes par état dans la région {selected_region}")
    fig = px.bar(sales_by_state, x="State", y="Sales", 
                 title=f"Ventes par état dans la région {selected_region}",
                 labels={"State": "État", "Sales": "Ventes ($)"})
    st.plotly_chart(fig)
else:
    st.warning("Aucune donnée disponible pour cette région.")


# Graphique circulaire des ventes par catégorie
st.subheader("📦 Répartition des ventes par catégorie")
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
fig = px.pie(names=sales_by_category.index, values=sales_by_category.values, 
             title="Répartition des ventes par catégorie", hole=0.3)
st.plotly_chart(fig)


# Aperçu des données brutes
st.subheader("📋 Aperçu des Données")
if st.checkbox("Afficher les données brutes"):
    st.write(df.head(20))  # Affiche les 20 premières lignes

# Produits à réapprovisionner (les 10 produits les plus vendus)
st.subheader("📦 Produits les plus demandés")
top_products = df.groupby("Product Name")["Sales"].sum().nlargest(10)
st.bar_chart(top_products)

# Clients fidèles à cibler
st.subheader("👥 Clients fidèles à fidéliser")
loyal_clients = df.groupby("Customer Name")["Sales"].sum().nlargest(10)
st.bar_chart(loyal_clients)


# Ajoute un graphique des clients les plus fréquents (pas seulement ceux qui rapportent le plus d’argent).
st.subheader("👥 Top 10 des clients les plus fréquents")
top_frequent_clients = df["Customer Name"].value_counts().head(10)
st.bar_chart(top_frequent_clients)

#  Identifie les produits qui se vendent le moins :
st.subheader("📉 Top 10 des produits les moins vendus")
low_selling_products = df["Product Name"].value_counts().nsmallest(10)
st.bar_chart(low_selling_products)

#  Ajoute un filtre pour choisir une gamme de prix des produits :
min_price, max_price = st.slider("Sélectionner une plage de prix", float(df["Sales"].min()), float(df["Sales"].max()), (10.0, 500.0))
filtered_df = df[(df["Sales"] >= min_price) & (df["Sales"] <= max_price)]

# comment les ventes varient en fonction du prix
st.subheader("📊 Répartition des ventes par tranche de prix")
fig = px.histogram(filtered_df, x="Sales", nbins=30, title="Distribution des ventes en fonction du prix")
st.plotly_chart(fig)

# catégories se vendent le mieux dans une certaine plage de prix
st.subheader("📦 Ventes par catégorie dans la plage de prix sélectionnée")
sales_by_category_filtered = filtered_df.groupby("Category")["Sales"].sum()
st.bar_chart(sales_by_category_filtered)





# Ajoute un multi-sélecteur pour comparer les ventes de plusieurs régions en même temps :
selected_regions = st.multiselect("Sélectionnez les régions à comparer", df["Region"].unique(), default=df["Region"].unique())
df_selected = df[df["Region"].isin(selected_regions)]
st.bar_chart(df_selected.groupby("Region")["Sales"].sum())

# Ajoute un bouton pour télécharger les données filtrées sous format CSV :
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(label="📥 Télécharger les données", data=csv, file_name="data_analyse.csv", mime="text/csv")




# Personnalisation du style CSS
st.markdown(
    """
    <style>
        .main {
            background-color: #F5F5F5;
        }
        h1 {
            color: #2E3B55;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True  # Ajoute bien la virgule avant cette ligne !
)

# In[ ]:




