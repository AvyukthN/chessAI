class Board:
    # fen strings
    # f1 _/_/_/_/_/_/_/_
    # f2 turn to move - (w or b)
    # f3 castling ability
        # K - white can castle King side
        # Q - white can castle Queen side
        # k - black can castle King side
        # q - black can castle Queen side
    # f4 en passant move ability (- if you cannot make an en passant move)
    # f5 50 move rule - counter starts at 0 and starts counting when a player makes a move that isnt with the pawn or a capture move (resets when the move is one of those 2)
    # f6 move counter (starts as 1 waiting for white to move, when black moves back it goes to 2)

    def __init__(self, starting_fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        self.fen = starting_fen
        self.board = [-1 for i in range(64)]
        self.spaces = '012345678'
        self.pieces = 'rnbqkpRNBQKP'

        self.piece_hash = {}
        for i in range(len(self.pieces)):
            self.piece_hash.update({self.pieces[i]: i})
        self.piece_hash.update({' ': -1})

        self.fen_fill()
     
    def fen_fill(self):
        fen_arr = self.fen.split(' ')[0]
        print(fen_arr)

        index = 0
        for i in range(len(fen_arr)):
            if fen_arr[i] in self.piece_hash.keys():
                self.board[index] = self.piece_hash[fen_arr[i]]
                index += 1
            elif fen_arr[i] in self.spaces:
                index += int(fen_arr[i])

        self.print_board() 
            
    def print_board(self):
        piece_hash = {v: k for k, v in self.piece_hash.items()}

        final_str = '+---+---+---+---+---+---+---+---+\n'
        for i in range(len(self.board)):
            if i % 8 == 0 and i != 0:
                final_str += '|'
                final_str += '\n'
                final_str += '+---+---+---+---+---+---+---+---+'
                final_str += '\n'
            
            if self.board[i] == -1:
                final_str += '| ' + piece_hash[self.board[i]].upper() + ' '
            elif self.board[i] < 6:
                final_str += '|<' + piece_hash[self.board[i]].upper() + '>'
            elif self.board[i] > 5:
                final_str += '|-' + piece_hash[self.board[i]].upper() + '-'

        final_str += '|\n'
        final_str += '+---+---+---+---+---+---+---+---+\n'

        print(final_str)