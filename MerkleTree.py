from pymerkle import InmemoryTree as MerkleTree
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

# Initialize the Merkle Tree
tree = MerkleTree(algorithm='sha256')

# Input total number of transactions
no_names = int(input("How many total transactions?: "))
list_names = []
for n in range(no_names):
    name = input(f'Enter transaction name {n + 1}: ')
    list_names.append(name)

# Initialize dictionaries and lists
dict_entries = {}
list_entries = []

# Append entries to the Merkle Tree and store relevant information
for i, name in enumerate(list_names):
    entry = name.encode('utf-8')
    index = tree.append_entry(entry)  # Leaf index
    list_entries.append(index)
    value = tree.get_leaf(index)  # Leaf hash
    dict_entries[index] = value
    print(f'The input is {index} and hash is {value.hex()[:4]}...')  # Display truncated hash
    if (i + 1) % 2 == 0 and i != 0:
        root_index = (index - 1) // 2
        root_hash = tree.get_state(root_index)
        print(f'The root of {list_entries[i - 1]} and {list_entries[i]} is {root_hash.hex()[:4]}...')  # Display truncated root hash

# Finalize the Merkle Tree
size = tree.get_size()  # Number of leaves
print(f"The total no. of leaves is {size}")
state = tree.get_state(0)  # Current root-hash
print(f"The final root is {state.hex()[:4]}...")  # Display truncated final root hash

# Function to visualize the Merkle Tree using matplotlib and networkx
def visualize_merkle_tree_matplotlib(tree, total_leaves):
    G = nx.DiGraph()  # Directed graph

    # Use a queue for iterative traversal
    queue = deque([(0, 'Root')])  # (current_index, parent_node_id)
    node_labels = {'Root': f'Root: {tree.get_state(0).hex()[:8]}...'}  # Truncated root hash
    levels = {'Root': 0}

    while queue:
        index, parent = queue.popleft()
        current_hash = tree.get_state(index)
        current_hash_str = current_hash.hex()[:8] + "..."  # Truncated hash
        node_id = f'Node {index}'

        # Add the current node to the graph
        G.add_node(node_id, label=current_hash_str)
        if parent != 'Root':
            G.add_edge(parent, node_id)

        # Determine the level for the layout
        current_level = levels[parent] + 1 if parent in levels else 0
        levels[node_id] = current_level

        # Add children to the queue
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < total_leaves:
            queue.append((left_index, node_id))

        if right_index < total_leaves:
            queue.append((right_index, node_id))

    # Add the root node explicitly
    G.add_node('Root', label=f'Root: {tree.get_state(0).hex()[:8]}...')
    levels['Root'] = 0

    # Define the layout for the tree using spring layout
    pos = nx.spring_layout(G, seed=42)  # Use seed for reproducibility

    # Draw the graph
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels=nx.get_node_attributes(G, 'label'),
            node_size=300, node_color='lightblue', font_size=8, font_weight='bold',
            arrows=True, arrowsize=20, edge_color='gray')

    # Draw the plot
    plt.title('Merkle Tree Visualization')
    plt.show()

# Call the matplotlib visualization function
print("\nDisplaying Merkle Tree using matplotlib:")
visualize_merkle_tree_matplotlib(tree, size)