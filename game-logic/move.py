class ChessRules:
    def __init__(self):
        self.board_size = 8
    
    def is_valid_pawn_move(self, from_row, from_col, to_row, to_col, color):
        """Валидация хода пешки"""
        direction = -1 if color == 'white' else 1
        # Пешка идёт вперёд на 1 клетку
        if to_col == from_col and to_row == from_row + direction:
            return True
        return False
    
    def is_valid_rook_move(self, from_row, from_col, to_row, to_col):
        """Валидация хода ладьи (горизонталь/вертикаль)"""
        return from_row == to_row or from_col == to_col
    