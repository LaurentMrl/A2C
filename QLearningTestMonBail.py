import numpy as np
from random import randint
import random

class EnvGrid(object):
    def __init__(self):
        self.y = 2
        self.x = 0

        self.grid = [
            [0, 0, 1],
            [0, -1, 0],
            [0, 0, 0]
        ]

        self.actionsDict = {"up" : [-1, 0], "down" : [1, 0], "left": [0, -1], "right": [0, 1]}

        self.actions = [
            [-1, 0], # Up
            [1, 0], #Down
            [0, -1], # Left
            [0, 1] # Right
        ]

    def reset(self):
        # Reset les coordonnées pour un nouvel essai
        self.y = 2
        self.x = 0
        return (self.y*3+self.x+1)

    def step(self, action):
        print(action)
        self.y = self.y + self.actions[action][0]
        self.x = self.x + self.actions[action][1]

        return (self.y*3+self.x+1) , self.grid[self.y][self.x]

    def show(self):
        print("---------------------")
        y = 0
        for line in self.grid:
            x = 0
            for pt in line:
                print("%s\t" % (pt if y != self.y or x != self.x else "X"), end="")
                x += 1
            y += 1
            print("")

    def is_finished(self):
        return self.grid[self.y][self.x] == 1

def take_action(st, Q, eps):
    moves = ["up", "down", "left", "right"]
    bannedMoves = []
    if random.uniform(0, 1) < eps:
        if st == 1 or st == 4 or st == 7:
            bannedMoves.append("left")
        if st == 3 or st == 6 or st == 9:
            bannedMoves.append("right")
        if st == 1 or st == 2 or st == 3:
            bannedMoves.append("up")
        if st == 7 or st == 8 or st == 9:
            bannedMoves.append("down")
        for move in bannedMoves:
            if move in moves:
                moves.remove(move)
        action = randint(0, len(moves)-1)
        action = moves[action]
        action = list(env.actionsDict.keys()).index(action)
    else: # Or greedy action
        # isActionGood = False
        # while isActionGood == False:
        action = np.argmax
        action = np.argmax(Q[st])
        print(action)
            # moves = ["up", "down", "left", "right"]
            # bannedMoves = []
            # if st == 1 or st == 4 or st == 7 and action ==:
            #     bannedMoves.append("left")
            # if st == 3 or st == 6 or st == 9:
            #     bannedMoves.append("right")
            # if st == 1 or st == 2 or st == 3:
            #     bannedMoves.append("up")
            # if st == 7 or st == 8 or st == 9:
            #     bannedMoves.append("down")
            # for move in bannedMoves:
            #     if move in moves:
            #         moves.remove(move)

    return action

if __name__ == '__main__':
    env = EnvGrid()
    st = env.reset()

    Q = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for _ in range(70):
        st = env.reset()
        print("Start new loop")
        while not env.is_finished():
            at = take_action(st, Q, 0.8)


            stp1, r = env.step(at)


            atp1 = take_action(stp1, Q, 0.0)
            Q[st][at] = Q[st][at] + 0.1*(r + 0.9*Q[stp1][atp1] - Q[st][at])

            st = stp1

    for s in range(1, 10):
        print(s, Q[s])