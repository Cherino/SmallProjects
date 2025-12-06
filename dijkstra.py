import networkx as nx  # NetworkX library for graph operations

# Original stops (nodes in the graph)
stops = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
#print("Nodes:", stops)

# Edge weights: each is a tuple (distance in meters, speed in km/h)
edge_weights = [(130,5),(30,5),(30,48),(50,5),(140,5),(140,48),(80,5),(40,5),(550,5),(550,48),(660,5),(380,5),(475,5),(475,64),(85,5),(360,5)]
#print("Weights (dist, speed):", edge_weights)

# Delay biases: all except bus boarding at A2 have (0,1) min delay
delay_biases = [(0,1)] * 16  # Initialize all to (0,1)
delay_biases[2] = (0, 25)  # max delay for bus boarding at A2 is 25 min
#print("Biases (min, max):", delay_biases)

# (start_node, end_node, weight_index, transport_mode)
all_edges = [
    # Walking edges
    ('A1', 'A2', 0, 'Walk'),
    ('A2', 'A3', 1, 'Walk'),
    ('A2', 'A4', 3, 'Walk'),
    ('A3', 'A5', 4, 'Walk'),#(parallel to bus)
    ('A4', 'A6', 6, 'Walk'),
    ('A5', 'A6', 7, 'Walk'),
    ('A5', 'A7', 8, 'Walk'),#(parallel to bus)
    ('A6', 'A9', 10, 'Walk'),
    ('A7', 'A8', 11, 'Walk'),
    ('A7', 'A10', 12, 'Walk'),#(parallel to bus)
    ('A8', 'A9', 14, 'Walk'),
    ('A10', 'A8', 15, 'Walk'),
    # Bus edges, added space so they appear aligned in output
    ('A2', 'A3b', 2, 'Bus '),
    ('A3b', 'A5b', 5, 'Bus '),
    ('A5b', 'A7b', 9, 'Bus '),
    ('A7b', 'A10b', 13, 'Bus '),
    # Exit edges
    ('A3b', 'A3', None, 'Exit'),
    ('A5b', 'A5', None, 'Exit'),
    ('A7b', 'A7', None, 'Exit'),
    ('A10b', 'A10', None, 'Exit')
]

def optimal_route(raw_path):
    cleaned_path = [raw_path[0]]  # Start with the source node
    for current_node in raw_path[1:]:  # Iterate over subsequent nodes
        isbus_stop = current_node[:-1] if current_node.endswith('b') else current_node
        if isbus_stop != cleaned_path[-1]:
            cleaned_path.append(isbus_stop)
    return cleaned_path  # Return the simplified path

def dijkstra_shortest_path(bias_case):
    """
    Compute the shortest path using Dijkstra's algorithm using NetworkX.
    Naming Convention: G (graph), source (start), target (goal), distance_to_target (total weight), path (node sequence via predecessors).
    Modeils travel time + delay as edge weights; enforces bus-only-from-A2 via dedicated nodes.
    """
    # Initialize the graph G (G = (V, E))
    G = nx.DiGraph()
    
    # Add all nodes: original stops + bus-only nodes (A3b, A5b, etc.)
    bus_only_nodes = [stop + 'b' for stop in ['A3', 'A5', 'A7', 'A10']]  # 'b' for bus-exclusive
    all_nodes = stops + bus_only_nodes  # V = set of all vertices
    G.add_nodes_from(all_nodes)  # Explicitly add vertices to G
    
    # Source vertex s (start: A1), target vertex t (goal: A8)
    source = 'A1'
    target = 'A8'
    
    # Iterate over all edges to add them to G with computed weights
    for start_node, end_node, weight_idx, transport_mode in all_edges:
        if transport_mode == 'Exit':
            # Exit edges: zero cost)
            edge_weight = 0
        else:
            # Non-exit edges: compute weight w(u,v) = travel_time + delay
            distance_m, speed_kmh = edge_weights[weight_idx]  # Fetch (dist, speed) for this edge
            min_delay, max_delay = delay_biases[weight_idx]  # Fetch (min, max) delay for this edge
            # Select delay based on case: optimistic (min) or pessimistic (max)
            selected_delay = min_delay if bias_case == 'min' else max_delay
            # Travel time in minutes: distance / (speed in m/min)
            travel_time = distance_m / (speed_kmh * 1000 / 60)  # Convert km/h to m/min
            edge_weight = travel_time + selected_delay  # Total weight for Dijkstra
        # Add directed edge (u,v) to E with weight, mode (for later printing)
        G.add_edge(start_node, end_node, weight=edge_weight, mode=transport_mode)
    
    # Run Dijkstra, find shortest path from source to target.
    # Returns path (via implicit predecessors) and distance_to_target (delta(s,t))
    raw_path = nx.shortest_path(G, source, target, weight='weight')  # Node sequence
    distance_to_target = nx.shortest_path_length(G, source, target, weight='weight')  # Total cost
    
    # Round the total distance for readability
    rounded_distance = round(distance_to_target, 2)
    
    # Return G (for edge queries)
    return rounded_distance, raw_path, G

# Compute for best case (min delays: optimistic boarding wait = 0)
best_case_distance, best_raw_path, best_graph = dijkstra_shortest_path('min')
best_optimal_route = optimal_route(best_raw_path)

# Compute for worst case (max delays: pessimistic boarding wait = 25)
worst_case_distance, worst_raw_path, worst_graph = dijkstra_shortest_path('max')
worst_optimal_route = optimal_route(worst_raw_path)

# Print the optimal routes and totals
print("\nBest Case Best Route:", best_optimal_route, f"({best_case_distance} min)")
print("Worst Case Best Route:", worst_optimal_route, f"({worst_case_distance} min)")

def print_route_details(raw_path, graph, case_title):
    print(f"\n{case_title}:")  # Header for this case
    print("Edge  | Mode | Time (min)")  # Table header
    
    # Move across the raw path edge-by-edge
    edge_index = 0  # Current position in path
    while edge_index < len(raw_path) - 1:  # Until second-to-last node
        current_node = raw_path[edge_index]  # u
        next_node = raw_path[edge_index + 1]  # v
        
        # Check if direct edge exists and has positive weight
        if graph.has_edge(current_node, next_node) and graph[current_node][next_node]['weight'] > 0:
            edge_data = graph[current_node][next_node]  # Fetch weight, mode
            # Clean node names: strip 'b' if bus node
            clean_start = current_node[:-1] if current_node.endswith('b') else current_node
            clean_end = next_node[:-1] if next_node.endswith('b') else next_node
            # Print row: edge as "A#-A#", mode padded, time rounded
            print(f"{clean_start}-{clean_end} | {edge_data['mode']:<3} | {round(edge_data['weight'], 2):<8}")
            edge_index += 1  # Move to next real edge
        else:
            edge_index += 1  # Skip

# Print details for best case
print_route_details(best_raw_path, best_graph, "Best Case Route Details")
# Print details for worst case
print_route_details(worst_raw_path, worst_graph, "Worst Case Route Details")