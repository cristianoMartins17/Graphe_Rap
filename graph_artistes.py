import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter
from meta_graph import build_meta_graph, save_meta_graph

G = nx.Graph()

artistes = [
    "Alpha Wann",
    "Angèle",
    "Booba",
    "Damso",
    "Di-Meh",
    "Disiz",
    "Orelsan",
    "Freeze Corleone",
    "Gazo",
    "Hamza",
    "Josman",
    "Jul",
    "Kaaris",
    "Kalash Criminel",
    "Koba LaD",
    "Laylow",
    "Leto",
    "Lomepal",
    "Makala",
    "Mister V",
    "Nekfeu",
    "Ziak",
    "Djadja & Dinaz",
    "PLK",
    "Roméo Elvis",
    "SCH",
    "SDM",
    "Slimka",
    "Tiakola",
    "Vald",
    "Werenoi",
    "Ninho",
    "Zola",
]
G.add_nodes_from(artistes)

# Liste de collaborations réelles (sans compter les morceaux fictifs / mashups)
raw_collabs = [

    # Alpha Wann / Nekfeu : plusieurs feats ("Flingue et Feu", "Point d'interrogation",
    # "Compte les hommes", "Vinyle", etc.)
    ("Alpha Wann", "Nekfeu"),
    ("Alpha Wann", "Nekfeu"),
    ("Alpha Wann", "Nekfeu"),
    ("Alpha Wann", "Nekfeu"),

    # Alpha Wann / Freeze Corleone : "Rap Catéchisme" + "ny à fond"
    ("Alpha Wann", "Freeze Corleone"),
    ("Alpha Wann", "Freeze Corleone"),

    # Angèle / Damso : "Silence", "Démons, "Tout tenter" 
    ("Angèle", "Damso"),
    ("Angèle", "Damso"),
    ("Angèle", "Damso"),

    # "Angèle / Orelsan : "Evidemment"
    ("Angèle", "Orelsan"),

    # Angèle / Roméo Elvis : "Tout Oublier", "J’ai vu"
    ("Angèle", "Roméo Elvis"),
    ("Angèle", "Roméo Elvis"),

    # Booba / Damso : plusieurs feats ("Pinocchio", "Paris c’est loin", "113") 
    ("Booba", "Damso"),
    ("Booba", "Damso"),
    ("Booba", "Damso"),

    # Booba / Kaaris :  "L.E.F" "Kalash"
    ("Booba", "Kaaris"),
    ("Booba", "Kaaris"),

    # Booba / SDM : plusieurs feats ("La zone", "Daddy", "Bonne journée", "Dolce Camara", "92i")
    ("Booba", "SDM"),
    ("Booba", "SDM"),
    ("Booba", "SDM"),
    ("Booba", "SDM"),
    ("Booba", "SDM"),

    # Damso / Disiz : "RENCONTRES" (feat documenté)
    ("Damso", "Disiz"),

    # Damso / Hamza : plusieurs feats ("God Bless", "BXL ZOO" "Nocif") 
    ("Damso", "Hamza"),
    ("Damso", "Hamza"),

    # Damso / Laylow : "R9RLine" 
    ("Damso", "Laylow"),

    # Damso / Nekfeu : "Tricheurs" 
    ("Damso", "Nekfeu"),

    # Damso / Orelsan : "Rêves bizarres" [web:122][web:124]
    ("Damso", "Orelsan"),

    # Di-Meh / Makala : Superwak Clique, multiples titres ensemble (on pondère à 2) [web:46][web:53]
    ("Di-Meh", "Makala"),
    ("Di-Meh", "Makala"),

    ("Di-Meh", "Slimka"),
    ("Di-Meh", "Slimka"),

    # Disiz / Orelsan : "Go Go Gadget" [web:48][web:51]
    ("Disiz", "Orelsan"),

    # Djadja & Dinaz / Ninho : "J’fais mes affaires" (exemple, un feat confirmé) [web:11]
    ("Djadja & Dinaz", "Ninho"),

    # Djadja & Dinaz / Zola : feat confirmé sur un projet commun [web:11]
    ("Djadja & Dinaz", "Zola"),

    # Freeze Corleone / Kaaris : "IRM"
    ("Freeze Corleone", "Kalash Criminel"),

    # Freeze Corleone / Kalash Criminel : "Rafale", "Chrome" (collabs drill FR) [web:101]
    ("Freeze Corleone", "Kalash Criminel"),

    # Gazo / Hamza : feat sur Mélo ("La Sauce" etc.) [web:131]
    ("Gazo", "Hamza"),

    # Gazo / Ninho : "Mauvais 2x" [web:94][web:97]
    ("Gazo", "Ninho"),

    # Gazo / Tiakola : La mélo est gangx, album commun (on pondère par ex. 3) [web:131][web:137]
    ("Gazo", "Tiakola"),
    ("Gazo", "Tiakola"),
    ("Gazo", "Tiakola"),

    # Gazo / Werenoi : "La Famine", "Obscur" [web:93][web:99][web:102]
    ("Gazo", "Werenoi"),
    ("Gazo", "Werenoi"),

    # Hamza / Josman : feat sur "God Bless" / scènes communes [web:21]
    ("Hamza", "Josman"),

    # Hamza / Laylow : "Dégaine", "Life" (exemple de multiples collabs) [web:21]
    ("Hamza", "Laylow"),
    ("Hamza", "Laylow"),

    # Hamza / Ninho : "Casanova", "No Hook" etc. [web:21]
    ("Hamza", "Ninho"),
    ("Hamza", "Ninho"),

    # Hamza / PLK : "Pilote" (feat avec SCH), au moins un feat confirmé [web:21]
    ("Hamza", "PLK"),

    # Josman / Laylow : "PINEAPPLE", "Mauvais réflexe" (ex.) [web:21]
    ("Josman", "Laylow"),

    # Josman / Makala : Superwak, plusieurs morceaux [web:46][web:53]
    ("Josman", "Makala"),
    ("Josman", "Makala"),

    # Josman / Kalash Criminel / Damso : ensemble sur "Free Congo" [web:92][web:101]
    ("Josman", "Kalash Criminel"),
    ("Josman", "Damso"),

    # Jul / SCH : "Rentrée dans le game", "Bande organisée" etc. [web:4][web:13]
    ("Jul", "SCH"),
    ("Jul", "SCH"),

    # Kaaris / Kalash Criminel : "Arrêt du cœur", "Tchalla" etc. [web:101]
    ("Kaaris", "Kalash Criminel"),
    ("Kaaris", "Kalash Criminel"),

    # Kalash Criminel / Ziak : "Zone en personne" (exemple d’un feat drill) [web:53]
    ("Kalash Criminel", "Ziak"),

    # Koba LaD / Ninho : "La zone" (ex.) [web:98]
    ("Koba LaD", "Ninho"),

    # Laylow / SCH : "Fallen Angels" (ex. collab sur des projets récents) [web:21]
    ("Laylow", "SCH"),

    # Laylow / Nekfeu : "Spécial" [web:21]
    ("Laylow", "Nekfeu"),

    # Leto / Ninho : "Tes parents" (ex.) [web:98]
    ("Leto", "Ninho"),

    # Leto / PLK : "Train de vie" (exemple documenté) [web:104]
    ("Leto", "PLK"),

    # Leto / Hamza : "Rodéo Drive"]
    ("Leto", "Hamza"),

    # Lomepal / Orelsan : "La vérité"
    ("Lomepal", "Orelsan"),

    # Lomepal / Roméo Elvis : "1000°C", "Billet" [web:115][web:118]
    ("Lomepal", "Roméo Elvis"),
    ("Lomepal", "Roméo Elvis"),

    # Makala / Slimka : Superwak, multiples morceaux [web:46][web:53]
    ("Makala", "Slimka"),
    ("Makala", "Slimka"),

    # Mister V / PLK : "MPLK" / "Jamais" etc. [web:71][web:74]
    ("Mister V", "PLK"),

    # Nekfeu / Orelsan : "Zone" (ex. feat commun), plus feat avec S-Crew/Orelsan [web:81][web:84]
    ("Nekfeu", "Orelsan"),

    # Ninho / PLK : "On sait jamais", "Problèmes" (plusieurs feats) [web:104]
    ("Ninho", "PLK"),
    ("Ninho", "PLK"),

    # Ninho / Tiakola : "Vérité", "Elle m’a eu" (ex.) [web:131]
    ("Ninho", "Tiakola"),

    # Ninho / Werenoi : "3 singes", "Safari" (ex.) [web:102]
    ("Ninho", "Werenoi"),

    # Orelsan / Vald : aucun feat officiel studio, seulement scènes / mashups → on ne met pas de poids
    # ("Orelsan", "Vald"),

    # SDM / Tiakola : "J’y pense" [web:131]
    ("SDM", "Tiakola"),

    # Tiakola / Werenoi : "Ciao" (ex.) [web:102]
    ("Tiakola", "Werenoi"),
]

