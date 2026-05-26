import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# ---------------------------------------------------------
# BFS FUNCTION (Algorithm Requirement)
# ---------------------------------------------------------
def manual_bfs(G, start_node):
    distances = {start_node: 0}
    queue = deque([start_node])
    while queue:
        current = queue.popleft()
        for neighbor in G.neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances

# ---------------------------------------------------------
# BIOLOGICAL DATABASE (Destinations kept in DB but ignored in graph)
# ---------------------------------------------------------
protein_db = {
    "Insulin": ["Rough_ER", "Golgi_Apparatus"], "Hemoglobin": ["Free_Ribosome", "Cytosol"],
    "Collagen": ["Rough_ER", "Extracellular_Space"], "Actin": ["Free_Ribosome", "Cytoskeleton"],
    "Myosin": ["Free_Ribosome", "Cytoskeleton"], "Keratin": ["Free_Ribosome", "Intermediate_Filaments"],
    "Tubulin": ["Free_Ribosome", "Microtubules"], "Albumin": ["Rough_ER", "Golgi_Apparatus"],
    "Ferritin": ["Free_Ribosome", "Cytosol"], "Helicase": ["Free_Ribosome", "Nucleus"],
    "Polymerase": ["Free_Ribosome", "Nucleus"], "Lactase": ["Rough_ER", "Cell_Membrane"],
    "Amylase": ["Rough_ER", "Secretory_Vesicle"], "Pepsin": ["Rough_ER", "Gastric_Pit"],
    "Trypsin": ["Rough_ER", "Pancreatic_Acinus"], "Antibody": ["Rough_ER", "Blood_Plasma"],
    "Rhodopsin": ["Rough_ER", "Retinal_Membrane"], "Histone_Protein": ["Free_Ribosome", "Nucleus"],
    "Myoglobin": ["Free_Ribosome", "Muscle_Cytosol"], "Fibrin": ["Rough_ER", "Blood_Plasma"]
}

# ---------------------------------------------------------
# USER INPUTS & EPIGENETIC LOGIC
# ---------------------------------------------------------
print("\n" + "="*50)
target = input("Enter target protein name (e.g., Insulin, Actin, Tubulin): ").strip().capitalize()
if target not in protein_db: 
    print("Protein not found. Defaulting to Insulin.")
    target = "Insulin"

print("\n--- Epigenetic Regulation State ---")
print("1. Acetylation (Gene ON - Allows Transcription)")
print("2. Methylation (Gene OFF - Represses Transcription)")
reg_choice = input("Select regulation state (1 or 2): ").strip()

# Set Biological State
gene_on = (reg_choice == '1')
epigenetic_label = "Acetylation (Gene ON)" if gene_on else "Methylation (Gene OFF)"

# ---------------------------------------------------------
# CONSTRUCT DIRECTED GRAPH
# ---------------------------------------------------------
G = nx.DiGraph()

# 1. Core Pathway
core_nodes = ["Transcription_Factor", "Promoter", "Target_Gene", "mRNA"]
for i in range(len(core_nodes)-1):
    G.add_edge(core_nodes[i], core_nodes[i+1])

# 2. Add branching pathways (Terminates at the Protein)
G.add_edge("mRNA", "Rough_ER")
G.add_edge("mRNA", "Free_Ribosome")

for prot, path in protein_db.items():
    G.add_edge(path[0], prot)  # Ribosome synthesizes -> Protein ONLY

# 3. Epigenetic Regulatory Loop 
G.add_edge("Histone_Complex", "Target_Gene")

# ---------------------------------------------------------
# DEFINE THE ACTIVE PATH LOGIC
# ---------------------------------------------------------
if gene_on:
    # Path: TF -> Promoter -> Target Gene -> mRNA -> Ribosome -> Protein
    active_path_nodes = ["Transcription_Factor", "Promoter", "Target_Gene", "mRNA", 
                         protein_db[target][0], target]
else:
    # If Methylation (OFF), path hits a brick wall
    active_path_nodes = ["Transcription_Factor", "Promoter", "Target_Gene"]
    
active_edges = list(zip(active_path_nodes, active_path_nodes[1:]))

