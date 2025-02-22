import random

class Node:
    def __init__(self, a, b, z):
        self.x = a
        self.y = b
        self.depth = z

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = random.randint(4, 7)
        self.source = None
        self.goal = None
        self.goal_level = 999999
        self.state = 0
        
        self.grid = []
        for i in range(self.N):
            row = []
            for j in range(self.N):
                row.append(random.choice([0, 1]))
            self.grid.append(row)
        
        self.path = []
        self.topo_order = []
        
    def generate_valid_positions(self):
        valid_positions = [(x, y) for x in range(self.N) for y in range(self.N) if self.grid[x][y] == 1]
        return random.sample(valid_positions, 2)
    
    def init(self):
        while True:
            source_x, source_y, goal_x, goal_y = *self.generate_valid_positions()[0], *self.generate_valid_positions()[1]
            if (source_x, source_y) != (goal_x, goal_y):
                break
        
        self.source = Node(source_x, source_y, 0)
        self.goal = Node(goal_x, goal_y, self.goal_level)
        
        print("Generated Grid:")
        for row in self.grid:
            print(row)
        print(f"Source: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")
        
        self.st_dfs(self.source)
        
        if self.found:
            print("Goal found")
            print("DFS Path:", self.path)
            print("Topological Order of Traversal:", self.topo_order)
            print("Number of moves required =", self.goal.depth)
        else:
            print("Goal cannot be reached from the starting block")
    

    
    def st_dfs(self, u):
        self.grid[u.x][u.y] = 0
        self.path.append((u.x, u.y))
        self.topo_order.append((u.x, u.y))
        
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            
            if 0 <= v_x < self.N and 0 <= v_y < self.N and self.grid[v_x][v_y] == 1:
                v_depth = u.depth + 1                
                if (v_x, v_y) == (self.goal.x, self.goal.y):
                    self.found = True
                    self.goal.depth = v_depth
                    self.path.append((v_x, v_y))
                    return
                
                child = Node(v_x, v_y, v_depth)
                self.st_dfs(child)
                
                if self.found:
                    return

if __name__ == "__main__":
    d = DFS()
    d.init()
