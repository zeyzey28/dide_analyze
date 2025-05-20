"""
Shortest Path Algorithm Implementation using Dijkstra's algorithm.
This module provides functions to find the shortest path between nodes in a graph.
"""
import heapq
from typing import Dict, List, Tuple, Any, Set, Optional


def dijkstra(graph: Dict[Any, Dict[Any, float]], start: Any) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
    """
    Implements Dijkstra's algorithm to find shortest paths from a starting node.
    
    Args:
        graph: A dictionary representing the graph where keys are nodes and values are dictionaries
               of neighboring nodes and their edge weights.
        start: The starting node.
    
    Returns:
        A tuple containing:
        - A dictionary of shortest distances from start to each node.
        - A dictionary of predecessors for each node.
    """
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Initialize predecessors
    predecessors = {node: None for node in graph}
    
    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]
    
    # Set to keep track of nodes whose shortest paths have been found
    visited: Set[Any] = set()
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if we've already processed this node
        if current_node in visited:
            continue
        
        # Mark the node as visited
        visited.add(current_node)
        
        # If the current distance is greater than the stored distance, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the new distance
            distance = current_distance + weight
            
            # If we found a shorter path to the neighbor
            if distance < distances[neighbor]:
                # Update the distance
                distances[neighbor] = distance
                # Update the predecessor
                predecessors[neighbor] = current_node
                # Add to priority queue
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors


def get_shortest_path(graph: Dict[Any, Dict[Any, float]], start: Any, end: Any) -> Tuple[Optional[List[Any]], Optional[float]]:
    """
    Finds the shortest path between start and end nodes in a graph.
    
    Args:
        graph: A dictionary representing the graph.
        start: The starting node.
        end: The destination node.
    
    Returns:
        A tuple containing:
        - The shortest path as a list of nodes (None if no path exists).
        - The total distance of the path (None if no path exists).
    """
    # Get distances and predecessors using Dijkstra's algorithm
    distances, predecessors = dijkstra(graph, start)
    
    # If the end node is not reachable from the start node
    if distances[end] == float('infinity'):
        return None, None
    
    # Reconstruct the path from end to start
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = predecessors[current]
    
    # Reverse the path to get it from start to end
    path.reverse()
    
    return path, distances[end]


def create_graph_from_edges(edges: List[Tuple[Any, Any, float]]) -> Dict[Any, Dict[Any, float]]:
    """
    Creates a graph from a list of edges.
    
    Args:
        edges: A list of tuples (node1, node2, weight) representing the edges.
    
    Returns:
        A dictionary representing the graph.
    """
    graph = {}
    
    for u, v, weight in edges:
        # Add node u if not already in the graph
        if u not in graph:
            graph[u] = {}
        
        # Add node v if not already in the graph
        if v not in graph:
            graph[v] = {}
        
        # Add edge from u to v with weight
        graph[u][v] = weight
    
    return graph 