import networkx as nx

def find_cliques_and_bridges(G):
    cliques = list(nx.find_cliques(G))
    big_cliques = [c for c in cliques if len(c) >= 3]

    clique_ids = {i+1: c for i, c in enumerate(big_cliques)}

    node_clique_map = {}
    for cid, members in clique_ids.items():
        for n in members:
            node_clique_map[n] = cid

    bridge_edges = []
    for u, v in G.edges():
        if u in node_clique_map and v in node_clique_map:
            if node_clique_map[u] != node_clique_map[v]:
                bridge_edges.append((u, v))

    return clique_ids, node_clique_map, bridge_edges
