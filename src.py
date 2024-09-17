import chess as ch
import board as br

class Pbot:


 def __init__(self, board, depth, enpassant, promotion, capture, check):
    self.board=board
    self.depth=depth
    self.enpassant=enpassant
    self.promotion=promotion
    self.capture=capture
    self.check=check

 def bestmove(self):
   return self.depth(None, 1)
 
 def evalFunction(self):
   compt = 0
   