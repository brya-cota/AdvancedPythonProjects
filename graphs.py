'''
Brya Cota
In this project, I will build a basic Graph data structure from scratch and then use AI to generate implementations for
printing the graph, graph traversal/search, and one advanced graph algorithm. The goal is to practice designing a core
data structure while learning how to effectively prompt, understand, integrate, test, and debug AI-generated code.
'''
# Adding the imports due to Gemini's response for the transversal/shortest path methods
from collections import deque
import heapq

class Graph:
    def __init__(self, is_directed_graph = False):
        # Initialize an empty adjacency list using a dictionary
        self.adjacency_list = {}
        self.directed_graph = is_directed_graph

    def add_vertex(self, vertex):
        # Keeping track of neighbors using a list
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v, weight = None):
        # Adding the edge and storing its weight (if applicable)
        self.adjacency_list[u].append((v, weight))

        # If undirected, adding edge going opposide way
        if not self.directed_graph:
            self.adjacency_list[v].append((u, weight))

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex)
            for edge in self.adjacency_list[vertex]:
                print(edge)

    def testing_graph(self):
        '''
        Undirected
        graph:
        V = {1, 2, 3, 4, 5, 6, 7}
        E = {(1, 2, 4), (1, 5, 5), (1, 6, 8), (2, 6, 4), (2, 7, 9),
             (3, 4, 3), (3, 6, 10), (3, 7, 10), (4, 5, 8), (4, 7, 4), (6, 7, 8)}
        Directed
        graph:
        V = {1, 2, 3, 4, 5}
        E = {(1, 2, 2), (1, 3, 7), (1, 4, 10), (2, 1, 4), (3, 1, 5),
             (3, 2, 1), (3, 5, 7), (4, 3, 1), (5, 1, 9)}
        '''
        # Undirected graph
        graph = Graph(is_directed_graph=False)
        graph.add_vertex('1')
        graph.add_vertex('2')
        graph.add_vertex('3')
        graph.add_vertex('4')
        graph.add_vertex('5')
        graph.add_vertex('6')
        graph.add_vertex('7')

        graph.add_edge('1', '2', 4)
        graph.add_edge('1', '5', 5)
        graph.add_edge('1', '6', 8)
        graph.add_edge('2', '6', 4)
        graph.add_edge('2', '7', 9)
        graph.add_edge('3', '4', 3)
        graph.add_edge('3', '6', 10)
        graph.add_edge('3', '7', 10)
        graph.add_edge('4', '5', 8)
        graph.add_edge('4', '7', 4)
        graph.add_edge('6', '7', 8)

        # Directed graph
        directed_graph = Graph(is_directed_graph=True)
        directed_graph.add_vertex('1')
        directed_graph.add_vertex('2')
        directed_graph.add_vertex('3')
        directed_graph.add_vertex('4')
        directed_graph.add_vertex('5')

        directed_graph.add_edge('1', '2', 2)
        directed_graph.add_edge('1', '3', 7)
        directed_graph.add_edge('1', '4', 10)
        directed_graph.add_edge('2', '1', 4)
        directed_graph.add_edge('3', '1', 5)
        directed_graph.add_edge('3', '2', 1)
        directed_graph.add_edge('3', '5', 7)
        directed_graph.add_edge('4', '3', 1)
        directed_graph.add_edge('5', '1', 9)

        # Print undirected graph
        print("-----------------\nUndirected Graph\n-----------------")

        # print ASCII Representation
        graph.print_ascii_graph()
        # Print BFS Order
        order = graph.bfs('1')
        print("BFS Traversal Order:", order)
        # Print shortest path of undirected graph
        distance, path = graph.dijkstra('1', '7')
        print(f"Shortest Distance: {distance}")
        print(f"Path Taken: {' -> '.join(path)}")

        # Print directed graph
        print("\n-----------------\nDirected Graph\n-----------------")

        # print ASCII Representation
        directed_graph.print_ascii_graph()
        # Print BFS Order
        order = directed_graph.bfs('1')
        print("BFS Traversal Order:", order)
        # Print shortest path of undirected graph
        distance, path = directed_graph.dijkstra('1', '5')
        print(f"Shortest Distance: {distance}")
        print(f"Path Taken: {' -> '.join(path)}")

    '''
    _________________________________________
    METHODS CREATED USING GOOGLE GEMINI
    _________________________________________
    '''
    def print_ascii_graph(self):
        """Prints a clean ASCII representation of the adjacency list."""
        print("--- ASCII Graph Representation ---")

        # Determine the arrow style based on graph type
        arrow = "-->" if self.directed_graph else "<-->"

        for vertex, edges in self.adjacency_list.items():
            # Format each neighbor: "Neighbor(weight)" or just "Neighbor" if weight is None
            edge_strs = []
            for neighbor, weight in edges:
                if weight is not None:
                    edge_strs.append(f"{neighbor}(w:{weight})")
                else:
                    edge_strs.append(str(neighbor))

            # Join all neighbors with the appropriate arrow
            if edge_strs:
                connections = f" {arrow} " + f" {arrow} ".join(edge_strs)
            else:
                connections = " (No connections)"

            print(f"[{vertex}]{connections}")
        print("----------------------------------")

        ### NEW BREADTH-FIRST TRAVERSAL METHOD ###
    def bfs (self, start_vertex):
        """Performs a Breadth-First Search starting from start_vertex."""
        if start_vertex not in self.adjacency_list:
            print(f"Vertex {start_vertex} not found in the graph.")
            return []

        # Track visited nodes to prevent infinite loops
        visited = set()
        # Queue for managing the BFS layers
        queue = deque([start_vertex])
        # List to store the order of traversal
        traversal_order = []

        # Mark the starting node as visited
        visited.add(start_vertex)

        while queue:
            # Pop the front vertex from the queue
            current_vertex = queue.popleft()
            traversal_order.append(current_vertex)

            # Look at all neighbors of the current vertex
            for neighbor, weight in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    ### NEW DIJKSTRA'S ALGORITHM METHOD ###
    def dijkstra(self, start_vertex, target_vertex):
        """Finds the shortest path and distance between start_vertex and target_vertex."""
        if start_vertex not in self.adjacency_list or target_vertex not in self.adjacency_list:
            print("Start or target vertex not found in graph.")
            return None, []

        # 1. Initialize distances with infinity, start node with 0
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[start_vertex] = 0

        # 2. Track the "parent" of each node to reconstruct the path later
        previous_vertices = {vertex: None for vertex in self.adjacency_list}

        # 3. Priority queue stores tuples: (distance, vertex)
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            # Pop the vertex with the smallest tentative distance
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # Optimization: If we reached our target, we can stop early
            if current_vertex == target_vertex:
                break

            # If we found a shorter path to this node already, skip it
            if current_distance > distances[current_vertex]:
                continue

            # Check neighbors
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                # If a shorter path to the neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        # 4. Reconstruct the shortest path from target back to start
        path = []
        current = target_vertex
        while current is not None:
            path.append(current)
            current = previous_vertices[current]
        path.reverse()  # Reverse to get start -> target order

        # If the start vertex isn't at the beginning, it means target is unreachable
        if path[0] != start_vertex:
            return float('inf'), []

        return distances[target_vertex], path

