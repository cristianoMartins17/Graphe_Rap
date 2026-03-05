"""
==================
Construction et affichage du graphe de collaborations (featurings)
entre artistes du rap francophone.

Chaque nœud  = un artiste.
Chaque arête = au moins un featuring commun, pondérée par le nombre de morceaux.
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter


# ---------------------------------------------------------------------------
# Données brutes
# ---------------------------------------------------------------------------

ARTISTES: list[str] = [
    "Alpha Wann", "Angèle", "Booba", "Damso", "Di-Meh", "Disiz",
    "Orelsan", "Freeze Corleone", "Gazo", "Hamza", "Josman", "Kaaris",
    "Kalash Criminel", "Koba LaD", "Laylow", "Leto", "Lomepal", "Makala",
    "Mister V", "Nekfeu", "Ziak", "PLK", "Roméo Elvis", "SCH", "SDM",
    "Slimka", "Tiakola", "Vald", "Werenoi", "Ninho", "Zola",
]

# Une entrée par morceau. La syntaxe *[...] * N évite la répétition.
COLLABORATIONS_BRUTES: list[tuple[str, str]] = [
    # Alpha Wann × Nekfeu  (9 morceaux)
    *[("Alpha Wann", "Nekfeu")] * 9,

    # Alpha Wann × Freeze Corleone  — "Rap Catéchisme", "ny à fond"
    *[("Alpha Wann", "Freeze Corleone")] * 2,

    # Alpha Wann × Laylow  — "STUNTMEN", "Vamonos"
    *[("Alpha Wann", "Laylow")] * 2,

    # Angèle × Damso  — "Silence", "Démons", "Tout tenter"
    *[("Angèle", "Damso")] * 3,

    ("Angèle", "Orelsan"),          # "Évidemment"
    ("Angèle", "Gazo"),             # "Notre dame"
    ("Angèle", "Tiakola"),          # "Notre dame"

    # Angèle × Roméo Elvis  — "Tout Oublier", "J'ai vu"
    *[("Angèle", "Roméo Elvis")] * 2,

    # Booba × Damso  — "Pinocchio", "Paris c'est loin", "113"
    *[("Booba", "Damso")] * 3,

    # Booba × Kaaris  — "L.E.F", "Kalash"
    *[("Booba", "Kaaris")] * 2,

    # Booba × SDM  — "La zone", "Daddy", "Bonne journée", "Dolce Camara", "92i"
    *[("Booba", "SDM")] * 5,

    ("Damso", "Disiz"),             # "RENCONTRES"

    # Damso × Hamza  — "God Bless", "BXL ZOO", "Nocif"
    *[("Damso", "Hamza")] * 3,

    ("Damso", "Laylow"),            # "R9RLine"
    ("Damso", "Nekfeu"),            # "Tricheurs"
    ("Damso", "Orelsan"),           # "Rêves bizarres"

    # Damso × Gazo  — "La Rue", "Bodies"
    *[("Damso", "Gazo")] * 2,

    # Di-Meh × Makala  — "Mortal Kombat", "Golden", "Depeche Mode"
    *[("Di-Meh", "Makala")] * 3,

    # Di-Meh × Slimka  (11 morceaux)
    *[("Di-Meh", "Slimka")] * 11,

    ("Di-Meh", "Laylow"),           # "Western Union"
    ("Di-Meh", "Roméo Elvis"),      # "Ride"
    ("Disiz", "Orelsan"),           # "Go Go Gadget"

    # Freeze Corleone × Kalash Criminel  — 3 morceaux
    *[("Freeze Corleone", "Kalash Criminel")] * 3,

    ("Freeze Corleone", "Ninho"),   # "Dictionnaire"
    ("Gazo", "Hamza"),              # "Drill FR5"

    # Gazo × Ninho  — "C'est carré le S", "Mauvais 2x"
    *[("Gazo", "Ninho")] * 2,

    # Gazo × Tiakola  (13 morceaux)
    *[("Gazo", "Tiakola")] * 13,

    ("Gazo", "Werenoi"),            # "La Famine"
    ("Gazo", "Orelsan"),            # "Optimale"

    # Le classico organisé
    ("Gazo", "SCH"), ("Gazo", "PLK"), ("PLK", "SCH"),

    # Hamza × Josman  — "Sloppy Toppy", "B!tch"
    *[("Hamza", "Josman")] * 2,

    ("Hamza", "Laylow"),            # "Window Shopper Part 2"
    ("Hamza", "Ninho"),             # "Elle m'a dit"

    # Hamza × PLK  — "Pilote", "En mieux"
    *[("Hamza", "PLK")] * 2,

    ("Josman", "Laylow"),           # "Brûle"

    # Josman × Kalash Criminel  — "Yémen pt1" + "Free Congo"
    *[("Josman", "Kalash Criminel")] * 2,

    # Free Congo  — Josman, Kalash Criminel, Damso, Ninho
    ("Josman", "Damso"),
    ("Kalash Criminel", "Damso"),
    ("Josman", "Ninho"),
    ("Kalash Criminel", "Ninho"),
    ("Damso", "Ninho"),

    # Kaaris × Kalash Criminel  — "Arrêt du cœur", "Tchalla"
    *[("Kaaris", "Kalash Criminel")] * 2,

    ("Kalash Criminel", "Ziak"),    # "Zone en personne"
    ("Koba LaD", "Ninho"),          # "La zone"
    ("Laylow", "SCH"),              # "Fallen Angels"
    ("Laylow", "Nekfeu"),           # "Spécial"
    ("Leto", "Ninho"),              # "Tes parents"
    ("Leto", "PLK"),                # "Train de vie"
    ("Leto", "Hamza"),              # "Rodéo Drive"
    ("Lomepal", "Orelsan"),         # "La vérité"

    # Lomepal × Roméo Elvis  — "1000°C", "Billet"
    *[("Lomepal", "Roméo Elvis")] * 2,

    # Makala × Slimka  — "Superwak" + autres
    *[("Makala", "Slimka")] * 2,

    ("Mister V", "PLK"),            # "MPLK", "Jamais"
    ("Nekfeu", "Orelsan"),          # "Zone"

    # Ninho × PLK  — "On sait jamais", "Problèmes"
    *[("Ninho", "PLK")] * 2,

    ("Ninho", "Tiakola"),           # "Vérité", "Elle m'a eu"
    ("Ninho", "Werenoi"),           # "3 singes", "Safari"
    ("SDM", "Tiakola"),             # "J'y pense"
    ("Tiakola", "Werenoi"),         # "Ciao"
]

# Palette de verts pour colorier les cliques (indice 0 = plus grande clique)
PALETTE_VERTS: list[str] = [
    "#006400",  # darkgreen
    "#228B22",  # forestgreen
    "#2E8B57",  # seagreen
    "#3CB371",  # mediumseagreen
    "#66CDAA",  # mediumaquamarine
    "#20B2AA",  # lightseagreen
    "#008080",  # teal
    "#9ACD32",  # yellowgreen
    "#6B8E23",  # olivedrab
]
COULEUR_HORS_CLIQUE = "#87CEEB"  # bleu clair
COULEUR_TOP_COLLAB  = "red"
COULEUR_DIAMETRE    = "purple"


# ---------------------------------------------------------------------------
# Construction du graphe
# ---------------------------------------------------------------------------

def construire_graphe() -> nx.Graph:
    """Construit le graphe pondéré artiste ↔ artiste depuis les données brutes."""
    G = nx.Graph()
    G.add_nodes_from(ARTISTES)

    poids_aretes = Counter(tuple(sorted(paire)) for paire in COLLABORATIONS_BRUTES)
    for (artiste_a, artiste_b), poids in poids_aretes.items():
        G.add_edge(artiste_a, artiste_b, weight=poids)

    return G


def detecter_cliques(G: nx.Graph) -> tuple[
    list[list[str]],
    dict[str, int],
    dict[str, str],
]:
    """
    Détecte toutes les cliques de taille ≥ 3 dans G.

    Retourne
    --------
    grandes_cliques : liste des cliques retenues (ordre quelconque)
    id_clique       : artiste → numéro de clique (1-indexé, priorité aux plus grandes)
    couleur_nœud    : artiste → couleur hexadécimale
    """
    grandes_cliques = [c for c in nx.find_cliques(G) if len(c) >= 3]
    cliques_triees  = sorted(grandes_cliques, key=len, reverse=True)

    id_clique:    dict[str, int] = {}
    couleur_nœud: dict[str, str] = {}

    for numero, clique in enumerate(cliques_triees):
        couleur = PALETTE_VERTS[numero % len(PALETTE_VERTS)]
        for artiste in clique:
            if artiste not in id_clique:   # priorité à la plus grande clique
                id_clique[artiste]    = numero + 1
                couleur_nœud[artiste] = couleur

    return grandes_cliques, id_clique, couleur_nœud


def detecter_ponts(G: nx.Graph, id_clique: dict[str, int]) -> list[tuple[str, str]]:
    """Retourne les arêtes reliant deux cliques différentes (ponts inter-cliques)."""
    return [
        (u, v)
        for u, v in G.edges()
        if u in id_clique and v in id_clique and id_clique[u] != id_clique[v]
    ]


def trouver_diametre(G: nx.Graph) -> tuple[tuple[str, str], int]:
    """
    Calcule le diamètre du graphe par BFS depuis chaque nœud.

    Retourne ((source, cible), distance_maximale).
    """
    distance_max = -1
    extremites   = (None, None)

    for source in G.nodes:
        for cible, distance in nx.shortest_path_length(G, source).items():
            if distance > distance_max:
                distance_max = distance
                extremites   = (source, cible)

    return extremites, distance_max


# ---------------------------------------------------------------------------
# Helpers d'affichage (usage interne)
# ---------------------------------------------------------------------------

def _couleurs_nœuds(G: nx.Graph, couleur_nœud: dict[str, str]) -> list[str]:
    return [couleur_nœud.get(n, COULEUR_HORS_CLIQUE) for n in G.nodes()]


def _top_collabs(G: nx.Graph) -> tuple[list[tuple[str, str]], int]:
    """Retourne (arêtes_de_poids_max, poids_max)."""
    poids_max   = max(d["weight"] for *_, d in G.edges(data=True))
    top_aretes  = [(u, v) for u, v, d in G.edges(data=True) if d["weight"] == poids_max]
    return top_aretes, poids_max


def _construire_legende(
    top_aretes:      list[tuple[str, str]],
    poids_max:       int,
    grandes_cliques: list[list[str]],
) -> list[mpatches.Patch]:
    """Construit la liste de patches pour la légende matplotlib."""
    elements: list[mpatches.Patch] = []

    for u, v in top_aretes:
        elements.append(mpatches.Patch(
            color=COULEUR_TOP_COLLAB,
            label=f"{u} – {v} ({poids_max} feats)",
        ))

    for numero, clique in enumerate(sorted(grandes_cliques, key=len, reverse=True)):
        elements.append(mpatches.Patch(
            color=PALETTE_VERTS[numero % len(PALETTE_VERTS)],
            label=f"C{numero + 1} ({len(clique)} artistes)",
        ))

    elements.append(mpatches.Patch(color=COULEUR_HORS_CLIQUE, label="Hors clique"))
    return elements


def afficher_diametre(G: nx.Graph, pos: dict) -> None:
    """Calcule, affiche en console et trace le chemin diamétral sur la figure courante."""
    (source, cible), distance = trouver_diametre(G)

    print("\n=== Diamètre du graphe ===")
    print(f"Artistes les plus éloignés : {source} ↔ {cible}")
    print(f"Distance : {distance}")
    chemin = nx.shortest_path(G, source, cible)
    print("Chemin : " + " → ".join(chemin))

    nx.draw_networkx_edges(
        G, pos,
        edgelist=list(zip(chemin, chemin[1:])),
        width=5,
        edge_color=COULEUR_DIAMETRE,
        alpha=1,
    )


# ---------------------------------------------------------------------------
# Affichage principal
# ---------------------------------------------------------------------------

def dessiner_graphe(
    G:               nx.Graph,
    grandes_cliques: list[list[str]],
    couleur_nœud:    dict[str, str],
) -> None:
    """Dessine le graphe complet avec nœuds, arêtes pondérées, légende et diamètre."""
    pos = nx.circular_layout(G)
    plt.figure(figsize=(17, 10))

    top_aretes, poids_max = _top_collabs(G)

    # Nœuds
    nx.draw_networkx_nodes(
        G, pos,
        node_size=1400,
        node_color=_couleurs_nœuds(G, couleur_nœud),
        alpha=0.95,
    )

    # Toutes les arêtes (largeur ∝ poids)
    nx.draw_networkx_edges(
        G, pos,
        edgelist=list(G.edges()),
        width=[1 + d["weight"] * 0.7 for *_, d in G.edges(data=True)],
        edge_color="#444444",
        alpha=0.6,
    )

    # Top collabs mis en valeur par-dessus
    nx.draw_networkx_edges(
        G, pos,
        edgelist=top_aretes,
        width=1 + poids_max * 0.7,
        edge_color=COULEUR_TOP_COLLAB,
        alpha=0.95,
    )

    nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")

    plt.legend(
        handles=_construire_legende(top_aretes, poids_max, grandes_cliques),
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=10,
        frameon=True,
        borderaxespad=0.0,
    )

    plt.title("Cartographie d'artistes et leurs featurings — Graphe rap FR", fontsize=20)
    plt.axis("off")
    plt.tight_layout(rect=[0, 0, 0.82, 1])

    afficher_diametre(G, pos)
    plt.show()


# ---------------------------------------------------------------------------
# Point d'entrée public
# ---------------------------------------------------------------------------

def build_graph(show: bool = True) -> tuple[
    nx.Graph,
    list[list[str]],
    dict[str, int],
    list[tuple[str, str]],
]:
    """
    Construit le graphe, détecte cliques et ponts, affiche si demandé.

    Paramètres
    ----------
    show : bool
        Si True, affiche le graphe matplotlib.

    Retourne
    --------
    G               : graphe NetworkX pondéré
    grandes_cliques : liste des cliques de taille ≥ 3
    id_clique       : artiste → numéro de clique
    ponts           : arêtes inter-cliques
    """
    G = construire_graphe()
    grandes_cliques, id_clique, couleur_nœud = detecter_cliques(G)
    ponts = detecter_ponts(G, id_clique)

    if show:
        dessiner_graphe(G, grandes_cliques, couleur_nœud)

    return G, grandes_cliques, id_clique, ponts


if __name__ == "__main__":
    build_graph(show=True)