######################################
# Comptage des poids
counts = Counter(tuple(sorted(e)) for e in raw_collabs)

for (a, b), w in counts.items():
    G.add_edge(a, b, weight=w)

# largeur des arêtes proportionnelle au poids
edges = G.edges(data=True)
widths = [1 + d["weight"] * 0.7 for (_, _, d) in edges]

# inactive = {"Nekfeu", "Lomepal", "Roméo Elvis", "Mister V", "Zola"}

######################################
#détection des "cliques" (groupes d'artistes tous connectés entre eux) pour colorier les nœuds en rouge s'ils font partie d'une clique avec au moins 3 artistes
# 🟢 vert foncé → clique 1
# 🟢 vert moyen → clique 2
# 🟢 vert clair → clique 3
# 🔵 bleu → artistes hors cliques

green_palette = [
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
cliques = list(nx.find_cliques(G))
big_cliques = [c for c in cliques if len(c) >= 3]

# Numérotation des cliques
clique_ids = {i: c for i, c in enumerate(big_cliques, 1)}

# dictionnaire artiste -> couleur

node_clique_map = {}      # artiste -> id_clique
node_color_map = {}       # artiste -> couleur

sorted_cliques = sorted(clique_ids.items(), key=lambda x: len(x[1]), reverse=True)

for i, (cid, clique) in enumerate(sorted_cliques):
    color = green_palette[i % len(green_palette)]
    for artist in clique:
        if artist not in node_clique_map:   # priorité aux grosses cliques
            node_clique_map[artist] = cid
            node_color_map[artist] = color
            print(f"Clique {i} ({len(clique)} artistes) : {clique} -> color {color}")

# détection des "ponts" (arêtes qui relient des cliques différentes) pour les colorier en rouge 
bridge_edges = []

for u, v in G.edges():
    if u in node_clique_map and v in node_clique_map:
        if node_clique_map[u] != node_clique_map[v]:
            bridge_edges.append((u, v))

# 🟢 Couche 1 : nœuds
# ⚪ Couche 2 : liens normaux
# 🔴 Couche 3 : ponts inter-cliques
# 🟣 Couche 4 : numéros de cliques
pos = nx.circular_layout(G) 
plt.figure(figsize=(17, 10))

# Couleurs des nœuds
node_colors = []
for n in G.nodes():
    if n in node_color_map:
        node_colors.append(node_color_map[n])
    else:
        node_colors.append("#87CEEB")  # hors clique


# --- Couche 1 : nœuds ---
nx.draw_networkx_nodes(
    G, pos,
    node_size=1400,
    node_color=node_colors,
    alpha=0.95
)

# --- Couche 2 : arêtes normales ---
normal_edges = [e for e in G.edges() if e not in bridge_edges and (e[1], e[0]) not in bridge_edges]

nx.draw_networkx_edges(
    G, pos,
    edgelist=normal_edges,
    width=1.2,
    alpha=0.3
)

# --- Couche 3 : ponts inter-cliques ---
nx.draw_networkx_edges(
    G, pos,
    edgelist=bridge_edges,
    width=3,
    edge_color="red",
    alpha=0.9
)

# --- Labels artistes ---
nx.draw_networkx_labels(
    G, pos,
    font_size=9,
    font_weight="bold"
)

######################################

legend_elements = []

for i, (cid, clique) in enumerate(sorted_cliques):
    color = green_palette[i % len(green_palette)]
    label = f"C{cid} ({len(clique)} artistes)"
    legend_elements.append(mpatches.Patch(color=color, label=label))

# Ponts inter-cliques
legend_elements.append(mpatches.Patch(color="red", label="Pont inter-clique"))

# Hors cliques
legend_elements.append(mpatches.Patch(color="#87CEEB", label="Hors clique"))

plt.legend(
    handles=legend_elements,
    loc="center left",
    bbox_to_anchor=(1.02, 0.5),
    fontsize=10,
    frameon=True,
    borderaxespad=0.
)

plt.title("Cartographie d'artistes et leurs featurings — Graphe rap FR", fontsize=20)
plt.axis("off")
plt.tight_layout(rect=[0, 0, 0.82, 1])
plt.show()

metaG = build_meta_graph(clique_ids, node_clique_map, bridge_edges)
save_meta_graph(metaG)