g = Graph()
g.testing_graph()

# # MY testing objects
# print("Undirected Graph\n-------------")
# graph = Graph(directed_graph = False)
# graph.add_vertex('A')
# graph.add_vertex('B')
# graph.add_vertex('C')
#
# graph.add_edge('A','B',1)
# graph.add_edge('B','C',6)
# graph.add_edge('A','C',2)
#
# graph.print_graph()

# print("\nDirected Graph\n-------------")
# directed_graph = Graph(is_directed_graph= True)
# directed_graph.add_vertex('D')
# directed_graph.add_vertex('E')
# directed_graph.add_vertex('F')
#
# directed_graph.add_edge('D','E',3)
# directed_graph.add_edge('E','F',10)
# directed_graph.add_edge('F','D',5)
#
# directed_graph.print_graph()

'''
---------------------------
AI GENERATED TEST SCRIPTS
---------------------------
'''
# # Create an undirected graph with weights
# g = Graph(directed_graph=False)
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_edge('A', 'B', 5)
# g.add_edge('A', 'C', 3)
# g.add_edge('B', 'D', 2)
# g.add_vertex('E') # Isolated vertex
#
# g.print_ascii_graph()
#
# g = Graph(directed_graph=False)
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_vertex('E')
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'E')
#
# # Perform BFS starting from 'A'
# order = g.bfs('A')
# print("BFS Traversal Order:", order)
#
# g = Graph(directed_graph=False)
# g.add_vertex('A')
# g.add_vertex('B')
# g.add_vertex('C')
# g.add_vertex('D')
# g.add_edge('A', 'B', 6)
# g.add_edge('A', 'C', 2)
# g.add_edge('C', 'B', 1)  # A -> C -> B is shorter (3) than A -> B (6)
# g.add_edge('B', 'D', 5)
# g.add_edge('C', 'D', 8)
#
# # Find the shortest path from 'A' to 'D'
# distance, path = g.dijkstra('A', 'D')
#
# print(f"Shortest Distance: {distance}")
# print(f"Path Taken: {' -> '.join(path)}")
