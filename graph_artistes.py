import networkx as nx
from collections import Counter

def build_meta_graph(clique_ids, node_clique_map, bridge_edges):
    metaG = nx.Graph()

    # --- nœuds = cliques ---
    for cid, members in clique_ids.items():
        metaG.add_node(
            f"C{cid}",
            size=len(members),
            members=members
        )

    # --- arêtes = ponts ---
    meta_edges = []

    for u, v in bridge_edges:
        c1 = node_clique_map[u]
        c2 = node_clique_map[v]
        if c1 != c2:
            meta_edges.append((f"C{c1}", f"C{c2}"))

    meta_counts = Counter(tuple(sorted(e)) for e in meta_edges)

    for (c1, c2), w in meta_counts.items():
        metaG.add_edge(c1, c2, weight=w)

    return metaG


def save_meta_graph(metaG, path="data/meta_graphe.gpickle"):
    nx.write_gpickle(metaG, path)


def load_meta_graph(path="data/meta_graphe.gpickle"):
    return nx.read_gpickle(path)
