import sys


class Node():
    def __init__(self, state, parent, action):
       self.state = state
       self.parent = parent
       self.action = action


class StackFrontier():
    def __init_(self):
      self. frontier = []

    def add (self, node) :
        self. frontier. append (node)

def contains_state(self, state):
    return any (node.state == state for node in self. frontier)

def empty (self): 
    return len (self. frontier) == 0
def remove (self) :
    if self. empty():
        raise Exception ("empty frontier")
    else:
         node = self. frontier [-1]
    self. frontier = self. frontier [:-1]
    return node


class QueueFrontier (StackFrontier): 
    def remove (self) :
        if self. empty():
            raise Exception ("empty frontier") 
        else:
            node = self. frontier [0]
            self. frontier = self. frontier [1:]
            return node
class Maze():
    def _init_(self, filename) :

#Read file and set height and width of maze 
        with open(filename) as f:
             contents = f. read ( )

#validate start and goal 
        if contents.count("A") != 1:
           raise Exception ("maze must have exactly one start point")
        if contents. count ("B") != 1:
           raise Exception ("maze must have exactly one goal")
        

#Determine height and width of maze
        contents = contents. splitlines ()
        self.height = len (contents)
        self.width = max(len(line) for line in contents)
                         

#keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents [i][j] == "A":
                        self.start = (i, j)
                        row. append (False)
                    elif contents [i] [j] == "B":
                        self.goal = (i. j)
                        row. append (False)
                    elif contents [i][j] = " ":
                        row.append (False)
            else:
                 row. append (True)
        except IndexError:
        row.append (False)
      self. walls.append (row) # type: ignore
    self.solution = None # type: ignore

def print (self):
    solution = self. solution[1] if self. solution is not None else None
print ( )
for i, row in enumerate (self.walls): # type: ignore
    for j, col in enumerate (row):
        if col:
            print(" ", end="")
        elif (i,j) == self.start: # type: ignore
            print ("A"), end="""""" 
        elif(i,j) == self. goal: # type: ignore
            print ("B", end="")
        elif solution is not None and (i, j) in solution: # type: ignore
           print ("*", end="*")
        else:
            print(" ", end="")
        print ()
    print ()

    def neighbors (self, state):
        row, col = state


# all possible actions
candidates = [
("up", (row - 1, col)), 
("down", (row + 1, col)), 
("left" , (row, col - 1)),
("right", (row, col + 1))]

        #Ensure actions are valid
results = []
for actions, (r,c) in candidates:
    try:
        if not self.walls[r][c]: # type: ignore
          results. append ((action, (r, c))) # type: ignore
    except IndexError:
      continue
return results 

def solve(self) :
     """Finds a solution to maze, if one exsits""" 

#kepp track of number of states explored
self. num_explored = 0


#Initialize frontier to just the starting position
start = Node(state=self.start, parent=None, action=None)
frontier = StackFrontier ()
frontier. add (start)

# Initialize an empty explored set
self.explored = set () # type: ignore

#Keep Looping until a solution found 
while True:
#if nothing left in frontier, then no path 
  if frontier. empty() :
    raise Exception ("no solution")
  
# choose a node from the frontier
node = frontier. remove ()
self.num_explored += 1

#if node is th goal then we have the solution

if node.state == self.goal:
    actions = []
    cells =[]

    #follow parents nodes to find solutions 
    while node. parent is not None: 
             actions. append (node. action)
             cells. append (node.state)
             node = node. parent
             actions. reverse()
             cells. reverse()
             self. solution = (action. cells)
             return

            #Mark node as explored
    self. explored. add (node. state)

#add neighbors to frontier
    for action ,state in self. neighbors (node.state) :
        if not frontier. contains_state(state) and state not in self. explored:
            child = Node (state=state, parent=node, action=action)
            frontier. add (child)