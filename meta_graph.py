# meta_graphe.py
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from graph_artistes import build_graph


def build_meta_graph():
    G, big_cliques, id_clique, ponts = build_graph(show=False)

    M = nx.Graph()  # Méta-graphe

    # ----------------------------
    # 1. Noeuds = cliques
    # ----------------------------
    clique_id_map = {}   # "C1" -> [artistes]

    for i, clique in enumerate(big_cliques, start=1):
        cid = f"C{i}"
        M.add_node(cid, size=len(clique))
        clique_id_map[cid] = clique

    # ----------------------------
    # 2. Arêtes = ponts inter-cliques
    # ----------------------------
    added_edges = set()

    for u, v in ponts:
        cu = id_clique[u]
        cv = id_clique[v]

        if cu != cv:
            c1 = f"C{cu}"
            c2 = f"C{cv}"

            if (c1, c2) not in added_edges and (c2, c1) not in added_edges:
                M.add_edge(c1, c2)
                added_edges.add((c1, c2))

    return M, clique_id_map


def draw_meta_graph():
    M, clique_id_map = build_meta_graph()

    pos = nx.spring_layout(M, seed=42)

    plt.figure(figsize=(17, 10))

    # Taille des noeuds proportionnelle à la taille de la clique
    sizes = [1200 + (M.nodes[n]["size"] * 300) for n in M.nodes()]

    # --- Noeuds ---
    nx.draw_networkx_nodes(
        M, pos,
        node_size=sizes,
        node_color="#2E8B57",
        alpha=0.95
    )

    # --- Arêtes (ponts) ---
    nx.draw_networkx_edges(
        M, pos,
        width=3,
        edge_color="red",
        alpha=0.9
    )

    # --- Labels ---
    nx.draw_networkx_labels(
        M, pos,
        font_size=12,
        font_weight="bold",
        font_color="white"
    )

    # ----------------------------
    # LÉGENDE GRAPHIQUE
    # ----------------------------
    legend_elements = [
        mpatches.Patch(color="#2E8B57", label="Clique (méta-noeud)"),
        mpatches.Patch(color="red", label="Pont inter-clique"),
    ]

    plt.legend(
        handles=legend_elements,
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),
        fontsize=11,
        frameon=True
    )

    # ----------------------------
    # LÉGENDE TEXTUELLE (composition des cliques)
    # ----------------------------
    legend_text = "Composition des cliques :\n\n"
    for cid, artists in clique_id_map.items():
        legend_text += f"{cid} ({len(artists)} artistes) :\n"
        legend_text += "  - " + ", ".join(sorted(artists)) + "\n\n"

    plt.gcf().text(
        0.01, 0.5,
        legend_text,
        fontsize=10,
        va='center'
    )

    plt.title("MÉTA-GRAPHE DES CLIQUES — Réseau abstrait", fontsize=20)
    plt.axis("off")
    plt.tight_layout(rect=[0.25, 0, 0.82, 1])
    plt.show()


if __name__ == "__main__":
    draw_meta_graph()