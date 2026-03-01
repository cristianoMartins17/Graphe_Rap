import networkx as nx
import matplotlib.pyplot as plt
from meta_graph import load_meta_graph

metaG = load_meta_graph("data/meta_graphe.gpickle")

pos = nx.spring_layout(metaG, seed=42)

node_sizes = [metaG.nodes[n]["size"] * 1200 for n in metaG.nodes()]
edge_widths = [metaG[u][v]["weight"] * 2 for u, v in metaG.edges()]

plt.figure(figsize=(12, 10))

nx.draw_networkx_nodes(
    metaG, pos,
    node_size=node_sizes,
    node_color="#2E8B57",
    alpha=0.9
)

nx.draw_networkx_edges(
    metaG, pos,
    width=edge_widths,
    alpha=0.7
)

labels = {
    n: f"{n}\n({metaG.nodes[n]['size']} artistes)"
    for n in metaG.nodes()
}

nx.draw_networkx_labels(metaG, pos, labels=labels, font_size=11)

plt.title("Méta-graphe des scènes", fontsize=18)
plt.axis("off")
plt.show()
