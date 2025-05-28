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
        # Sélection de colonnes numériques automatiquement
        numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()

        if len(numeric_cols) >= 1:
            col_x = st.selectbox("🧭 Axe X :", numeric_cols)
            col_y = st.selectbox("🧭 Axe Y :", numeric_cols, index=1 if len(numeric_cols) > 1 else 0)

            # Création du graphe
            fig, ax = plt.subplots()
            df.plot(kind="barh", x=col_x, y=col_y, ax=ax, color='skyblue', legend=False)
            ax.set_xlabel(col_y)
            ax.set_ylabel(col_x)
            st.pyplot(fig)
        else:
            st.warning("Ce fichier ne contient pas de colonnes numériques à visualiser.")
else:
    st.error("❌ Le fichier est introuvable. Vérifie le chemin.")
