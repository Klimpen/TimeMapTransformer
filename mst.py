

class MST:
    def __init__(self, root):
        self.root = root
        visited = []
        to_visit = {}
        to_visit.update({0: self.root})
        
        while to_visit:
            next_vertex = None
            next_vertex_distance = 1000