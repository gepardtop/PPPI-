#ИИ для шахмат: Minimax алгоритм уровни 1-100
class ChessAI:
    def __init__(self, difficulty=1):  # 1-100 уровень
        self.depth = min(difficulty, 6)  # Ограничение глубины
    
    def minimax(self, board, depth, alpha, beta, maximizing):
        """Minimax с альфа-бета отсечением"""
        if depth == 0:
            return self.evaluate_board(board)
        
        if maximizing:
            max_eval = -float('inf')
            for move in board.legal_moves:
                board.make_move(move)
                eval_score = self.minimax(board, depth-1, alpha, beta, False)
                board.undo_move()
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            # Аналогично для минимизирующего игрока
            pass