# ---------------------------------------------------------
# STATIC COORDINATES (Clean, Spacious Layout)
# ---------------------------------------------------------
pos = {
    "Transcription_Factor": (0, 0),
    "Promoter":             (3, 0),
    "Target_Gene":          (6, 0),
    "mRNA":                 (9, 0),
    "Rough_ER":             (12, 10),
    "Free_Ribosome":        (12, -10),
    "Histone_Complex":      (6, 4)
}

# Dynamically space the upper hemisphere 
er_prots = [p for p, path in protein_db.items() if path[0] == "Rough_ER"]
for i, p in enumerate(er_prots):
    y_pos = 20 - (i * 2.5)
    pos[p] = (16, y_pos) # Terminate at Final Protein

# Dynamically space the lower hemisphere
free_prots = [p for p, path in protein_db.items() if path[0] == "Free_Ribosome"]
for i, p in enumerate(free_prots):
    y_pos = -4 - (i * 2.5)
    pos[p] = (16, y_pos) # Terminate at Final Protein

# ---------------------------------------------------------
# VISUALIZATION RENDERING
# ---------------------------------------------------------
# Canvas adjusted to 22x14 for perfect centering after removing the destination column
plt.figure(figsize=(22, 14), facecolor='#121212') 
ax = plt.gca()
ax.set_facecolor('#121212')

# Define background elements
background_nodes = [n for n in G.nodes() if n not in active_path_nodes and n != "Histone_Complex"]
reg_edges = [("Histone_Complex", "Target_Gene")]
background_edges = [e for e in G.edges() if e not in active_edges and e not in reg_edges]

# 1. Draw Background
nx.draw_networkx_nodes(G, pos, nodelist=background_nodes, node_color='#333333', node_size=800, edgecolors='#555555')
nx.draw_networkx_edges(G, pos, edgelist=background_edges, edge_color='#444444', 
                       arrowstyle='-|>', arrowsize=15, width=1.5)

# 2. Draw Active Path
nx.draw_networkx_nodes(G, pos, nodelist=active_path_nodes, node_color='red', node_size=1200, edgecolors='white', linewidths=2)
nx.draw_networkx_edges(G, pos, edgelist=active_edges, edge_color='red', width=3.5, arrowstyle='-|>', arrowsize=25)

# 3. Draw Epigenetic Regulation
reg_color = '#00FF00' if gene_on else '#FF0000'
reg_style = 'solid' if gene_on else 'dashed'

nx.draw_networkx_nodes(G, pos, nodelist=["Histone_Complex"], node_color=reg_color, node_size=1400, edgecolors='white')
nx.draw_networkx_edges(G, pos, edgelist=[("Histone_Complex", "Target_Gene")], 
                       edge_color=reg_color, style=reg_style, width=4, arrowstyle='-|>', arrowsize=25)

plt.text(pos["Histone_Complex"][0] + 1.0, pos["Histone_Complex"][1], epigenetic_label, 
         color=reg_color, fontsize=11, fontweight='bold', ha='left', va='center',
         bbox=dict(facecolor='#121212', edgecolor=reg_color, boxstyle='round,pad=0.3'))

# 4. Draw Node Labels
nx.draw_networkx_labels(G, pos, font_size=8, font_color='white', font_weight='bold')

# 5. Documentation and Title
title_status = "SUCCESSFUL SYNTHESIS" if gene_on else "SYNTHESIS ABORTED (Gene Silenced)"
plt.title(f"Gene Regulatory Network | Target: {target}\nStatus: {title_status}", 
          color='white', fontsize=18, fontweight='bold', pad=20)

path_string = " -> ".join(active_path_nodes)
plt.text(0.5, 0.02, f"ACTIVE PATH: {path_string}", transform=plt.gca().transAxes, 
        ha='center', fontsize=12, fontweight='bold', color='red',
        bbox=dict(facecolor='#222222', edgecolor='red', boxstyle='round,pad=0.5'))

plt.axis('off')

# ---------------------------------------------------------
# TERMINAL OUTPUT FOR REPORT
# ---------------------------------------------------------
print("\n" + "="*50)
print(f"--- NODE DEGREE METRICS FOR REPORT ---")
print(f"{'Node Name':<25} | {'In-Degree':<10} | {'Out-Degree':<10}")
for node in sorted(G.nodes()):
    print(f"{node:<25} | {G.in_degree(node):<10} | {G.out_degree(node):<10}")
print("="*50 + "\n")

plt.show(block=True)