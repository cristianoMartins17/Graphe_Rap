import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from collections import Counter

def build_graph(show):
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

        # Alpha Wann / Nekfeu : tout les feats que je connais (hors groupe 1995, screw, etc)
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),
        ("Alpha Wann", "Nekfeu"),

        # Alpha Wann / Freeze Corleone : "Rap Catéchisme" + "ny à fond"
        ("Alpha Wann", "Freeze Corleone"),
        ("Alpha Wann", "Freeze Corleone"),

        # Alpha Wann / Laylow : "STUNTMEN" , "Vamonos"
        ("Alpha Wann", "Laylow"),
        ("Alpha Wann", "Laylow"),

        # Angèle / Damso : "Silence", "Démons, "Tout tenter" 
        ("Angèle", "Damso"),
        ("Angèle", "Damso"),
        ("Angèle", "Damso"),

        # "Angèle / Orelsan : "Evidemment"
        ("Angèle", "Orelsan"),

        # "Angèle / Gazo : "Notre dame"
        ("Angèle", "Gazo"),

        # "Angèle / Tiakola : "Notre dame"
        ("Angèle", "Tiakola"),

        # Angèle / Roméo Elvis : "Tout Oublier", "J’ai vu"
        ("Angèle", "Roméo Elvis"),
        ("Angèle", "Roméo Elvis"),

        # Booba / Damso : "Pinocchio", "Paris c’est loin", "113"
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

        # Damso / Hamza : "God Bless", "BXL ZOO" "Nocif"
        ("Damso", "Hamza"),
        ("Damso", "Hamza"),
        ("Damso", "Hamza"),

        # Damso / Laylow : "R9RLine" 
        ("Damso", "Laylow"),

        # Damso / Nekfeu : "Tricheurs" 
        ("Damso", "Nekfeu"),

        # Damso / Orelsan : "Rêves bizarres" 
        ("Damso", "Orelsan"),

        # Damso / Gazo : "La Rue" "Bodies"
        ("Damso", "Gazo"),
        ("Damso", "Gazo"),

        # Di-Meh / Makala : "Mortal kombat" "Golden" "depeche mode"
        ("Di-Meh", "Makala"),
        ("Di-Meh", "Makala"),
        ("Di-Meh", "Makala"),

        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),
        ("Di-Meh", "Slimka"),

        # Di-Meh / Laylow : "Western Union"
        ("Di-Meh", "Laylow"),

        # Di-Meh / Roméo Elvis : "Ride"
        ("Di-Meh", "Roméo Elvis"),

        # Disiz / Orelsan : "Go Go Gadget" 
        ("Disiz", "Orelsan"),

        # Freeze Corleone / Kaaris : "Encore des problèmes", "Braquage à l'africaine pt5", "Apocalypse"
        ("Freeze Corleone", "Kalash Criminel"),
        ("Freeze Corleone", "Kalash Criminel"),
        ("Freeze Corleone", "Kalash Criminel"),

        # Freeze Corleone / Ninho : "Dictionnaire"
        ("Freeze Corleone", "Ninho"),

        # Freeze Corleone / Gazo : "Drill FR4"
        # Gazo / Hamza : "Drill FR5"
        ("Gazo", "Hamza"),

        # Gazo / Ninho : "C'est carré le S" "Mauvais 2x"
        ("Gazo", "Ninho"),
        ("Gazo", "Ninho"),

        # Gazo / Tiakola : 
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),
        ("Gazo", "Tiakola"),

        # Gazo / Werenoi : "La Famine"
        ("Gazo", "Werenoi"),

        # Gazo / Orelsan : "Optimale"
        ("Gazo", "Orelsan"),

        # "Le classico organisé"
        ("Gazo", "SCH"),
        ("Gazo", "PLK"),
        ("PLK", "SCH"),

        # Hamza / Josman : "Sloppy toppy" "B!tch"
        ("Hamza", "Josman"),
        ("Hamza", "Josman"),

        # Hamza / Laylow : "Window shopper Part 2"
        ("Hamza", "Laylow"),

        # Hamza / Ninho : "elle m'as dit"
        ("Hamza", "Ninho"),

        # Hamza / PLK : "Pilote" "En mieux"
        ("Hamza", "PLK"),
        ("Hamza", "PLK"),

        # Josman / Laylow : "Brule"
        ("Josman", "Laylow"),

        # Josman /Kalash Criminel : "Yemen pt1"
        ("Josman", "Kalash Criminel"),

        # Josman / Kalash Criminel / Damso : ensemble sur "Free Congo"
        ("Josman", "Kalash Criminel"),
        ("Josman", "Damso"),
        ("Kalash Criminel", "Damso"),
        ("Josman", "Ninho"),
        ("Kalash Criminel", "Ninho"),
        ("Damso", "Ninho"),
        
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
    
    # Recherche du poids maximum
    max_weight = max(d["weight"] for (_, _, d) in edges)

    # Liste des duos ayant ce poids
    top_collabs = [(u, v, d["weight"]) for (u, v, d) in edges if d["weight"] == max_weight]

    # Artistes à mettre en avant
    top_artists = set()
    for u, v, w in top_collabs:
        top_artists.add(u)
        top_artists.add(v)

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

    id_clique = {}      # artiste -> id_clique
    node_color_map = {}       # artiste -> couleur

    sorted_cliques = sorted(clique_ids.items(), key=lambda x: len(x[1]), reverse=True)

    for i, (cid, clique) in enumerate(sorted_cliques):
        color = green_palette[i % len(green_palette)]
        for artist in clique:
            if artist not in id_clique:   # priorité aux grosses cliques
                id_clique[artist] = cid
                node_color_map[artist] = color
                print(f"Clique {i} ({len(clique)} artistes) : {clique} -> color {color}")

    # détection des "ponts" (arêtes qui relient des cliques différentes) pour les colorier en rouge 
    ponts = []

    for u, v in G.edges():
        if u in id_clique and v in id_clique:
            if id_clique[u] != id_clique[v]:
                ponts.append((u, v))

    # 🟢 : nœuds
    # ⚪ : liens normaux
    # 🔴 : ponts inter-cliques
    # 🟣 : numéros de cliques
    pos = nx.circular_layout(G) 
    plt.figure(figsize=(17, 10))

    # Liste des duos ayant ce poids
    top_collabs = [(u, v) for (u, v, d) in edges if d["weight"] == max_weight]

    # Artistes à mettre en avant
    top_artists = set()
    for u, v in top_collabs:
        top_artists.add(u)
        top_artists.add(v)

    # Couleurs des nœuds
    node_colors = []
    for n in G.nodes():
        if n in node_color_map:
            node_colors.append(node_color_map[n])
        else:
            node_colors.append("#87CEEB")  # bleu clair pour les artistes hors cliques


    # --- Couche 1 : nœuds ---
    nx.draw_networkx_nodes(
        G, pos,
        node_size=1400,
        node_color=node_colors,
        alpha=0.95
    )

    # --- Couche 2 : toutes les arêtes (pondérées) ---
    edges = G.edges(data=True)

    # Recherche du poids maximum
    max_weight = max(d["weight"] for (_, _, d) in edges)


    # largeur proportionnelle au poids
    widths = [1 + d["weight"] * 0.7 for (_, _, d) in edges]

    nx.draw_networkx_edges(
        G, pos,
        edgelist=G.edges(),
        width=widths,
        edge_color="#444444",
        alpha=0.6
    )

    # --- Labels artistes ---
    nx.draw_networkx_labels(
        G, pos,
        font_size=9,
        font_weight="bold"
    )

    # Artistes les plus connectés entre eux
    nx.draw_networkx_edges(
        G, pos,
        edgelist=top_collabs,
        width=1 + max_weight * 0.7,
        edge_color="red",
        alpha=0.95
    )

    ######################################
    legend_elements = []

    for (u, v) in top_collabs:
        label = f"{u} – {v} ({max_weight} feats)"
        legend_elements.append(
            mpatches.Patch(color="red", label=label)
        )

    for i, (cid, clique) in enumerate(sorted_cliques):
        color = green_palette[i % len(green_palette)]
        label = f"C{cid} ({len(clique)} artistes)"
        legend_elements.append(mpatches.Patch(color=color, label=label))

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

    if show:
        plt.title("Cartographie d'artistes et leurs featurings — Graphe rap FR", fontsize=20)
        plt.axis("off")
        plt.tight_layout(rect=[0, 0, 0.82, 1])
        plt.show()

    return G, big_cliques, id_clique, ponts

if __name__ == "__main__":
    G, big_cliques, id_clique, ponts = build_graph(show=True)