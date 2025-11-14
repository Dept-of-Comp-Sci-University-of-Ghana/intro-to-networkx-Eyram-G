import networkx as nx
import matplotlib.pyplot as plt

# Create an undirected graph
G = nx.Graph()

# Add nodes
nodes = ["Ernest", "Mark", "Charlse", "Priscilla", "Dela", "Kojo", "Eyra"]
G.add_nodes_from(nodes)

# Add edges (relationships)
edges = [
    ("Ernest", "Mark"),
    ("Mark", "Charlse"),
    ("Ernest", "Priscilla"),
    ("Priscilla", "Dela"),
    ("Dela", "Ernest"),
    ("Dela", "Kojo"),
    ("Mark", "Eyra")
]
G.add_edges_from(edges)

# Compute graph metrics
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
isolated_nodes = list(nx.isolates(G))
degree_dict = dict(G.degree())

# Print metrics
print("Graph Metrics")
print(f"Number of Nodes: {num_nodes}")
print(f"Number of Edges: {num_edges}")
print(f"Isolated Nodes: {isolated_nodes if isolated_nodes else 'None'}\n")

print("Degree Distribution")
for node, degree in degree_dict.items():
    print(f"{node}: Degree {degree}")

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=10)
plt.title("Group Alpha")
plt.show()