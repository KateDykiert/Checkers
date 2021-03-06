from Board.Tile import Tile
from Pieces.NullPiece import NullPiece
from Pieces.King import King
from Pieces.Man import Man

class Board:

    gameTiles = {}

    def __init__(self):
        pass

    def createBoard(self):
        for x in range(64):
            self.gameTiles[x] = Tile(x, NullPiece())

        self.gameTiles[1] = Tile(1, Man("Black", 1))
        self.gameTiles[3] = Tile(3, Man("Black", 3))
        self.gameTiles[5] = Tile(5, Man("Black", 5))
        self.gameTiles[7] = Tile(7, Man("Black", 7))
        self.gameTiles[8] = Tile(8, Man("Black", 8))
        self.gameTiles[10] = Tile(10, Man("Black", 10))
        self.gameTiles[12] = Tile(12, Man("Black", 12))
        self.gameTiles[14] = Tile(14, Man("Black", 14))
        self.gameTiles[17] = Tile(17, Man("Black", 17))
        self.gameTiles[19] = Tile(19, Man("Black", 19))
        self.gameTiles[21] = Tile(21, Man("Black", 21))
        self.gameTiles[23] = Tile(23, Man("Black", 23))

        self.gameTiles[40] = Tile(40, Man("White", 40))
        self.gameTiles[42] = Tile(42, Man("White", 42))
        self.gameTiles[44] = Tile(44, Man("White", 44))
        self.gameTiles[46] = Tile(46, Man("White", 46))
        self.gameTiles[49] = Tile(49, Man("White", 49))
        self.gameTiles[51] = Tile(51, Man("White", 51))
        self.gameTiles[53] = Tile(53, Man("White", 53))
        self.gameTiles[55] = Tile(55, Man("White", 55))
        self.gameTiles[56] = Tile(56, Man("White", 56))
        self.gameTiles[58] = Tile(58, Man("White", 58))
        self.gameTiles[60] = Tile(60, Man("White", 60))
        self.gameTiles[62] = Tile(62, Man("White", 62))



    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('|', end = self.gameTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0

