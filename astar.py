import operator
import os


class Maze:

    def __init__(self, maze_contents, m_width, m_height, start_state, goal_state, visited):
        self.maze_contents = maze_contents
        self.m_width = m_width
        self.m_height = m_height
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = visited


def import_maze():
    file = open("maze4.txt", "r")
    maze_f = file.read()
    maze_f = maze_f.splitlines()
    m_height = len(maze_f)
    m_width = len(maze_f[0])
    for i in range(m_height):
        for j in range(m_width):
            if maze_f[i][j] == "B":
                goal = [i, j, 0]
            elif maze_f[i][j] == "A":
                start = [i, j, 0]

    arr = []
    temp = []
    for i in range(0, m_width):
        temp.append(0)
    for i in range(0, m_height):
        temp2 = temp.copy()
        arr.append(temp2)
    m = Maze(maze_f, m_width, m_height, start, goal, arr)
    return m


class Node:

    def __init__(self, parent, state, action):
        self.parent = parent
        self.state = state
        self.action = action
        self.heu_val = 99


class Frontier:

    def __init__(self):
        self.frontier = []

    def expand_frontier(self, parent, maze_obj):
        maze_obj.visited[parent.state[0]][parent.state[1]] = 1
        front.frontier.remove(parent)
        possibilities = []
        possibilities.clear()
        parent.state[2] = 1
        print(parent.state)
        if maze_obj.maze_contents[parent.state[0]][parent.state[1] + 1] == " " \
                and maze_obj.visited[parent.state[0]][parent.state[1] + 1] != 1:
            temp_state = [parent.state[0], parent.state[1] + 1, 0]
            temp_node_1 = Node(parent, temp_state, "rt")
            possibilities.append(temp_node_1)
        elif maze_obj.maze_contents[parent.state[0]][parent.state[1] + 1] == "B":
            solved(parent, maze_obj)

        if maze_obj.maze_contents[parent.state[0]][parent.state[1] - 1] == " " \
                and maze_obj.visited[parent.state[0]][parent.state[1] - 1] != 1:
            temp_state = [parent.state[0], parent.state[1] - 1, 0]
            temp_node_2 = Node(parent, temp_state, "lf")
            possibilities.append(temp_node_2)
        elif maze_obj.maze_contents[parent.state[0]][parent.state[1] - 1] == "B":
            solved(parent, maze_obj)

        if maze_obj.maze_contents[parent.state[0] + 1][parent.state[1]] == " " \
                and maze_obj.visited[parent.state[0] + 1][parent.state[1]] != 1:
            temp_state = [parent.state[0] + 1, parent.state[1], 0]
            temp_node_3 = Node(parent, temp_state, "dn")
            possibilities.append(temp_node_3)
        elif maze_obj.maze_contents[parent.state[0] + 1][parent.state[1]] == "B":
            solved(parent, maze_obj)

        if maze_obj.maze_contents[parent.state[0] - 1][parent.state[1]] == " " \
                and maze_obj.visited[parent.state[0] - 1][parent.state[1]] != 1:
            temp_state = [parent.state[0] - 1, parent.state[1], 0]
            temp_node_4 = Node(parent, temp_state, "up")
            possibilities.append(temp_node_4)
        elif maze_obj.maze_contents[parent.state[0] - 1][parent.state[1]] == "B":
            solved(parent, maze_obj)

        merged_list = possibilities + self.frontier
        for x in list(merged_list):
            if merged_list.count(x) > 1:
                merged_list.remove(x)

        for j in list(merged_list):
            itr = 0
            temp = j
            while temp.parent is not None:
                itr = itr + 1
                temp = temp.parent
            j.heu_val = abs(maze_obj.goal_state[0] - j.state[0]) + abs(maze_obj.goal_state[1]
                                                                       - j.state[
                                                                           1]) + itr
        merged_list.sort(key=operator.attrgetter('heu_val'))
        self.frontier = merged_list


def solved(parent, maze_obj):
    print("\n solution found!")
    input()


def display(parent, maze_obj):
    os.system('cls')
    temp = parent
    path = []
    path.clear()
    solved_grid = ""
    while temp.parent is not None:
        arr = [temp.state[0], temp.state[1]]
        path.append(arr)
        temp = temp.parent
    for n in range(maze_obj.m_height):
        for m in range(maze_obj.m_width):
            star = False
            for o in range(len(path)):
                if path[o][0] == n and path[o][1] == m:
                    star = True
            if star is False:
                solved_grid = solved_grid + maze_obj.maze_contents[n][m]
            else:
                solved_grid = solved_grid + "0"
    for f in range(len(solved_grid)):
        if f % maze_obj.m_width == 0:
            print()
        print(solved_grid[f], end="")
    print()


maze = import_maze()
start_node = Node(None, maze.start_state, None)
front = Frontier()
front.frontier.append(start_node)

while True:
    display(front.frontier[0], maze)
    front.expand_frontier(front.frontier[0], maze)
