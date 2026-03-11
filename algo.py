class LocationGame:

    def __init__(self, graph, weights):

        self.graph = graph
        self.weights = weights
        self.n = len(weights)


    def available_moves(self, used):

        moves = []

        for v in range(self.n):

            if v in used:
                continue

            valid = True

            for u in used:
                if v in self.graph[u]:
                    valid = False
                    break

            if valid:
                moves.append(v)

        return moves


    # минимакс 
    def minimax(self, used, turn, p2_score):

        moves = self.available_moves(used)

        # конец игры
        if not moves:
            return p2_score


        # ход P1 
        if turn == 1:

            best = float("inf")

            for v in moves:

                new_used = used.copy()
                new_used.add(v)

                value = self.minimax(new_used, 2, p2_score)

                best = min(best, value)

            return best


        else:

            best = -float("inf")

            for v in moves:

                new_used = used.copy()
                new_used.add(v)

                value = self.minimax(
                    new_used,
                    1,
                    p2_score + self.weights[v]
                )

                best = max(best, value)

            return best


    def p2_has_strategy(self, B):

        result = self.minimax(set(), 1, 0)

        return result >= B


#ПРИМЕР
if __name__ == "__main__":

    graph = {
        0: {1},
        1: {0,2},
        2: {1,3},
        3: {2,4},
        4: {3}
    }

    weights = [10, 1, 5, 15, 5]

    game = LocationGame(graph, weights)

    B = 10

    if game.p2_has_strategy(B):
        print("P2 может гарантировать", B)
    else:
        print("P2 не может гарантировать", B)