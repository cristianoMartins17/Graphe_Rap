"""
==============
Construction et affichage du méta-graphe des cliques.

Chaque nœud  = une clique du graphe artistes.
Chaque arête = au moins un pont inter-cliques reliant les deux cliques.
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from graph_artistes import build_graph


# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------

def construire_meta_graphe() -> tuple[nx.Graph, dict[str, list[str]]]:
    """
    Construit le méta-graphe à partir du graphe artistes.

    Retourne
    --------
    M              : méta-graphe (nœuds = cliques, arêtes = ponts inter-cliques)
    composition    : identifiant de clique → liste d'artistes
    """
    G, grandes_cliques, id_clique, ponts = build_graph(show=False)

    M           = nx.Graph()
    composition = {}   # "C1" → [artistes]

    # Nœuds : une clique = un nœud, taille stockée comme attribut
    for numero, clique in enumerate(grandes_cliques, start=1):
        cid = f"C{numero}"
        M.add_node(cid, taille=len(clique))
        composition[cid] = clique

    # Arêtes : un pont inter-cliques = une arête dans M (sans doublon)
    aretes_ajoutees: set[tuple[str, str]] = set()

    for u, v in ponts:
        cid_u = f"C{id_clique[u]}"
        cid_v = f"C{id_clique[v]}"

        paire = tuple(sorted((cid_u, cid_v)))
        if paire not in aretes_ajoutees:
            M.add_edge(cid_u, cid_v)
            aretes_ajoutees.add(paire)

    return M, composition


# ---------------------------------------------------------------------------
# Affichage
# ---------------------------------------------------------------------------

def _legende_composition(composition: dict[str, list[str]]) -> str:
    """Génère le texte de la légende listant la composition de chaque clique."""
    lignes = ["Composition des cliques :\n"]
    for cid, artistes in composition.items():
        lignes.append(f"{cid} ({len(artistes)} artistes) :")
        lignes.append("  " + ", ".join(sorted(artistes)) + "\n")
    return "\n".join(lignes)


def dessiner_meta_graphe() -> None:
    """Construit et affiche le méta-graphe des cliques."""
    M, composition = construire_meta_graphe()

    pos = nx.circular_layout(M)
    plt.figure(figsize=(17, 10))

    # Taille des nœuds proportionnelle au nombre d'artistes dans la clique
    tailles_nœuds = [1200 + M.nodes[n]["taille"] * 300 for n in M.nodes()]

    nx.draw_networkx_nodes(
        M, pos,
        node_size=tailles_nœuds,
        node_color="#2E8B57",
        alpha=0.95,
    )
    nx.draw_networkx_edges(
        M, pos,
        width=3,
        edge_color="red",
        alpha=0.9,
    )
    nx.draw_networkx_labels(
        M, pos,
        font_size=12,
        font_weight="bold",
        font_color="white",
    )

    # Légende graphique (patches)
    plt.legend(
        handles=[
            mpatches.Patch(color="#2E8B57", label="Clique (méta-nœud)"),
            mpatches.Patch(color="red",     label="Pont inter-clique"),
        ],
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=11,
        frameon=True,
    )

    # Légende textuelle (composition des cliques)
    plt.gcf().text(
        0.01, 0.5,
        _legende_composition(composition),
        fontsize=10,
        va="center",
    )

    plt.title("MÉTA-GRAPHE DES CLIQUES — Réseau abstrait", fontsize=20)
    plt.axis("off")
    plt.tight_layout(rect=[0.25, 0, 0.82, 1])
    plt.show()


if __name__ == "__main__":
    dessiner_meta_graphe()