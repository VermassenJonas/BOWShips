

from typing import Dict
from logic import Enums as enums
from logic.Ship import Ship
from logic.components.ArmourBelt import ArmourBelt
from logic.components.ArmourDeck import ArmourDeck


class Citadel:
	def __init__(self, ship : Ship) -> None:
		
		self.ship = ship
		
		self.armourBelts : Dict[enums.Belt, ArmourBelt] =  {}
		for belt in enums.Belt:
			self.armourBelts[belt] = ArmourBelt(belt)
		self.armourDecks : Dict[enums.Deck, ArmourDeck]  = {}
		self.armourDecks[enums.Deck.MAIN_DECK] = ArmourDeck(enums.Deck.MAIN_DECK,self.getMainCoverage , self.ship)
		self.armourDecks[enums.Deck.FORE_DECK] = ArmourDeck(enums.Deck.FORE_DECK,self.getForeCoverage , self.ship)
		self.armourDecks[enums.Deck.AFT_DECK] = ArmourDeck(enums.Deck.AFT_DECK,self.getAftCoverage , self.ship)

	def getMainCoverage(self)	:
		return '1'
	def getForeCoverage(self)	:
		return '0.5'
	def getAftCoverage(self)	:
		return '0.75'

		#TODO: make dependent on hull shape