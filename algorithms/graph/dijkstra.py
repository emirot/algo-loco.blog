

def dijkstra(graph):
    start = "A"
    times = {a: float("inf") for a in graph.keys()}
    times[start] = 0
    a = list(times)
    while a:
        node_selected = min(a, key=lambda k: times[k])
        print("node selected", node_selected)
        a.remove(node_selected)
        for node, t in graph[node_selected].items():
            if times[node_selected] + t < times[node]:
                times[node] = times[node_selected] + t
    print(times)

graph = {
    "A": {"B": 4, "D": 3},
    "B": {"C": 1},
    "C": {},
    "D": {"B": 1, "C": 3}
}

dijkstra(graph)
