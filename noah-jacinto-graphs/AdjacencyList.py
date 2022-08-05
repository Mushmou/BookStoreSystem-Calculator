"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        l = self.adj[i]

        for k in range(0, len(l)):
            if l.get(k) == j:
                l.remove(k)
                return

    def has_edge(self, i : int, j: int) ->bool:
        l = self.adj[i]

        for k in range(0, len(l)):
            if l.get(k) == j:
                return True

        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, j) -> List:
        out = ArrayList.ArrayList()

        for i in range(0, self.n):
            if self.has_edge(i, j):
                out.append(i)

        return out

    def bfs(self, r :int):
        seen = ArrayList.ArrayList()
        for i in range(0, self.n):
            seen.append(False)

        q = ArrayQueue.ArrayQueue()
        bfs_order = ArrayQueue.ArrayQueue()

        q.add(r)
        bfs_order.add(r)
        seen[r] = True

        while q.size() > 0:
            current_node = q.remove()
            adjacent_nodes = self.out_edges(current_node)

            for current_adj_node in range(0, len(adjacent_nodes)):
                node = adjacent_nodes.get(current_adj_node)

                if seen[node] == False:
                    q.add(node)
                    bfs_order.add(node)
                    seen[node] = True

        print(bfs_order)
        return bfs_order

    def dfs(self, r :int):
        seen = ArrayList.ArrayList()
        for i in range(0, self.n):
            seen.append(False)

        s = ArrayStack.ArrayStack()
        dfs_order = ArrayQueue.ArrayQueue()

        s.push(r)
        dfs_order.add(r)

        while s.size() > 0:
            current_node = s.pop()

            if  current_node not in dfs_order:
                dfs_order.add(current_node)

            if seen[current_node] == False:
                seen[current_node] = True
                adjacent_nodes = self.out_edges(current_node)

                for current_adj_node in range(0, len(adjacent_nodes)):
                    node = adjacent_nodes.get(current_adj_node)
                    s.push(node)

        print(dfs_order)
        return dfs_order

    def shortest_path(self, r :int):
        seen = ArrayList.ArrayList()
        for i in range(0, self.n):
            seen.append(False)

        parent = ArrayList.ArrayList()
        for i in range(0, self.n):
            parent.append(None)

        q = ArrayQueue.ArrayQueue()

        q.add(r)
        parent[r] = r
        seen[r] = True

        while q.size() > 0:
            current_node = q.remove()
            adjacent_nodes = self.out_edges(current_node)

            for current_adj_node in range(0, len(adjacent_nodes)):
                node = adjacent_nodes.get(current_adj_node)

                if seen[node] == False:
                    q.add(node)
                    parent[node] = current_node
                    seen[node] = True

        return parent

    def distance(self, r : int, dest: int):
        path = self.shortest_path(r)
        d = 0

        while dest != path[dest]:
            dest = path[dest]
            d += 1

        return d

    def size(self) -> int :
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))

'''

# q = AdjacencyList(7)
#
# q.add_edge(0,1)
# q.add_edge(0,3)
# q.add_edge(1,3)
# q.add_edge(1,5)
# q.add_edge(2,1)
# q.add_edge(2,6)
# q.add_edge(3,5)
# q.add_edge(3,4)
# q.add_edge(4,0)
# q.add_edge(4,6)
# q.add_edge(5,2)
# q.add_edge(6,3)
# q.add_edge(6,5)
# #
# print(q)
# print("the parent array :", q.shortest_path(0))
# print(q.distance(5, 5))
