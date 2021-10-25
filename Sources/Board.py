from Deck import Deck  
from Card import Card,Attack,Defense,Distance,Safety

class Board():

    def __init__(self):
        self.lastBattle=Attack(4) #Derniere attaque subit initialisé à Feu Rouge
        self.lastSpeed=None #Derniere limite de vitesse subit
        self.safetyDeck=Deck() #Deck des cartes bottes
        self.distanceDeck=Deck() #Deck des cartes distance
        self.speedDeck=Deck() #Deck des cartes de la pile de vitesse
        self.battleDeck=Deck() #Deck des cartes bottes de la pile de bataille
    
    # getters et setters des attributs privés
    
    @property
    def safetyDeck(self):
        return self.__safetyDeck  
    
    @safetyDeck.setter
    def safetyDeck(self,deck):
        if not(isinstance(deck,Deck)):
            print("Erreur: safetyDeck ne peut prendre qu'une pile de type Deck")
        else :
            self.__safetyDeck=deck
    
    @property
    def distanceDeck(self):
        return self.__distanceDeck  
    
    @distanceDeck.setter
    def distanceDeck(self,deck):
        if not(isinstance(deck,Deck)):
            print("Erreur: distanceDeck ne peut prendre qu'une pile de type Deck")
        else :
            self.__distanceDeck=deck
    
    @property
    def lastBattle(self):
        return self.__lastBattle
    
    @lastBattle.setter
    def lastBattle(self,card):
        if (card == Attack(0) or card == Attack(1) or card == Attack(2) or card == Attack(4)):
            self.__lastBattle=card
        elif (card == None) :
            self.__lastBattle=None
        else :
            self.__lastBattle=None
            print("Erreur : lastBattle ne peut prendre qu'une carte de bataille ou None")
    
    @property
    def lastSpeed(self):
        return self.__lastSpeed  
    
    @lastSpeed.setter
    def lastSpeed(self,card):
        if (card == Attack(3)):
            self.__lastSpeed=card
        elif (card == None) :
            self.__lastSpeed=None
        else :
            self.__lastSpeed=None
            print("Erreur : lastSpeed ne peut prendre qu'une carte de limite de vitesse ou None")

    @property
    def speedDeck(self):
        return self.__speedDeck  
    
    @speedDeck.setter
    def speedDeck(self,deck):
        if not(isinstance(deck,Deck)) :
            print("Erreur: speedDeck ne peut prendre qu'une pile de type Deck")
        else :
            self.__speedDeck=deck
    
    @property
    def battleDeck(self):
        return self.__battleDeck  
    
    @battleDeck.setter
    def battleDeck(self,deck):
        if not(isinstance(deck,Deck)):
            print("Erreur: battleDeck ne peut prendre qu'une pile de type Deck")
        else :
            self.__battleDeck=deck

    def __str__(self):
        msg=""
        if(self.safetyDeck.cardList != []):
            for i in self.safetyDeck.cardList:
                msg+= f", {i.name}"
        
        if(self.lastSpeed != None):
            msg+= f", {self.lastSpeed.name}"
        
        if(self.lastBattle != None):
            msg+= f", {self.lastBattle.name}"
        
        return msg
    

    #méthode de sauvegarde des attributs de Board
    def save(self):
        msg=" "
        if self.lastBattle == None:
            msg+="None"
        else:
            msg+=str(self.lastBattle.ID)
        
        msg+=" "
        if self.lastSpeed == None:
            msg+="None"
        else:
            msg+=str(self.lastSpeed.ID)

        msg+=self.safetyDeck.save()
        msg+=self.distanceDeck.save()
        msg+=self.speedDeck.save()
        msg+=self.battleDeck.save()
        return msg

    #méthode de chargement des attributs de Board
    def load(self,boardLoad):
        if boardLoad[0] == 'None':
            self.lastBattle = None
        else :
           self.lastBattle = Attack(int(boardLoad[0]))
        if boardLoad[1] == 'None':
            self.lastSpeed = None
        else :
           self.lastSpeed = Attack(int(boardLoad[1]))
        i=2
        if(int(boardLoad[i])>0):
            i+=1
            safetyIdString=boardLoad[i];i+=1
            safetyTypeString=boardLoad[i]
            safetyId,safetyType=[],[]
            for x,y in zip(safetyIdString,safetyTypeString):
                safetyId.append(int(x))
                safetyType.append(int(y))    
            self.safetyDeck=Deck(safetyType,safetyId)
        else:
            self.safetyDeck=Deck()
        i+=1
        if(int(boardLoad[i])>0):
            i+=1
            distanceIdString=boardLoad[i];i+=1
            distanceTypeString=boardLoad[i]
            distanceId,distanceType=[],[]
            for x,y in zip(distanceIdString,distanceTypeString):
                distanceId.append(int(x))
                distanceType.append(int(y))    
            self.distanceDeck=Deck(distanceType,distanceId)
        else:
            self.distanceDeck=Deck()
        i+=1
        if(int(boardLoad[i])>0):
            i+=1
            speedIdString=boardLoad[i];i+=1
            speedTypeString=boardLoad[i]
            speedId,speedType=[],[]
            for x,y in zip(speedIdString,speedTypeString):
                speedId.append(int(x))
                speedType.append(int(y))    
            self.speedDeck=Deck(speedType,speedId)
        else:
            self.speedDeck=Deck()
        i+=1
        if(int(boardLoad[i])>0):
            i+=1
            battleIdString=boardLoad[i];i+=1
            battleTypeString=boardLoad[i]
            battleId,battleType=[],[]
            for x,y in zip(battleIdString,battleTypeString):
                battleId.append(int(x))
                battleType.append(int(y))    
            self.battleDeck=Deck(battleType,battleId)
        else:
            self.battleDeck=Deck()
