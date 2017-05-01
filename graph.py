# Assuming graph is meant to be undirected
import json


def build_graph(json_graph):
    """
    Build a dictionary of Start -> End destinations with weights
    EG. {'A': {'B': 100, 'C': 30}}
    """
    graph = {}
    for start, destinations in json.loads(json_graph).iteritems():
        if start not in graph:
            graph[start] = {}
        for destination, weight in destinations.iteritems():
            if destination not in graph:
                graph[destination] = {}
            if destination not in graph[start]:
                graph[start][destination] = weight
            if start not in graph[destination]:
                graph[destination][start] = weight
    return graph


def find_route(graph, start, end):
    """Uses Djikstra's to find the route"""
    if start not in graph or end not in graph:
        return None
    weights = {}    # Total distance to get to k from start
    current_route = {}  # K and how we got there V
    unvisited = set(graph.keys())
    unvisited.remove(start)
    visited = set()
    visited.add(start)
    weights[start] = 0

    def update_weights_from_point(point):
        """From the given point update the weight to get to its destinations."""
        for dest, weight in graph[point].iteritems():
            old_weight = weights.get(dest)
            new_weight = weight + weights[point]
            if not old_weight or new_weight < old_weight:
                weights[dest] = new_weight
                current_route[dest] = point

    def pick_next_point():
        """Pick the next unvisited destination with the lowest weight."""
        lowest_weight = 0
        new_point = None
        for point, weight in weights.iteritems():
            if point in unvisited:
                if new_point is None or weight < lowest_weight:
                    lowest_weight = weight
                    new_point = point
        return new_point

    point = start
    while end not in visited:
        update_weights_from_point(point)
        point = pick_next_point()
        visited.add(point)
        unvisited.remove(point)

    # Get the path
    path = [end]
    how_we_got_here = end
    while start not in path:
        how_we_got_here = current_route[how_we_got_here]
        path.append(how_we_got_here)
    path.reverse()

    return path

if __name__ == "__main__":
    json_graph = """
    {
        "A": { "B": 100, "C": 30 },
        "B": { "F": 300 },
        "C": { "D": 200 },
        "D": { "H": 90, "E": 80 },
        "E": { "H": 30, "G": 150, "F":50 },
        "F": { "G": 70 },
        "G": { "H": 50 },
        "H": {}
    }"""

    json_query = '{"start":"A","end":"H"}'
    query = json.loads(json_query)
    print find_route(
        build_graph(json_graph), query.get("start"), query.get("end"))

    # start = raw_input("Specify Starting Location")
    # end = raw_input("Specify Ending Location")
    # print find_route(start, end)
