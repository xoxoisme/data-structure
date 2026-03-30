class graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def __str__(self):
        return str(self.graph)
    
# 예제 사용법:
if __name__ == "__main__":
    g = graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    print(g)
    # 출력: {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}