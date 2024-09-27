import heapq
from typing import Optional

from helpers import Map

import math

def heuristic(a: tuple[float, float], b: tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        a (tuple[float, float]): The coordinates of the first point (x1, y1).
        b (tuple[float, float]): The coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    delta = (b[0] - a[0], b[1] - a[1])
    return math.sqrt(delta[0]**2 + delta[1]**2)

def reconstruct_path(came_from: dict[int, int], current: int) -> list[int]:
    """
    Reconstruct the path from the start node to the goal node.

    Args:
        came_from (dict[int, int]): A dictionary mapping each node to the node it came from.
        current (int): The goal node.

    Returns:
        list[int]: The reconstructed path from the start node to the goal node.
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def shortest_path(M: Map, start: int, goal: int) -> Optional[list[int]]:
    """
    Find the shortest path between two nodes in a map using the A* algorithm.

    Args:
        M (Map): The map containing the graph, intersections, and roads.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        Optional[list[int]]: The shortest path from the start node to the goal node, or None if no path is found.
    """
    came_from = {}
    min_heap = []

    g_score = {node: float('inf') for node in M.intersections}
    f_score = {node: float('inf') for node in M.intersections}
    
    g_score[start] = 0 # g_score of start node is 0
    h_score = heuristic(M.intersections[start],M.intersections[goal])
    f_score[start] = g_score[start] + h_score

    heapq.heappush(min_heap,(f_score[start],start))

    while len(min_heap) > 0:
        _,current = heapq.heappop(min_heap)

        if current == goal:
            return reconstruct_path(came_from , goal)
        
        for neighbor in M.roads[current]:
            neighbor_g_score = heuristic(M.intersections[current],M.intersections[neighbor])
            tentative_g_score = g_score[current] + neighbor_g_score
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                
                g_score[neighbor] = tentative_g_score
                h_score = heuristic(M.intersections[neighbor],M.intersections[goal])
                f_score[neighbor] = g_score[neighbor] + h_score

                if all(neighbor != item[1] for item in min_heap):
                    heapq.heappush(min_heap,(f_score[neighbor],neighbor))

    return None