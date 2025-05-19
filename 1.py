import heapq


class Dijkstra:
    def __init__(self, graph_nodes, start):
        self.arr = graph_nodes
        self.num = start

    def Dijkstra(self):
        total_nodes = len(self.arr)
        distance_tracker = [float('inf')] * total_nodes
        path_origin = [None] * total_nodes
        distance_tracker[self.num] = 0

        process = []
        heapq.heappush(process, (0, self.num))

        while process:
            current_distance, current_node = heapq.heappop(process)

            if current_distance > distance_tracker[current_node]:
                continue

            for neighbor, edge_weight in self.arr[current_node]:
                alternative_route = distance_tracker[current_node] + edge_weight
                if alternative_route < distance_tracker[neighbor]:
                    distance_tracker[neighbor] = alternative_route
                    path_origin[neighbor] = current_node
                    heapq.heappush(process, (alternative_route, neighbor))

        return distance_tracker, path_origin


# Пример использования
road_network = [
    [(1, 1), (3, 2)],  # Узел 0 соединён с узлом 1 (длина 1) и узлом 3 (длина 2)
    [(0, 1), (2, 3), (3, 1)],  # Узел 1
    [(1, 3), (3, 5)],  # Узел 2
    [(0, 2), (1, 1), (2, 5)]  # Узел 3
]

cl = Dijkstra(road_network, 2)
result = cl.Dijkstra()
print(result[0])
print(result[1])
