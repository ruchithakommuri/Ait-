MAX = 1000
MIN = -1000

values = [3, 5, 2, 9, 12, 5, 23, 23]

def minimax(depth, node, maximizing, alpha, beta):
    if depth == 3:
        return values[node]

    if maximizing:
        best = MIN

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        for i in range(2):
            val = minimax(depth + 1, node * 2 + i,
                          True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


result = minimax(0, 0, True, MIN, MAX)

print("Optimal Value:", result)
