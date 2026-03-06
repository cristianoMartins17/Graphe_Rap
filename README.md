# Analyse des collaborations dans le rap francophone avec des graphes
## Description

Ce projet modélise et analyse les collaborations musicales (featurings) entre artistes du rap francophone en utilisant la théorie des graphes.
Chaque artiste est représenté par un nœud et chaque collaboration par une arête pondérée correspondant au nombre de morceaux réalisés ensemble.

L'objectif est de :
- construire un graphe de collaborations entre artistes
- détecter les cliques (groupes d’artistes fortement connectés)
- identifier les ponts entre cliques
- calculer le diamètre du graphe
- construire un méta-graphe des cliques permettant d’obtenir une vision plus abstraite du réseau

Ce projet a été réalisé dans le cadre d’un projet universitaire donné par un professeur, afin de mettre en pratique les concepts de théorie des graphes et d’analyse de réseaux avec Python.

## Structure du projet

| Fichier             | Description                                              |
| ------------------- | -------------------------------------------------------- |
| `graph_artistes.py` | Construction et visualisation du graphe des artistes     |
| `meta_graphe.py`    | Construction et visualisation du méta-graphe des cliques |

## Technologies utilisées

- Python
- NetworkX = manipulation et analyse de graphes
- Matplotlib = visualisation graphique

Installation des dépendances :
pip install networkx matplotlib

# Graphe des artistes (graph_artistes.py)

Ce fichier construit un graphe de collaborations musicales.

Modélisation
- Nœud : un artiste
- Arête : une collaboration
- Poids de l'arête : nombre de morceaux réalisés ensemble

## Fonctions principales
construire_graphe()

Construit le graphe pondéré des artistes.

Fonctionnement :

1) Création d’un graphe vide NetworkX
2) Ajout des artistes comme nœuds
3) Comptage des collaborations entre chaque paire d’artistes
4) Création des arêtes avec un poids correspondant au nombre de featurings

detecter_cliques(G)

Détecte toutes les cliques de taille ≥ 3 dans le graphe.
Une clique est un sous-graphe dans lequel tous les artistes collaborent entre eux.

Étapes :

1) Recherche de toutes les cliques avec nx.find_cliques
2) Filtrage des cliques de taille ≥ 3
3) Tri par taille décroissante
4) Attribution d'une couleur à chaque clique

| Valeur            | Description                             |
| ----------------- | --------------------------------------- |
| `grandes_cliques` | liste des cliques détectées             |
| `id_clique`       | dictionnaire artiste → numéro de clique |
| `couleur_noeud`   | dictionnaire artiste → couleur          |

# Méta-graphe des cliques (meta_graphe.py)

Ce fichier construit un méta-graphe représentant les relations entre communautés d'artistes.

## Modélisation 
Dans ce graphe abstrait :
- nœud = une clique
- arête = un pont entre deux cliques
Ce graphe permet de simplifier fortement le réseau et de mettre en évidence les relations entre groupes d'artistes.

## Fonctions principales
construire_meta_graphe()
Construit le méta-graphe à partir du graphe des artistes.

Étapes :
1) Construction du graphe des artistes
2) Création d’un nœud pour chaque clique
3) Ajout d’une arête si un pont relie deux cliques
4) Stockage de la composition des cliques

| Valeur        | Description                            |
| ------------- | -------------------------------------- |
| `M`           | méta-graphe                            |
| `composition` | dictionnaire clique → liste d'artistes |

_legende_composition(composition)
Fonction interne qui génère un texte décrivant la composition de chaque clique.

dessiner_meta_graphe()
Affiche la visualisation du méta-graphe.

Caractéristiques :
- taille des nœuds proportionnelle au nombre d'artistes
- arêtes représentant les ponts entre communautés
- légende graphique et textuelle

## Exemple de visualisation
Graphe des artistes
Représentation complète du réseau de collaborations avec :
- communautés (cliques)
- intensité des collaborations
- chemin du diamètre

Méta-graphe
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

## Améliorations possibles
Plusieurs extensions peuvent être envisagées :
- utiliser une base de données musicale réelle
- analyser un réseau beaucoup plus grand
- ajouter des mesures de centralité
- utiliser des algorithmes de détection de communautés plus avancés
- créer une interface interactive

