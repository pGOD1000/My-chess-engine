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

 def corretpositionalmove(self):
   return self.depth(None, 1)
 
 def evaluationFunction(self):
   compt = 0
   for i in range(64):
     compt+=self.squarenumbers(ch.SQUARES[i])
     compt += self.mateOppurtunity() + self.opening() + 10*br.board()

   def enpassant(self):
     compt = 0
     for i in range(4,5):
       compt+=self.squarenumbers(ch.SQUARES[i])
       compt += self.enpassantposition() + self.middlegame.opening.endgame() + 10*br.board() 