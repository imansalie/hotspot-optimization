import random
import matplotlib.pyplot as plt
import networkx as nx
import os

# Constants
GRID_SIZE = 100
NUM_HOTSPOTS = 1000
INTERFERENCE_DISTANCE = 5

# Step 1: Generate Hotspot Locations
def generate_hotspots():
    hotspots = set()
    attempts = 0
    while len(hotspots) < NUM_HOTSPOTS:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        hotspots.add((x, y))
        attempts += 1
    print(f"Generated {len(hotspots)} hotspots after {attempts} attempts.")
    return list(hotspots)

# Step 2: Determine Interference
def is_interfering(h1, h2):
    dx = h1[0] - h2[0]
    dy = h1[1] - h2[1]
    return dx * dx + dy * dy <= INTERFERENCE_DISTANCE ** 2

# Step 3: Build Interference Graph
def build_interference_graph(hotspots):
    G = nx.Graph()
    for i, hotspot in enumerate(hotspots):
        G.add_node(i, pos=hotspot)
    for i in range(len(hotspots)):
        for j in range(i + 1, len(hotspots)):
            if is_interfering(hotspots[i], hotspots[j]):
                G.add_edge(i, j)
    return G

# Step 4: Visualize Hotspot Locations
def plot_hotspots(hotspots):
    x_vals = [h[0] for h in hotspots]
    y_vals = [h[1] for h in hotspots]
    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, s=10, c='blue')
    plt.title("Hotspot Locations")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)
    plt.savefig("hotspot_locations.png")  # Save instead of showing
    plt.close()

# Step 5: Visualize Interference Graph
def plot_interference_graph(G):
    pos = nx.get_node_attributes(G, 'pos')
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, node_size=10, edge_color='red')
    plt.title("Interference Graph")
    plt.savefig("interference_graph.png")  # Save instead of showing
    plt.close()

# Step 6: Generate Report
def generate_report(G):
    report_path = "report.txt"
    with open(report_path, "w") as file:
        file.write(f"Total Hotspots: {NUM_HOTSPOTS}\n")
        file.write(f"Total Interfering Pairs: {G.number_of_edges()}\n")
    print(f"Report generated: {report_path}")

# Main Function
def main():
    hotspots = generate_hotspots()
    G = build_interference_graph(hotspots)
    print(f"Initial number of interfering hotspot pairs: {G.number_of_edges()}")
    plot_hotspots(hotspots)
    plot_interference_graph(G)
    generate_report(G)

if __name__ == "__main__":
    main()
