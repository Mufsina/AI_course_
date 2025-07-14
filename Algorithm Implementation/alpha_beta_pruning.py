def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0 or isinstance(node, int):
        return node
    if maximizing:
        max_eval = float('-inf')
        for child in node:
            eval = alpha_beta(child, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:
            eval = alpha_beta(child, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
