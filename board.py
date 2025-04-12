class HexBoard:
    def __init__(self, size: int):
        self.size = size  # Tamaño N del tablero (NxN)
        self.board = [[0 for _ in range(size)] for _ in range(size)]  # Matriz NxN (0=vacío, 1=Jugador1, 2=Jugador2)
    
    def clone(self) -> 'HexBoard':
        pass

    def place_piece(self, row: int, col: int, player_id: int) -> bool:
        pass

    def get_possible_moves(self) -> list:
        pass
    
    def check_connection(self, player_id: int) -> bool:
        pass