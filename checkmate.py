"""This simple python script gets pawn coordinates and rival's king coordinates as inputs,
   and returns number of possible promotions of the pawn to checkmate the king.
   Chess board squares are represented as x,y indexes, starting from 1 and ending on index 8."""

from collections import namedtuple

def move_pawn(chess_obj):
	"""Promotes the pawn"""
    return chess_obj.coors[0]+1,chess_obj.coors[1]

def initBoard(pawn_coor,king_coor):
	"""Initializes the chess board"""
	ChessObj = namedtuple('ChessObj', ['symbol','coors'])
	Pawn = ChessObj('P',pawn_coor)
	Bishop = ChessObj('B',move_pawn(Pawn))
	Queen = ChessObj('Q',move_pawn(Pawn))
	Knight = ChessObj('N',move_pawn(Pawn))
	Rook = ChessObj('R',move_pawn(Pawn))
	BlackKing = ChessObj('k',king_coor)
	return [BlackKing,Bishop,Queen,Knight,Rook]


def move_generator(chess_obj):
	"""Generates possible moves according to chess object given."""
    xPos = chess_obj.coors[0]
    yPos = chess_obj.coors[1]
    lateral_moves,diag_moves,moves = [],[],[]
    if chess_obj.symbol == 'Q':
        lateral_moves = [(xPos,yPos+i) for i in range(1,9-yPos) if in_board(chess_obj.coors)]
        lateral_moves.extend([(xPos,yPos-i) for i in range(yPos)])
        lateral_moves.extend([(xPos-i,yPos) for i in range(1,xPos) if in_board(chess_obj.coors)])
        diag_moves = [(xPos-i,yPos+i) for i in range(1,9-yPos) if in_board(chess_obj.coors)]
        diag_moves.extend([(xPos-i,yPos-i) for i in range(yPos)])
        moves = lateral_moves
        moves.extend(diag_moves)
        return moves
    elif chess_obj.symbol == 'R':
         lateral_moves = [(xPos,yPos+i) for i in range(1,9-yPos) if in_board(chess_obj.coors)]
         lateral_moves.extend([xPos,yPos-i] for i in range(yPos))
         lateral_moves.extend([(xPos-i,yPos) for i in range(1,xPos) if in_board(chess_obj.coors)])
         return lateral_moves
    elif chess_obj.symbol == 'B':
         diag_moves = [(xPos-i,yPos+i) for i in range(1,9-yPos) if in_board(chess_obj.coors)]
         diag_moves.extend([(xPos-i,yPos-i) for i in range(yPos)])
         return diag_moves


def calc_range(chess_obj):
	"""Calculates possible moves of a chess object. Returns a list of x,y tuples"""
    possible_moves = []
    x,y = chess_obj.coors
    if chess_obj.symbol == 'N':
        possible_moves.extend(list(filter(in_board,[(x-2,y-1),(x-1,y-2),(x-2,y+1),(x-1,y+2)])))
    else:
        possible_moves.extend(list(filter(in_board,move_generator(chess_obj))))
    
    return possible_moves


def in_board(pos_tuple):
	"""Checks if the possible move is within chess board boundaries"""
    return True if (0 < pos_tuple[0] < 9) and (0 < pos_tuple[1] < 9) else False


if __name__ == "__main__":
    px,py = raw_input().split()
    kx,ky = raw_input().split()
    px,py = int(px),int(py)
    kx,ky = int(kx),int(ky)
    pawn_coor = (px,py)
    king_coor = (kx,ky)

    BlackKing = initBoard(pawn_coor,king_coor)[0]
    promotions = initBoard(pawn_coor,king_coor)[1:]

    counter = 0
    for obj in promotions:
    	if BlackKing.coors in calc_range(obj):
    		counter += 1
    print counter
