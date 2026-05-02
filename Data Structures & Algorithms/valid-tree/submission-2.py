
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        
        # Create 2 Hashmaps Key->values and values->keys]
        forward = collections.defaultdict(set)
        found = set()

        for edge in edges:
            forward[edge[0]].add(edge[1]) # since acyclic
            forward[edge[1]].add(edge[0])
            found.add(edge[0])
            found.add(edge[1])


        print(forward)
        print(found)

        for current in forward:
            for value in forward[current]:
                if value not in found:
                    return False
                found.remove(value)
                if current in forward[value]:
                    forward[value].remove(current)
            print(found)
            
               
                
        return True




