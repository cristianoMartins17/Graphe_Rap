import networkx as nx
import matplotlib.pyplot as plt
from meta_graph import load_meta_graph

def draw_meta_graph():
    metaG = load_meta_graph("data/meta_graphe.gpickle")

    pos = nx.spring_layout(metaG, seed=42)

    node_sizes = [metaG.nodes[n]["size"] * 1200 for n in metaG.nodes()]
    edge_widths = [metaG[u][v]["weight"] * 2 for u, v in metaG.edges()]

    plt.figure(figsize=(12, 10))

    nx.draw_networkx_nodes(metaG, pos, node_size=node_sizes)
    nx.draw_networkx_edges(metaG, pos, width=edge_widths)

    labels = {n: f"{n}\n({metaG.nodes[n]['size']} artistes)" for n in metaG.nodes()}
    nx.draw_networkx_labels(metaG, pos, labels=labels)

    plt.title("Méta-graphe des scènes")
    plt.axis("off")
    plt.savefig("outputs/meta_graphe.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    draw_meta_graph()