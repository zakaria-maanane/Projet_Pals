import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Visualisation des fichiers Pals 📊")

# Dictionnaire des fichiers CSV
csv_files = {
    "Comparaison of ordinary": r"C:\Users\zakar\Pals\Data propre\Projet_Pals\Pals_Data_comparaison_of_ordinary.csv",
    "Hide": r"C:\Users\zakar\Pals\Data propre\Projet_Pals\Pals_Data_hide.csv",
    "Palu": r"C:\Users\zakar\Pals\Data propre\Projet_Pals\Pals_Palu.csv",
    "Palu Jobs": r"C:\Users\zakar\Pals\Data propre\Projet_Pals\Pals_Palu_Jobs.csv",
    "Palu Refresh": r"C:\Users\zakar\Pals\Data propre\Projet_Pals\Pals_Palu_refresh.csv",
    "Tower": r"C:\Users\zakar\Pals\Data propre\Projet_Pals\Pals_Tower.csv"
}

# Sélection du fichier
selected_file = st.selectbox("📂 Choisis un fichier CSV :", list(csv_files.keys()))

# Lecture du fichier
path = csv_files[selected_file]

if os.path.exists(path):
    df = pd.read_csv(path)

    st.write(f"### Aperçu de : {selected_file}")
    st.dataframe(df)

    if st.checkbox("📈 Afficher un graphique"):

        # Colonnes numériques et catégorielles
        num_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()
        cat_cols = df.select_dtypes(exclude=["float", "int"]).columns.tolist()

        if len(num_cols) >= 1 and len(cat_cols) >= 1:
            # Sélection des axes
            col_cat = st.selectbox("🧭 Axe Y (catégorie) :", cat_cols)
            col_val = st.selectbox("🧭 Axe X (valeur numérique) :", num_cols)

            # Création du graphe
            fig, ax = plt.subplots(figsize=(8, len(df) * 0.3 + 1))  # Taille dynamique selon nb de lignes
            df_sorted = df.sort_values(by=col_val, ascending=True)  # Trier pour une meilleure lisibilité
            df_sorted.plot(kind="barh", x=col_cat, y=col_val, ax=ax, color='skyblue', legend=False)

            ax.set_xlabel(col_val)
            ax.set_ylabel(col_cat)
            ax.tick_params(axis="y", labelsize=8)
            ax.invert_yaxis()  # Le plus haut en haut

            st.pyplot(fig, use_container_width=True)
        else:
            st.warning("Il faut au moins une colonne catégorielle et une colonne numérique pour tracer le graphique.")
else:
    st.error("❌ Le fichier est introuvable. Vérifie le chemin.")
