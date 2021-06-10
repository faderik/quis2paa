
# import argparse  #FOR CLI PURPOSE
import timeit
from collections import deque

# Global Var
GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None
NodesExpanded = 0 # Number of Nodes Visited
MaxSearchDeep = 0
MaxFrontier = 0
Moves = 0

# Puzzle State
class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)

# BFS Algorithm
def bfs(startState):

    global MaxFrontier, GoalNode, MaxSearchDeep

    boardVisited = set()
    Queue = deque([PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        posiblePaths = subNodes(node)
        for path in posiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            QueueSize = len(Queue)
            MaxFrontier = QueueSize

# DFS Algorithm
def dfs(startState):
    # tobe continued

# Obtain Sub Nodes 
def subNodes(node):
    # tobe continued

# Determine the move direction and limitation
def move(state, direction):
    # tobe continued

def printState(state):
    print("+---+---+---+")
    print("| {} | {} | {} |".format(state[0], state[1], state[2]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(state[3], state[4], state[5]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(state[6], state[7], state[8]))
    print("+---+---+---+")

def prinReq(node):
    # tobe continued

# Main Driver Program
def main():
    print("Quis DAA E 2021 - 8 Puzzle Solver\n")

    # User can input InitialState
    InitialState = [8,6,4,2,1,3,5,7,0]

    print('= GOAL STATE =')
    printState(GoalState)
    print()

    print('INITIAL STATE')
    printState(InitialState)
    print()

    global GoalNode
    global Moves

    startTime = timeit.default_timer()
    
    # Chose One of below Algorithm
    bfs(InitialState)
    # dfs(InitialState)

    time = timeit.default_timer() - startTime
    deep = GoalNode.depth

    print("+++++++++++ PROCESS TO GOAL +++++++++++++++")
    print()
    # prinReq(GoalNode)
    print()
    print("++++++++++++++++ RESULT ++++++++++++++++++++")
    print("Number of Moves : ", str(Moves))
    print("Node Visited : ", str(NodesExpanded))
    print("Search Depth : ", str(deep))
    print("Running Time : ", format(time, '.8f'))
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print()


main()