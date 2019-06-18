import sys
import random

WALL = "#"
CANDY = "0"
GHOST = "&"
BLANK = "-"
U = "U"
D = "D"
L = "L"
R = "R"

Actions = [U, D, L, R]


class PacMan:

    def __init__(self, args):
        filename = str(args[1])
        file = open(filename, "r")
        line = file.readline()
        (lines, columns) = line.split(" ")

        self.discount = 0.9
        self.grid = []
        self.alpha = float(args[2])
        self.epsilon = float(args[3])
        self.times = int(args[4])
        self.lines = int(lines)
        self.columns = int(columns)
        self.grid = file.readlines()
        file.close()
        for line in range(self.lines):
            self.grid[line] = self.grid[line].replace("\n", "")
        self.show()

    def show(self):
        print()
        for line in self.grid:
            print(line)
        print()


def q_learn(pacman):
    Q = {}
    for line in range(pacman.lines):
        for col in range(pacman.columns):
            item = pacman.grid[line][col]
            if item != WALL and item != GHOST and item != CANDY:
                Q[(line, col, U)] = float(0.000)
                Q[(line, col, D)] = float(0.000)
                Q[(line, col, L)] = float(0.000)
                Q[(line, col, R)] = float(0.000)

    while pacman.times > 0:
        ok = False
        pos = (0, 0)
        while not ok:
            pos = (random.randrange(0, pacman.lines), random.randrange(0, pacman.columns))
            state = pacman.grid[pos[0]][pos[1]]
            if state != WALL and state != GHOST and state != CANDY:
                ok = True

        # pos = (3, 1)
        terminal = False
        while not terminal:
            rand = random.random()
            print(rand, "\n", pos)
            action = U
            # random action
            if rand < pacman.epsilon:
                print("Random action! ", rand)
                action = map_action(random.randrange(0, 4))
                next_pos, reward, terminal = take_action(pacman, pos, action)

            # q learning action
            else:
                action, value = best(Q, pos[0], pos[1])
                print("Best action is ", action, " with value: ", "{:.4f}".format(value))
                next_pos, reward, terminal = take_action(pacman, pos, action)

            # compute q
            best_q = 0
            if terminal:
                best_q = reward
            else:
                next_action, best_q = best(Q, next_pos[0], next_pos[1])

            Q[pos[0], pos[1], action] = float(Q[pos[0], pos[1], action] + pacman.alpha*(
                    reward + pacman.discount * best_q - Q[pos[0], pos[1], action]
            ))
            pos = next_pos

        pacman.times -= 1

    output(Q, pacman)


def take_action(pacman, pos, action):
    new_pos = (-1, -1)
    if action == U:
        new_pos = (pos[0] - 1, pos[1])
    elif action == D:
        new_pos = (pos[0] + 1, pos[1])
    elif action == L:
        new_pos = (pos[0], pos[1] - 1)
    elif action == R:
        new_pos = (pos[0], pos[1] + 1)

    next_state = pacman.grid[new_pos[0]][new_pos[1]]
    print("Next State: ", next_state)
    if next_state == WALL:
        return pos, -1, False
    elif next_state == CANDY:
        return new_pos, 10, True
    elif next_state == BLANK:
        return new_pos, -1, False
    elif next_state == GHOST:
        return new_pos, -10, True


def map_action(number):
    if number == 0:
        return U
    elif number == 1:
        return D
    elif number == 2:
        return L
    elif number == 3:
        return R


def best(Q, line, col):
    highest = Q[(line, col, U)]
    sol = U
    for a in Actions:
        if Q[(line, col, a)] > highest:
            highest = Q[(line, col, a)]
            sol = a

    return sol, highest


def output(Q, pacman):
    q = open("q.txt", "w")
    pi = open("pi.txt", "w")

    for line in range(pacman.lines):
        for col in range(pacman.columns):
            item = pacman.grid[line][col]
            if item == WALL or item == GHOST or item == CANDY:
                pi.write(item)
            else:
                for a in Actions:
                    value = Q[(line, col, a)]
                    q.write(
                        str(line) + "," + str(col) + "," + a + "," + "{:.4f}\n".format(value)
                    )

                sol, value = best(Q, line, col)

                pi.write(sol)
        pi.write("\n")

    pi.close()
    q.close()


def main():
    args = sys.argv
    if len(args) < 5:
        print("Erro na quantidade de entradas")
        exit(1)

    pacman = PacMan(args)
    q_learn(pacman)


if __name__ == "__main__":
    main()
