from collections import defaultdict

class Solution:
    
    def find_ingree_with(self, graph, seen):
        queue = []
        for k, v in graph.items():
            if k not in seen and len(v) == 0:
                queue.append(k)
        return queue
    
    def check_circular(self, graph):
        
        for k, v in graph.items():
            for e in v:
                if e in graph and k in graph[e]:
                    return True
        return False
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {}
        for i in range(0, numCourses):
            graph[i] = []
        
        for dest, source in prerequisites:
            graph[dest].append(source)
            
        seen = set()
        queue = self.find_ingree_with(graph, seen)
        order = []
        if self.check_circular(graph):
            return []
        while queue:
            p = queue.pop(0)
            if p not in seen:
                g = {}
                for i in range(0, numCourses):
                    if graph[i]:
                        graph[i] = [ e for e in graph[i] if e != p]
                        if len(graph[i]) == 0:
                            queue.append(i)
                order.append(p)
                seen.add(p)

        if len(order) != numCourses:
            return []
                
        return order