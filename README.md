# 🐉 Pals Analysis – Optimisation des Stratégies dans Palworld

## 🎮 Contexte

Amateur de jeux vidéo et passionné par l’univers de **Palworld**, j’ai réalisé un projet d’analyse de données autour des créatures appelées *Pals*. Ces données offrent une opportunité unique d’explorer les caractéristiques, les comportements et les performances de ces compagnons, dans le but d’optimiser à la fois les **stratégies de combat** et la **productivité dans les campements**.

Ce projet mêle **SQL**, **Python**, **Streamlit** et **visualisation de données**, dans une approche complète de **data exploration** et de **création d’outils interactifs**.

---

## 📂 Données

Le dataset se compose de **6 tables** extraites du jeu :

1. `combat-attribute`
2. `job-skill`
3. `hidden-attribute`
4. `refresh-area`
5. `ordinary-boss-attribute`
6. `tower-boss-attribute`

Les données contiennent notamment :
- Attributs de combat (attaque, défense, vitesse, etc.)
- Compétences de travail (ramassage, production, etc.)
- Nature, taille, rareté, probabilité de capture
- Localisation d'apparition et niveaux

---

## 🧠 Objectifs de l’analyse

- Identifier les **Pals les plus puissants** pour les combats
- Analyser la **répartition des compétences** utiles pour les campements
- Étudier l’impact de la **rareté**, **taille**, ou **vitesse** sur la performance
- Proposer une **équipe de Pals équilibrée**
- Optimiser une **stratégie de capture efficace**
- Construire une **application web interactive** avec Streamlit

---

## 🛠️ Méthodologie

### 1. Préparation
- Exploration initiale des tables
- Nettoyage, correction et normalisation des données
- Import dans une base de données `MariaDB` via le terminal

### 2. Analyse Exploratoire (EDA)
- Réalisée via **SQL** pour les requêtes et **Pandas/Matplotlib/Seaborn** pour la visualisation
- Réponses à plus de 20 questions clés sur les Pals : distributions, corrélations, scores, raretés, compétences...

### 3. Visualisation & Application
- Création d’un dashboard avec **Streamlit**
- Mise en avant des **graphiques les plus pertinents** : distribution des raretés, top Pals, stratégie de capture, etc.

---

## 📊 Résultats clés

- Identification des **10 Pals les plus puissants**
- Corrélation entre rareté et puissance confirmée
- Classement des **Pals les plus adaptés au travail de nuit**
- Proposition d’une **équipe optimale de 5 Pals**
- Tableau des **Pals les plus capturables** pour optimiser sa stratégie d’expansion

---

