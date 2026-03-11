# Analyse des collaborations dans le rap francophone avec des graphes

## Description

(Notre professeur a autorisé, voire conseillé, l'utilisation de l'IA. J'ai donc utilisé Claude pour le HTML et l'implémentation de Dijkstra.)

Ce projet modélise et analyse les collaborations musicales (featurings) entre artistes du rap francophone en utilisant la théorie des graphes.
Chaque artiste est représenté par un nœud et chaque collaboration par une arête pondérée correspondant au nombre de morceaux réalisés ensemble.

L'objectif est de :
- construire un graphe de collaborations entre artistes
- détecter les cliques (groupes d'artistes fortement connectés)
- identifier les ponts entre cliques
- calculer le diamètre du graphe via l'algorithme de Dijkstra
- construire un méta-graphe des cliques permettant d'obtenir une vision plus abstraite du réseau
- visualiser l'ensemble de manière interactive dans un navigateur web

## Structure du projet

| Fichier               | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| `graph_artistes.py`   | Construction et visualisation du graphe des artistes               |
| `meta_graphe.py`      | Construction et visualisation du méta-graphe des cliques           |
| `export_json.py`      | Export des données en JSON pour la visualisation HTML              |
| `rap_fr_graphes.html` | Visualisation interactive (graphe + méta-graphe + Dijkstra)        |

## Technologies utilisées

- Python
- NetworkX — manipulation et analyse de graphes
- Matplotlib — visualisation graphique
- D3.js — visualisation interactive dans le navigateur
- HTML / CSS / JavaScript — interface web standalone

Installation des dépendances Python :
```
pip install networkx matplotlib
```

---

# Graphe des artistes (graph_artistes.py)

Ce fichier construit un graphe de collaborations musicales.

### Modélisation
- Nœud : un artiste
- Arête : une collaboration
- Poids de l'arête : nombre de morceaux réalisés ensemble

## Fonctions principales

### construire_graphe()

Construit le graphe pondéré des artistes.

Fonctionnement :

1. Création d'un graphe vide NetworkX
2. Ajout des artistes comme nœuds
3. Comptage des collaborations entre chaque paire d'artistes
4. Création des arêtes avec un poids correspondant au nombre de featurings

### detecter_cliques(G)

Détecte toutes les cliques de taille ≥ 3 dans le graphe.
Une clique est un sous-graphe dans lequel tous les artistes collaborent entre eux.

Étapes :

1. Recherche de toutes les cliques avec `nx.find_cliques`
2. Filtrage des cliques de taille ≥ 3
3. Tri par taille décroissante
4. Attribution d'une couleur à chaque clique

| Valeur            | Description                             |
| ----------------- | --------------------------------------- |
| `grandes_cliques` | liste des cliques détectées             |
| `id_clique`       | dictionnaire artiste → numéro de clique |
| `couleur_noeud`   | dictionnaire artiste → couleur          |

---

# Méta-graphe des cliques (meta_graphe.py)

Ce fichier construit un méta-graphe représentant les relations entre communautés d'artistes.

## Modélisation

Dans ce graphe abstrait :
- nœud = une clique
- arête = un pont entre deux cliques

Ce graphe permet de simplifier fortement le réseau et de mettre en évidence les relations entre groupes d'artistes.

## Fonctions principales

### construire_meta_graphe()

Construit le méta-graphe à partir du graphe des artistes.

Étapes :
1. Construction du graphe des artistes
2. Création d'un nœud pour chaque clique
3. Ajout d'une arête si un pont relie deux cliques
4. Stockage de la composition des cliques

| Valeur        | Description                            |
| ------------- | -------------------------------------- |
| `M`           | méta-graphe                            |
| `composition` | dictionnaire clique → liste d'artistes |

### _legende_composition(composition)

Fonction interne qui génère un texte décrivant la composition de chaque clique.

### dessiner_meta_graphe()

Affiche la visualisation du méta-graphe.

Caractéristiques :
- taille des nœuds proportionnelle au nombre d'artistes
- arêtes représentant les ponts entre communautés
- légende graphique et textuelle

---

# Visualisation interactive (export_json.py + rap_fr_graphes.html)

Cette partie du projet permet d'explorer les deux graphes dans un navigateur web, sans serveur ni dépendance externe, à partir d'un unique fichier HTML autonome.

## Fonctionnement général

```
graph_artistes.py  ──┐
                      ├──► export_json.py ──► rap_fr_graphes.html
meta_graphe.py     ──┘
```

`export_json.py` appelle les fonctions Python existantes et sérialise les données (nœuds, arêtes, cliques, ponts) en JSON. Ces données sont ensuite embarquées directement dans le fichier HTML, qui utilise la bibliothèque D3.js pour le rendu.

## Utilisation

**Étape 1 — Régénérer les données** (uniquement si le graphe Python a changé) :
```bash
python export_json.py
```

**Étape 2 — Ouvrir la visualisation** :
Double-cliquer sur `rap_fr_graphes.html`. Aucun serveur requis.

## Contenu de la visualisation

### Onglet « Graphe principal »

Affiche le graphe complet des artistes avec :
- nœuds colorés par clique d'appartenance (même palette que Matplotlib)
- arêtes dont l'épaisseur est proportionnelle au nombre de featurings
- arêtes top collaboration (rouge) et ponts inter-cliques (vert acide) mis en évidence
- sidebar affichant les statistiques, le classement des artistes par degré et la liste des cliques

Interactions disponibles :
- survol d'un nœud → affiche le nom, la clique et les principales collaborations
- survol d'une arête → affiche les deux artistes et le nombre de featurings
- clic sur une clique dans la légende → isole visuellement les membres pendant 2,5 secondes
- scroll / drag → zoom et déplacement du graphe

### Onglet « Méta-graphe des cliques »

Affiche le méta-graphe avec :
- un nœud par clique, dont le rayon est proportionnel à la taille de la clique
- des arêtes rouges représentant les ponts inter-cliques
- sidebar listant la composition de chaque clique et le nombre de ponts associés

Interactions disponibles :
- survol d'un nœud → affiche la liste complète des artistes de la clique
- survol d'une arête → affiche les deux cliques reliées
- scroll / drag → zoom et déplacement

### Algorithme de Dijkstra (onglet graphe principal)

Un bouton **▶ AFFICHER LE DIAMÈTRE** dans la sidebar calcule et affiche le diamètre du graphe :

| Étape | Description |
| ----- | ----------- |
| `buildAdjacency()` | Construit la liste d'adjacence avec poids = 1 sur toutes les arêtes |
| `dijkstra(adj, source)` | Exécute Dijkstra depuis un nœud source |
| `findDiameter()` | Lance Dijkstra depuis chaque nœud et retient la paire maximisant la distance |
| `reconstructPath()` | Remonte le chemin depuis le tableau des prédécesseurs |

Le chemin diamétral est tracé en **violet animé** sur le graphe. Les nœuds et arêtes hors chemin sont grisés pour faciliter la lecture. Un bouton **✕ Effacer** remet le graphe dans son état initial.

> Note : le poids des arêtes n'est pas pris en compte pour ce calcul — chaque arête vaut 1 saut, conformément à la définition du diamètre topologique du graphe.

## Choix techniques

Les coordonnées des nœuds sont calculées par NetworkX (`circular_layout`) côté Python, puis exportées en JSON dans l'intervalle `[-1, 1]`. Le SVG utilise un `viewBox="-1.2 -1.2 2.4 2.4"` afin d'utiliser ces coordonnées directement, sans aucune conversion pixel — ce qui rend le rendu indépendant de la taille de la fenêtre.

---

## Exemple de visualisation

**Graphe des artistes**
Représentation complète du réseau de collaborations avec :
- communautés (cliques)
- intensité des collaborations
- chemin du diamètre (via Dijkstra)

**Méta-graphe**
Version simplifiée du réseau :
- chaque nœud représente une communauté d'artistes
- les arêtes représentent les connexions entre communautés

## Objectifs pédagogiques du projet

Ce projet permet de mettre en pratique :
- la modélisation de réseaux avec des graphes
- la détection de communautés (cliques)
- l'analyse de centralité et de distances
- la construction de méta-graphes
- la visualisation de réseaux
- l'implémentation de l'algorithme de Dijkstra

## Améliorations possibles

Plusieurs extensions peuvent être envisagées :
- utiliser une base de données musicale réelle
- analyser un réseau beaucoup plus grand
- ajouter des mesures de centralité
- utiliser des algorithmes de détection de communautés plus avancés
- ajouter un mode de recherche par artiste dans la visualisation HTML
- permettre le chargement dynamique d'un nouveau jeu de données sans regénérer le HTML
